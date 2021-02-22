# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: digimons.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='digimons.proto',
  package='digimons',
  syntax='proto3',
  serialized_options=b'Z\021./server/digimons',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0e\x64igimons.proto\x12\x08\x64igimons\"\x19\n\tDigiquest\x12\x0c\n\x04name\x18\x01 \x01(\t\"6\n\nDigisponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03img\x18\x02 \x01(\t\x12\r\n\x05level\x18\x03 \x01(\t2@\n\x07\x44iginfo\x12\x35\n\x06search\x12\x13.digimons.Digiquest\x1a\x14.digimons.Digisponse\"\x00\x42\x13Z\x11./server/digimonsb\x06proto3'
)




_DIGIQUEST = _descriptor.Descriptor(
  name='Digiquest',
  full_name='digimons.Digiquest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='digimons.Digiquest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=28,
  serialized_end=53,
)


_DIGISPONSE = _descriptor.Descriptor(
  name='Digisponse',
  full_name='digimons.Digisponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='digimons.Digisponse.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='img', full_name='digimons.Digisponse.img', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='level', full_name='digimons.Digisponse.level', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=55,
  serialized_end=109,
)

DESCRIPTOR.message_types_by_name['Digiquest'] = _DIGIQUEST
DESCRIPTOR.message_types_by_name['Digisponse'] = _DIGISPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Digiquest = _reflection.GeneratedProtocolMessageType('Digiquest', (_message.Message,), {
  'DESCRIPTOR' : _DIGIQUEST,
  '__module__' : 'digimons_pb2'
  # @@protoc_insertion_point(class_scope:digimons.Digiquest)
  })
_sym_db.RegisterMessage(Digiquest)

Digisponse = _reflection.GeneratedProtocolMessageType('Digisponse', (_message.Message,), {
  'DESCRIPTOR' : _DIGISPONSE,
  '__module__' : 'digimons_pb2'
  # @@protoc_insertion_point(class_scope:digimons.Digisponse)
  })
_sym_db.RegisterMessage(Digisponse)


DESCRIPTOR._options = None

_DIGINFO = _descriptor.ServiceDescriptor(
  name='Diginfo',
  full_name='digimons.Diginfo',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=111,
  serialized_end=175,
  methods=[
  _descriptor.MethodDescriptor(
    name='search',
    full_name='digimons.Diginfo.search',
    index=0,
    containing_service=None,
    input_type=_DIGIQUEST,
    output_type=_DIGISPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DIGINFO)

DESCRIPTOR.services_by_name['Diginfo'] = _DIGINFO

# @@protoc_insertion_point(module_scope)
