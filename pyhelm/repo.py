import cStringIO
import itertools
import os
from git import Repo
from urlparse import urlparse
import requests
import shutil
import tarfile
import tempfile
import yaml
import boto3.s3
from botocore.exceptions import ClientError


def _get_from_http(repo_url, file_url):
    """Downloads the Chart's repo index from HTTP(S)"""
    
    if repo_url not in file_url:
        file_url = os.path.join(repo_url, file_url)

    index = requests.get(file_url)
    return index.content

def _get_from_s3(repo_url, file_url):
    """Download the index / Chart from S3 bucket"""

    s3_client = boto3.client('s3')

    # NOTE(ljakimczuk): this is done for two
    # reasons. First, it allows to use this
    # function for either getting index.yaml
    # or Chart. Second, at least the Chartmuseum-
    # generated index.yaml may have the relative
    # URLs (guess due to its multi-tenancy), so
    # turning them into absolute is needed.
    if repo_url not in file_url:
        file_url = os.path.join(repo_url, file_url)
    
    file_url_parsed = urlparse(file_url)

    try:
        file_object = s3_client.get_object(
            Bucket=file_url_parsed.netloc,
            Key=file_url_parsed.path.strip('/'),
        )

        return file_object['Body'].read()
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchBucket':
            raise RuntimeError('%s repository not found' % file_url_parsed.netloc)
        elif e.response['Error']['Code'] == 'NoSuchKey':
            raise RuntimeError('%s not found in the repository' % file_url_parsed.path.strip('/'))
        else:
            raise

def _get_from_repo(repo_scheme, repo_url, file_url):
    """Wrap download from specific repository"""

    if repo_scheme == 's3':
        return _get_from_s3(
            repo_url,
            file_url,
        )
    elif repo_scheme in ('http', 'https'):
        return _get_from_http(
            repo_url,
            file_url,
        )
    else:
        raise RuntimeError('The %s repository not supported' % repo_scheme.upper())

def repo_index(repo_url):
    """Downloads the Chart's repo index"""
    repo_scheme = urlparse(repo_url).scheme

    return yaml.load(
        _get_from_repo(
            repo_scheme,
            repo_url,
            'index.yaml',
        )
    )

def from_repo(repo_url, chart, version=None):
    """Downloads the chart from a repo."""
    _tmp_dir = tempfile.mkdtemp(prefix='pyhelm-', dir='/tmp')
    repo_scheme = urlparse(repo_url).scheme
    index = repo_index(repo_url)

    if chart not in index['entries']:
        raise RuntimeError('Chart not found in repo')

    versions = index['entries'][chart]

    if version is not None:
        versions = itertools.ifilter(lambda k: k['version'] == version,
                                     versions)
    try:
        metadata = sorted(versions, key=lambda x: x['version'])[0]
        for url in metadata['urls']:
            fname = url.split('/')[-1]
            try:
                fobj = cStringIO.StringIO(
                    _get_from_repo(
                        repo_scheme,
                        repo_url,
                        url,
                    )
                )

                tar = tarfile.open(mode="r:*", fileobj=fobj)
                tar.extractall(_tmp_dir)
                return os.path.join(_tmp_dir, chart)
            except:
                # NOTE(flaper87): Catch requests errors
                # and untar errors
                pass
    except IndexError:
        raise RuntimeError('Chart version %s not found' % version)


def git_clone(repo_url, branch='master', path=''):
    """clones repo to a /tmp/ dir"""

    _tmp_dir = tempfile.mkdtemp(prefix='pyhelm-', dir='/tmp')
    repo = Repo.clone_from(repo_url, _tmp_dir, branch=branch)

    return os.path.join(_tmp_dir, path)


def source_cleanup(target_dir):
    """Clean up source."""
    shutil.rmtree(target_dir)
