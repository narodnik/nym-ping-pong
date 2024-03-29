# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: types.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import proto.structs_pb2 as structs__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='types.proto',
  package='types',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0btypes.proto\x12\x05types\x1a\rstructs.proto\"\xeb\x01\n\x07Request\x12)\n\x04send\x18\x02 \x01(\x0b\x32\x19.types.RequestSendMessageH\x00\x12,\n\x05\x66\x65tch\x18\x03 \x01(\x0b\x32\x1b.types.RequestFetchMessagesH\x00\x12+\n\x07\x63lients\x18\x04 \x01(\x0b\x32\x18.types.RequestGetClientsH\x00\x12+\n\x07\x64\x65tails\x18\x05 \x01(\x0b\x32\x18.types.RequestOwnDetailsH\x00\x12$\n\x05\x66lush\x18\x06 \x01(\x0b\x32\x13.types.RequestFlushH\x00\x42\x07\n\x05value\"N\n\x12RequestSendMessage\x12\x0f\n\x07message\x18\x01 \x01(\x0c\x12\'\n\trecipient\x18\x02 \x01(\x0b\x32\x14.config.ClientConfig\"\x16\n\x14RequestFetchMessages\"\x13\n\x11RequestGetClients\"\x13\n\x11RequestOwnDetails\"\x0e\n\x0cRequestFlush\"\xa0\x02\n\x08Response\x12-\n\texception\x18\x01 \x01(\x0b\x32\x18.types.ResponseExceptionH\x00\x12*\n\x04send\x18\x02 \x01(\x0b\x32\x1a.types.ResponseSendMessageH\x00\x12-\n\x05\x66\x65tch\x18\x03 \x01(\x0b\x32\x1c.types.ResponseFetchMessagesH\x00\x12,\n\x07\x63lients\x18\x04 \x01(\x0b\x32\x19.types.ResponseGetClientsH\x00\x12,\n\x07\x64\x65tails\x18\x05 \x01(\x0b\x32\x19.types.ResponseOwnDetailsH\x00\x12%\n\x05\x66lush\x18\x06 \x01(\x0b\x32\x14.types.ResponseFlushH\x00\x42\x07\n\x05value\"\"\n\x11ResponseException\x12\r\n\x05\x65rror\x18\x01 \x01(\t\"\x15\n\x13ResponseSendMessage\";\n\x12ResponseGetClients\x12%\n\x07\x63lients\x18\x01 \x03(\x0b\x32\x14.config.ClientConfig\";\n\x12ResponseOwnDetails\x12%\n\x07\x64\x65tails\x18\x01 \x01(\x0b\x32\x14.config.ClientConfig\"\x0f\n\rResponseFlush\")\n\x15ResponseFetchMessages\x12\x10\n\x08messages\x18\x01 \x03(\x0c\x62\x06proto3')
  ,
  dependencies=[structs__pb2.DESCRIPTOR,])




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='types.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='send', full_name='types.Request.send', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fetch', full_name='types.Request.fetch', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clients', full_name='types.Request.clients', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='details', full_name='types.Request.details', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flush', full_name='types.Request.flush', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='value', full_name='types.Request.value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=38,
  serialized_end=273,
)


_REQUESTSENDMESSAGE = _descriptor.Descriptor(
  name='RequestSendMessage',
  full_name='types.RequestSendMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='types.RequestSendMessage.message', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='recipient', full_name='types.RequestSendMessage.recipient', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=275,
  serialized_end=353,
)


_REQUESTFETCHMESSAGES = _descriptor.Descriptor(
  name='RequestFetchMessages',
  full_name='types.RequestFetchMessages',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=355,
  serialized_end=377,
)


_REQUESTGETCLIENTS = _descriptor.Descriptor(
  name='RequestGetClients',
  full_name='types.RequestGetClients',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=379,
  serialized_end=398,
)


_REQUESTOWNDETAILS = _descriptor.Descriptor(
  name='RequestOwnDetails',
  full_name='types.RequestOwnDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=400,
  serialized_end=419,
)


_REQUESTFLUSH = _descriptor.Descriptor(
  name='RequestFlush',
  full_name='types.RequestFlush',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=421,
  serialized_end=435,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='types.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='exception', full_name='types.Response.exception', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='send', full_name='types.Response.send', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fetch', full_name='types.Response.fetch', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clients', full_name='types.Response.clients', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='details', full_name='types.Response.details', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flush', full_name='types.Response.flush', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='value', full_name='types.Response.value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=438,
  serialized_end=726,
)


_RESPONSEEXCEPTION = _descriptor.Descriptor(
  name='ResponseException',
  full_name='types.ResponseException',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='types.ResponseException.error', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=728,
  serialized_end=762,
)


_RESPONSESENDMESSAGE = _descriptor.Descriptor(
  name='ResponseSendMessage',
  full_name='types.ResponseSendMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=764,
  serialized_end=785,
)


_RESPONSEGETCLIENTS = _descriptor.Descriptor(
  name='ResponseGetClients',
  full_name='types.ResponseGetClients',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='clients', full_name='types.ResponseGetClients.clients', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=787,
  serialized_end=846,
)


_RESPONSEOWNDETAILS = _descriptor.Descriptor(
  name='ResponseOwnDetails',
  full_name='types.ResponseOwnDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='details', full_name='types.ResponseOwnDetails.details', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=848,
  serialized_end=907,
)


_RESPONSEFLUSH = _descriptor.Descriptor(
  name='ResponseFlush',
  full_name='types.ResponseFlush',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=909,
  serialized_end=924,
)


_RESPONSEFETCHMESSAGES = _descriptor.Descriptor(
  name='ResponseFetchMessages',
  full_name='types.ResponseFetchMessages',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='messages', full_name='types.ResponseFetchMessages.messages', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=926,
  serialized_end=967,
)

_REQUEST.fields_by_name['send'].message_type = _REQUESTSENDMESSAGE
_REQUEST.fields_by_name['fetch'].message_type = _REQUESTFETCHMESSAGES
_REQUEST.fields_by_name['clients'].message_type = _REQUESTGETCLIENTS
_REQUEST.fields_by_name['details'].message_type = _REQUESTOWNDETAILS
_REQUEST.fields_by_name['flush'].message_type = _REQUESTFLUSH
_REQUEST.oneofs_by_name['value'].fields.append(
  _REQUEST.fields_by_name['send'])
_REQUEST.fields_by_name['send'].containing_oneof = _REQUEST.oneofs_by_name['value']
_REQUEST.oneofs_by_name['value'].fields.append(
  _REQUEST.fields_by_name['fetch'])
_REQUEST.fields_by_name['fetch'].containing_oneof = _REQUEST.oneofs_by_name['value']
_REQUEST.oneofs_by_name['value'].fields.append(
  _REQUEST.fields_by_name['clients'])
_REQUEST.fields_by_name['clients'].containing_oneof = _REQUEST.oneofs_by_name['value']
_REQUEST.oneofs_by_name['value'].fields.append(
  _REQUEST.fields_by_name['details'])
_REQUEST.fields_by_name['details'].containing_oneof = _REQUEST.oneofs_by_name['value']
_REQUEST.oneofs_by_name['value'].fields.append(
  _REQUEST.fields_by_name['flush'])
_REQUEST.fields_by_name['flush'].containing_oneof = _REQUEST.oneofs_by_name['value']
_REQUESTSENDMESSAGE.fields_by_name['recipient'].message_type = structs__pb2._CLIENTCONFIG
_RESPONSE.fields_by_name['exception'].message_type = _RESPONSEEXCEPTION
_RESPONSE.fields_by_name['send'].message_type = _RESPONSESENDMESSAGE
_RESPONSE.fields_by_name['fetch'].message_type = _RESPONSEFETCHMESSAGES
_RESPONSE.fields_by_name['clients'].message_type = _RESPONSEGETCLIENTS
_RESPONSE.fields_by_name['details'].message_type = _RESPONSEOWNDETAILS
_RESPONSE.fields_by_name['flush'].message_type = _RESPONSEFLUSH
_RESPONSE.oneofs_by_name['value'].fields.append(
  _RESPONSE.fields_by_name['exception'])
_RESPONSE.fields_by_name['exception'].containing_oneof = _RESPONSE.oneofs_by_name['value']
_RESPONSE.oneofs_by_name['value'].fields.append(
  _RESPONSE.fields_by_name['send'])
_RESPONSE.fields_by_name['send'].containing_oneof = _RESPONSE.oneofs_by_name['value']
_RESPONSE.oneofs_by_name['value'].fields.append(
  _RESPONSE.fields_by_name['fetch'])
_RESPONSE.fields_by_name['fetch'].containing_oneof = _RESPONSE.oneofs_by_name['value']
_RESPONSE.oneofs_by_name['value'].fields.append(
  _RESPONSE.fields_by_name['clients'])
_RESPONSE.fields_by_name['clients'].containing_oneof = _RESPONSE.oneofs_by_name['value']
_RESPONSE.oneofs_by_name['value'].fields.append(
  _RESPONSE.fields_by_name['details'])
_RESPONSE.fields_by_name['details'].containing_oneof = _RESPONSE.oneofs_by_name['value']
_RESPONSE.oneofs_by_name['value'].fields.append(
  _RESPONSE.fields_by_name['flush'])
_RESPONSE.fields_by_name['flush'].containing_oneof = _RESPONSE.oneofs_by_name['value']
_RESPONSEGETCLIENTS.fields_by_name['clients'].message_type = structs__pb2._CLIENTCONFIG
_RESPONSEOWNDETAILS.fields_by_name['details'].message_type = structs__pb2._CLIENTCONFIG
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['RequestSendMessage'] = _REQUESTSENDMESSAGE
DESCRIPTOR.message_types_by_name['RequestFetchMessages'] = _REQUESTFETCHMESSAGES
DESCRIPTOR.message_types_by_name['RequestGetClients'] = _REQUESTGETCLIENTS
DESCRIPTOR.message_types_by_name['RequestOwnDetails'] = _REQUESTOWNDETAILS
DESCRIPTOR.message_types_by_name['RequestFlush'] = _REQUESTFLUSH
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['ResponseException'] = _RESPONSEEXCEPTION
DESCRIPTOR.message_types_by_name['ResponseSendMessage'] = _RESPONSESENDMESSAGE
DESCRIPTOR.message_types_by_name['ResponseGetClients'] = _RESPONSEGETCLIENTS
DESCRIPTOR.message_types_by_name['ResponseOwnDetails'] = _RESPONSEOWNDETAILS
DESCRIPTOR.message_types_by_name['ResponseFlush'] = _RESPONSEFLUSH
DESCRIPTOR.message_types_by_name['ResponseFetchMessages'] = _RESPONSEFETCHMESSAGES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'types_pb2'
  # @@protoc_insertion_point(class_scope:types.Request)
  })
_sym_db.RegisterMessage(Request)

RequestSendMessage = _reflection.GeneratedProtocolMessageType('RequestSendMessage', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTSENDMESSAGE,
  '__module__' : 'types_pb2'
  # @@protoc_insertion_point(class_scope:types.RequestSendMessage)
  })
_sym_db.RegisterMessage(RequestSendMessage)

RequestFetchMessages = _reflection.GeneratedProtocolMessageType('RequestFetchMessages', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTFETCHMESSAGES,
  '__module__' : 'types_pb2'
  # @@protoc_insertion_point(class_scope:types.RequestFetchMessages)
  })
_sym_db.RegisterMessage(RequestFetchMessages)

RequestGetClients = _reflection.GeneratedProtocolMessageType('RequestGetClients', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTGETCLIENTS,
  '__module__' : 'types_pb2'
  # @@protoc_insertion_point(class_scope:types.RequestGetClients)
  })
_sym_db.RegisterMessage(RequestGetClients)

RequestOwnDetails = _reflection.GeneratedProtocolMessageType('RequestOwnDetails', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTOWNDETAILS,
  '__module__' : 'types_pb2'
  # @@protoc_insertion_point(class_scope:types.RequestOwnDetails)
  })
_sym_db.RegisterMessage(RequestOwnDetails)

RequestFlush = _reflection.GeneratedProtocolMessageType('RequestFlush', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTFLUSH,
  '__module__' : 'types_pb2'
  # @@protoc_insertion_point(class_scope:types.RequestFlush)
  })
_sym_db.RegisterMessage(RequestFlush)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'types_pb2'
  # @@protoc_insertion_point(class_scope:types.Response)
  })
_sym_db.RegisterMessage(Response)

ResponseException = _reflection.GeneratedProtocolMessageType('ResponseException', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEEXCEPTION,
  '__module__' : 'types_pb2'
  # @@protoc_insertion_point(class_scope:types.ResponseException)
  })
_sym_db.RegisterMessage(ResponseException)

ResponseSendMessage = _reflection.GeneratedProtocolMessageType('ResponseSendMessage', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSESENDMESSAGE,
  '__module__' : 'types_pb2'
  # @@protoc_insertion_point(class_scope:types.ResponseSendMessage)
  })
_sym_db.RegisterMessage(ResponseSendMessage)

ResponseGetClients = _reflection.GeneratedProtocolMessageType('ResponseGetClients', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEGETCLIENTS,
  '__module__' : 'types_pb2'
  # @@protoc_insertion_point(class_scope:types.ResponseGetClients)
  })
_sym_db.RegisterMessage(ResponseGetClients)

ResponseOwnDetails = _reflection.GeneratedProtocolMessageType('ResponseOwnDetails', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEOWNDETAILS,
  '__module__' : 'types_pb2'
  # @@protoc_insertion_point(class_scope:types.ResponseOwnDetails)
  })
_sym_db.RegisterMessage(ResponseOwnDetails)

ResponseFlush = _reflection.GeneratedProtocolMessageType('ResponseFlush', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEFLUSH,
  '__module__' : 'types_pb2'
  # @@protoc_insertion_point(class_scope:types.ResponseFlush)
  })
_sym_db.RegisterMessage(ResponseFlush)

ResponseFetchMessages = _reflection.GeneratedProtocolMessageType('ResponseFetchMessages', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEFETCHMESSAGES,
  '__module__' : 'types_pb2'
  # @@protoc_insertion_point(class_scope:types.ResponseFetchMessages)
  })
_sym_db.RegisterMessage(ResponseFetchMessages)


# @@protoc_insertion_point(module_scope)
