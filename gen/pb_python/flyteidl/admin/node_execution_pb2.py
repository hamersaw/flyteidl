# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flyteidl/admin/node_execution.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flyteidl.admin import common_pb2 as flyteidl_dot_admin_dot_common__pb2
from flyteidl.core import execution_pb2 as flyteidl_dot_core_dot_execution__pb2
from flyteidl.core import identifier_pb2 as flyteidl_dot_core_dot_identifier__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='flyteidl/admin/node_execution.proto',
  package='flyteidl.admin',
  syntax='proto3',
  serialized_pb=_b('\n#flyteidl/admin/node_execution.proto\x12\x0e\x66lyteidl.admin\x1a\x1b\x66lyteidl/admin/common.proto\x1a\x1d\x66lyteidl/core/execution.proto\x1a\x1e\x66lyteidl/core/identifier.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\"M\n\x17NodeExecutionGetRequest\x12\x32\n\x02id\x18\x01 \x01(\x0b\x32&.flyteidl.core.NodeExecutionIdentifier\"q\n\x18NodeExecutionListRequest\x12\r\n\x05limit\x18\x01 \x01(\r\x12\x0e\n\x06offset\x18\x02 \x01(\r\x12\x0f\n\x07\x66ilters\x18\x03 \x01(\t\x12%\n\x07sort_by\x18\x04 \x01(\x0b\x32\x14.flyteidl.admin.Sort\"\x8d\x01\n\rNodeExecution\x12\x32\n\x02id\x18\x01 \x01(\x0b\x32&.flyteidl.core.NodeExecutionIdentifier\x12\x11\n\tinput_uri\x18\x02 \x01(\t\x12\x35\n\x07\x63losure\x18\x03 \x01(\x0b\x32$.flyteidl.admin.NodeExecutionClosure\"K\n\x11NodeExecutionList\x12\x36\n\x0fnode_executions\x18\x01 \x03(\x0b\x32\x1d.flyteidl.admin.NodeExecution\"\xdc\x02\n\x14NodeExecutionClosure\x12\x14\n\noutput_uri\x18\x01 \x01(\tH\x00\x12.\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1d.flyteidl.core.ExecutionErrorH\x00\x12\x30\n\x05phase\x18\x03 \x01(\x0e\x32!.flyteidl.core.NodeExecutionPhase\x12.\n\nstarted_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x08\x64uration\x18\x05 \x01(\x0b\x32\x19.google.protobuf.Duration\x12.\n\ncreated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x0f\n\routput_resultB3Z1github.com/lyft/flyteidl/gen/pb-go/flyteidl/adminb\x06proto3')
  ,
  dependencies=[flyteidl_dot_admin_dot_common__pb2.DESCRIPTOR,flyteidl_dot_core_dot_execution__pb2.DESCRIPTOR,flyteidl_dot_core_dot_identifier__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,])




_NODEEXECUTIONGETREQUEST = _descriptor.Descriptor(
  name='NodeExecutionGetRequest',
  full_name='flyteidl.admin.NodeExecutionGetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='flyteidl.admin.NodeExecutionGetRequest.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=212,
  serialized_end=289,
)


_NODEEXECUTIONLISTREQUEST = _descriptor.Descriptor(
  name='NodeExecutionListRequest',
  full_name='flyteidl.admin.NodeExecutionListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='limit', full_name='flyteidl.admin.NodeExecutionListRequest.limit', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset', full_name='flyteidl.admin.NodeExecutionListRequest.offset', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filters', full_name='flyteidl.admin.NodeExecutionListRequest.filters', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sort_by', full_name='flyteidl.admin.NodeExecutionListRequest.sort_by', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=291,
  serialized_end=404,
)


_NODEEXECUTION = _descriptor.Descriptor(
  name='NodeExecution',
  full_name='flyteidl.admin.NodeExecution',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='flyteidl.admin.NodeExecution.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='input_uri', full_name='flyteidl.admin.NodeExecution.input_uri', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='closure', full_name='flyteidl.admin.NodeExecution.closure', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=407,
  serialized_end=548,
)


_NODEEXECUTIONLIST = _descriptor.Descriptor(
  name='NodeExecutionList',
  full_name='flyteidl.admin.NodeExecutionList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_executions', full_name='flyteidl.admin.NodeExecutionList.node_executions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=550,
  serialized_end=625,
)


_NODEEXECUTIONCLOSURE = _descriptor.Descriptor(
  name='NodeExecutionClosure',
  full_name='flyteidl.admin.NodeExecutionClosure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='output_uri', full_name='flyteidl.admin.NodeExecutionClosure.output_uri', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='flyteidl.admin.NodeExecutionClosure.error', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='phase', full_name='flyteidl.admin.NodeExecutionClosure.phase', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='started_at', full_name='flyteidl.admin.NodeExecutionClosure.started_at', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration', full_name='flyteidl.admin.NodeExecutionClosure.duration', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='flyteidl.admin.NodeExecutionClosure.created_at', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='flyteidl.admin.NodeExecutionClosure.updated_at', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='output_result', full_name='flyteidl.admin.NodeExecutionClosure.output_result',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=628,
  serialized_end=976,
)

_NODEEXECUTIONGETREQUEST.fields_by_name['id'].message_type = flyteidl_dot_core_dot_identifier__pb2._NODEEXECUTIONIDENTIFIER
_NODEEXECUTIONLISTREQUEST.fields_by_name['sort_by'].message_type = flyteidl_dot_admin_dot_common__pb2._SORT
_NODEEXECUTION.fields_by_name['id'].message_type = flyteidl_dot_core_dot_identifier__pb2._NODEEXECUTIONIDENTIFIER
_NODEEXECUTION.fields_by_name['closure'].message_type = _NODEEXECUTIONCLOSURE
_NODEEXECUTIONLIST.fields_by_name['node_executions'].message_type = _NODEEXECUTION
_NODEEXECUTIONCLOSURE.fields_by_name['error'].message_type = flyteidl_dot_core_dot_execution__pb2._EXECUTIONERROR
_NODEEXECUTIONCLOSURE.fields_by_name['phase'].enum_type = flyteidl_dot_core_dot_execution__pb2._NODEEXECUTIONPHASE
_NODEEXECUTIONCLOSURE.fields_by_name['started_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_NODEEXECUTIONCLOSURE.fields_by_name['duration'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_NODEEXECUTIONCLOSURE.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_NODEEXECUTIONCLOSURE.fields_by_name['updated_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_NODEEXECUTIONCLOSURE.oneofs_by_name['output_result'].fields.append(
  _NODEEXECUTIONCLOSURE.fields_by_name['output_uri'])
_NODEEXECUTIONCLOSURE.fields_by_name['output_uri'].containing_oneof = _NODEEXECUTIONCLOSURE.oneofs_by_name['output_result']
_NODEEXECUTIONCLOSURE.oneofs_by_name['output_result'].fields.append(
  _NODEEXECUTIONCLOSURE.fields_by_name['error'])
_NODEEXECUTIONCLOSURE.fields_by_name['error'].containing_oneof = _NODEEXECUTIONCLOSURE.oneofs_by_name['output_result']
DESCRIPTOR.message_types_by_name['NodeExecutionGetRequest'] = _NODEEXECUTIONGETREQUEST
DESCRIPTOR.message_types_by_name['NodeExecutionListRequest'] = _NODEEXECUTIONLISTREQUEST
DESCRIPTOR.message_types_by_name['NodeExecution'] = _NODEEXECUTION
DESCRIPTOR.message_types_by_name['NodeExecutionList'] = _NODEEXECUTIONLIST
DESCRIPTOR.message_types_by_name['NodeExecutionClosure'] = _NODEEXECUTIONCLOSURE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NodeExecutionGetRequest = _reflection.GeneratedProtocolMessageType('NodeExecutionGetRequest', (_message.Message,), dict(
  DESCRIPTOR = _NODEEXECUTIONGETREQUEST,
  __module__ = 'flyteidl.admin.node_execution_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.NodeExecutionGetRequest)
  ))
_sym_db.RegisterMessage(NodeExecutionGetRequest)

NodeExecutionListRequest = _reflection.GeneratedProtocolMessageType('NodeExecutionListRequest', (_message.Message,), dict(
  DESCRIPTOR = _NODEEXECUTIONLISTREQUEST,
  __module__ = 'flyteidl.admin.node_execution_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.NodeExecutionListRequest)
  ))
_sym_db.RegisterMessage(NodeExecutionListRequest)

NodeExecution = _reflection.GeneratedProtocolMessageType('NodeExecution', (_message.Message,), dict(
  DESCRIPTOR = _NODEEXECUTION,
  __module__ = 'flyteidl.admin.node_execution_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.NodeExecution)
  ))
_sym_db.RegisterMessage(NodeExecution)

NodeExecutionList = _reflection.GeneratedProtocolMessageType('NodeExecutionList', (_message.Message,), dict(
  DESCRIPTOR = _NODEEXECUTIONLIST,
  __module__ = 'flyteidl.admin.node_execution_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.NodeExecutionList)
  ))
_sym_db.RegisterMessage(NodeExecutionList)

NodeExecutionClosure = _reflection.GeneratedProtocolMessageType('NodeExecutionClosure', (_message.Message,), dict(
  DESCRIPTOR = _NODEEXECUTIONCLOSURE,
  __module__ = 'flyteidl.admin.node_execution_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.NodeExecutionClosure)
  ))
_sym_db.RegisterMessage(NodeExecutionClosure)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z1github.com/lyft/flyteidl/gen/pb-go/flyteidl/admin'))
# @@protoc_insertion_point(module_scope)
