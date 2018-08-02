# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hapi/release/status.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from hapi.release import test_suite_pb2 as hapi_dot_release_dot_test__suite__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='hapi/release/status.proto',
  package='hapi.release',
  syntax='proto3',
  serialized_pb=_b('\n\x19hapi/release/status.proto\x12\x0chapi.release\x1a\x1dhapi/release/test_suite.proto\x1a\x19google/protobuf/any.proto\"\xa4\x02\n\x06Status\x12\'\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x19.hapi.release.Status.Code\x12\x11\n\tresources\x18\x03 \x01(\t\x12\r\n\x05notes\x18\x04 \x01(\t\x12\x34\n\x13last_test_suite_run\x18\x05 \x01(\x0b\x32\x17.hapi.release.TestSuite\"\x98\x01\n\x04\x43ode\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08\x44\x45PLOYED\x10\x01\x12\x0b\n\x07\x44\x45LETED\x10\x02\x12\x0e\n\nSUPERSEDED\x10\x03\x12\n\n\x06\x46\x41ILED\x10\x04\x12\x0c\n\x08\x44\x45LETING\x10\x05\x12\x13\n\x0fPENDING_INSTALL\x10\x06\x12\x13\n\x0fPENDING_UPGRADE\x10\x07\x12\x14\n\x10PENDING_ROLLBACK\x10\x08\x42\tZ\x07releaseb\x06proto3')
  ,
  dependencies=[hapi_dot_release_dot_test__suite__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_STATUS_CODE = _descriptor.EnumDescriptor(
  name='Code',
  full_name='hapi.release.Status.Code',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEPLOYED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUPERSEDED', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETING', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PENDING_INSTALL', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PENDING_UPGRADE', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PENDING_ROLLBACK', index=8, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=242,
  serialized_end=394,
)
_sym_db.RegisterEnumDescriptor(_STATUS_CODE)


_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='hapi.release.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='hapi.release.Status.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resources', full_name='hapi.release.Status.resources', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='notes', full_name='hapi.release.Status.notes', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_test_suite_run', full_name='hapi.release.Status.last_test_suite_run', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STATUS_CODE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=102,
  serialized_end=394,
)

_STATUS.fields_by_name['code'].enum_type = _STATUS_CODE
_STATUS.fields_by_name['last_test_suite_run'].message_type = hapi_dot_release_dot_test__suite__pb2._TESTSUITE
_STATUS_CODE.containing_type = _STATUS
DESCRIPTOR.message_types_by_name['Status'] = _STATUS

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), dict(
  DESCRIPTOR = _STATUS,
  __module__ = 'hapi.release.status_pb2'
  # @@protoc_insertion_point(class_scope:hapi.release.Status)
  ))
_sym_db.RegisterMessage(Status)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\007release'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
