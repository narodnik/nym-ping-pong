# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='message.proto',
  package='message',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rmessage.proto\x12\x07message\"\x9a\x01\n\x0b\x43hatMessage\x12\x0f\n\x07\x43ontent\x18\x01 \x01(\x0c\x12\x17\n\x0fSenderPublicKey\x18\x02 \x01(\x0c\x12\x1f\n\x17SenderProviderPublicKey\x18\x03 \x01(\x0c\x12\x14\n\x0cMessageNonce\x18\x04 \x01(\x03\x12\x17\n\x0fSenderTimestamp\x18\x05 \x01(\x03\x12\x11\n\tSignature\x18\x06 \x01(\x0c\x62\x06proto3')
)




_CHATMESSAGE = _descriptor.Descriptor(
  name='ChatMessage',
  full_name='message.ChatMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Content', full_name='message.ChatMessage.Content', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='SenderPublicKey', full_name='message.ChatMessage.SenderPublicKey', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='SenderProviderPublicKey', full_name='message.ChatMessage.SenderProviderPublicKey', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='MessageNonce', full_name='message.ChatMessage.MessageNonce', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='SenderTimestamp', full_name='message.ChatMessage.SenderTimestamp', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Signature', full_name='message.ChatMessage.Signature', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=27,
  serialized_end=181,
)

DESCRIPTOR.message_types_by_name['ChatMessage'] = _CHATMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ChatMessage = _reflection.GeneratedProtocolMessageType('ChatMessage', (_message.Message,), {
  'DESCRIPTOR' : _CHATMESSAGE,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:message.ChatMessage)
  })
_sym_db.RegisterMessage(ChatMessage)


# @@protoc_insertion_point(module_scope)
