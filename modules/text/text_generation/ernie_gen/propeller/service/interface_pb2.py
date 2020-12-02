# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: interface.proto

import sys
_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='interface.proto',
    package='interface',
    syntax='proto3',
    serialized_options=None,
    serialized_pb=_b(
        '\n\x0finterface.proto\x12\tinterface\"\'\n\x05Slots\x12\x1e\n\x05slots\x18\x01 \x03(\x0b\x32\x0f.interface.Slot\"\xb8\x01\n\x04Slot\x12\"\n\x04type\x18\x01 \x01(\x0e\x32\x14.interface.Slot.Type\x12\x0c\n\x04\x64ims\x18\x02 \x03(\x03\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"p\n\x04Type\x12\x08\n\x04\x42OOL\x10\x00\x12\t\n\x05INT16\x10\x01\x12\t\n\x05INT32\x10\x02\x12\t\n\x05INT64\x10\x03\x12\x08\n\x04\x46P16\x10\x04\x12\x08\n\x04\x46P32\x10\x05\x12\x08\n\x04\x46P64\x10\x06\x12\n\n\x06SIZE_T\x10\x13\x12\t\n\x05UINT8\x10\x14\x12\x08\n\x04INT8\x10\x15\x32:\n\tInference\x12-\n\x05Infer\x12\x10.interface.Slots\x1a\x10.interface.Slots\"\x00\x62\x06proto3'
    ))

_SLOT_TYPE = _descriptor.EnumDescriptor(
    name='Type',
    full_name='interface.Slot.Type',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(name='BOOL', index=0, number=0, serialized_options=None, type=None),
        _descriptor.EnumValueDescriptor(name='INT16', index=1, number=1, serialized_options=None, type=None),
        _descriptor.EnumValueDescriptor(name='INT32', index=2, number=2, serialized_options=None, type=None),
        _descriptor.EnumValueDescriptor(name='INT64', index=3, number=3, serialized_options=None, type=None),
        _descriptor.EnumValueDescriptor(name='FP16', index=4, number=4, serialized_options=None, type=None),
        _descriptor.EnumValueDescriptor(name='FP32', index=5, number=5, serialized_options=None, type=None),
        _descriptor.EnumValueDescriptor(name='FP64', index=6, number=6, serialized_options=None, type=None),
        _descriptor.EnumValueDescriptor(name='SIZE_T', index=7, number=19, serialized_options=None, type=None),
        _descriptor.EnumValueDescriptor(name='UINT8', index=8, number=20, serialized_options=None, type=None),
        _descriptor.EnumValueDescriptor(name='INT8', index=9, number=21, serialized_options=None, type=None),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=144,
    serialized_end=256,
)
_sym_db.RegisterEnumDescriptor(_SLOT_TYPE)

_SLOTS = _descriptor.Descriptor(
    name='Slots',
    full_name='interface.Slots',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='slots',
            full_name='interface.Slots.slots',
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=30,
    serialized_end=69,
)

_SLOT = _descriptor.Descriptor(
    name='Slot',
    full_name='interface.Slot',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='type',
            full_name='interface.Slot.type',
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='dims',
            full_name='interface.Slot.dims',
            index=1,
            number=2,
            type=3,
            cpp_type=2,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='data',
            full_name='interface.Slot.data',
            index=2,
            number=3,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[
        _SLOT_TYPE,
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=72,
    serialized_end=256,
)

_SLOTS.fields_by_name['slots'].message_type = _SLOT
_SLOT.fields_by_name['type'].enum_type = _SLOT_TYPE
_SLOT_TYPE.containing_type = _SLOT
DESCRIPTOR.message_types_by_name['Slots'] = _SLOTS
DESCRIPTOR.message_types_by_name['Slot'] = _SLOT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Slots = _reflection.GeneratedProtocolMessageType(
    'Slots',
    (_message.Message, ),
    {
        'DESCRIPTOR': _SLOTS,
        '__module__': 'interface_pb2'
        # @@protoc_insertion_point(class_scope:interface.Slots)
    })
_sym_db.RegisterMessage(Slots)

Slot = _reflection.GeneratedProtocolMessageType(
    'Slot',
    (_message.Message, ),
    {
        'DESCRIPTOR': _SLOT,
        '__module__': 'interface_pb2'
        # @@protoc_insertion_point(class_scope:interface.Slot)
    })
_sym_db.RegisterMessage(Slot)

_INFERENCE = _descriptor.ServiceDescriptor(
    name='Inference',
    full_name='interface.Inference',
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    serialized_start=258,
    serialized_end=316,
    methods=[
        _descriptor.MethodDescriptor(
            name='Infer',
            full_name='interface.Inference.Infer',
            index=0,
            containing_service=None,
            input_type=_SLOTS,
            output_type=_SLOTS,
            serialized_options=None,
        ),
    ])
_sym_db.RegisterServiceDescriptor(_INFERENCE)

DESCRIPTOR.services_by_name['Inference'] = _INFERENCE

# @@protoc_insertion_point(module_scope)