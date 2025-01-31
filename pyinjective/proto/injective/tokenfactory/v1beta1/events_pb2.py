# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/tokenfactory/v1beta1/events.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from pyinjective.proto.cosmos.bank.v1beta1 import bank_pb2 as cosmos_dot_bank_dot_v1beta1_dot_bank__pb2
from pyinjective.proto.injective.tokenfactory.v1beta1 import (
    authorityMetadata_pb2 as injective_dot_tokenfactory_dot_v1beta1_dot_authorityMetadata__pb2,
)


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n+injective/tokenfactory/v1beta1/events.proto\x12\x1einjective.tokenfactory.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1e\x63osmos/bank/v1beta1/bank.proto\x1a\x36injective/tokenfactory/v1beta1/authorityMetadata.proto"D\n\x12\x45ventCreateTFDenom\x12\x18\n\x07\x61\x63\x63ount\x18\x01 \x01(\tR\x07\x61\x63\x63ount\x12\x14\n\x05\x64\x65nom\x18\x02 \x01(\tR\x05\x64\x65nom"x\n\x10\x45ventMintTFDenom\x12+\n\x11recipient_address\x18\x01 \x01(\tR\x10recipientAddress\x12\x37\n\x06\x61mount\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00R\x06\x61mount"p\n\x0e\x45ventBurnDenom\x12%\n\x0e\x62urner_address\x18\x01 \x01(\tR\rburnerAddress\x12\x37\n\x06\x61mount\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00R\x06\x61mount"V\n\x12\x45ventChangeTFAdmin\x12\x14\n\x05\x64\x65nom\x18\x01 \x01(\tR\x05\x64\x65nom\x12*\n\x11new_admin_address\x18\x02 \x01(\tR\x0fnewAdminAddress"p\n\x17\x45ventSetTFDenomMetadata\x12\x14\n\x05\x64\x65nom\x18\x01 \x01(\tR\x05\x64\x65nom\x12?\n\x08metadata\x18\x02 \x01(\x0b\x32\x1d.cosmos.bank.v1beta1.MetadataB\x04\xc8\xde\x1f\x00R\x08metadataB\x9f\x02\n"com.injective.tokenfactory.v1beta1B\x0b\x45ventsProtoP\x01ZRgithub.com/InjectiveLabs/injective-core/injective-chain/modules/tokenfactory/types\xa2\x02\x03ITX\xaa\x02\x1eInjective.Tokenfactory.V1beta1\xca\x02\x1eInjective\\Tokenfactory\\V1beta1\xe2\x02*Injective\\Tokenfactory\\V1beta1\\GPBMetadata\xea\x02 Injective::Tokenfactory::V1beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "injective.tokenfactory.v1beta1.events_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals["DESCRIPTOR"]._serialized_options = (
        b'\n"com.injective.tokenfactory.v1beta1B\013EventsProtoP\001ZRgithub.com/InjectiveLabs/injective-core/injective-chain/modules/tokenfactory/types\242\002\003ITX\252\002\036Injective.Tokenfactory.V1beta1\312\002\036Injective\\Tokenfactory\\V1beta1\342\002*Injective\\Tokenfactory\\V1beta1\\GPBMetadata\352\002 Injective::Tokenfactory::V1beta1'
    )
    _globals["_EVENTMINTTFDENOM"].fields_by_name["amount"]._loaded_options = None
    _globals["_EVENTMINTTFDENOM"].fields_by_name["amount"]._serialized_options = b"\310\336\037\000"
    _globals["_EVENTBURNDENOM"].fields_by_name["amount"]._loaded_options = None
    _globals["_EVENTBURNDENOM"].fields_by_name["amount"]._serialized_options = b"\310\336\037\000"
    _globals["_EVENTSETTFDENOMMETADATA"].fields_by_name["metadata"]._loaded_options = None
    _globals["_EVENTSETTFDENOMMETADATA"].fields_by_name["metadata"]._serialized_options = b"\310\336\037\000"
    _globals["_EVENTCREATETFDENOM"]._serialized_start = 221
    _globals["_EVENTCREATETFDENOM"]._serialized_end = 289
    _globals["_EVENTMINTTFDENOM"]._serialized_start = 291
    _globals["_EVENTMINTTFDENOM"]._serialized_end = 411
    _globals["_EVENTBURNDENOM"]._serialized_start = 413
    _globals["_EVENTBURNDENOM"]._serialized_end = 525
    _globals["_EVENTCHANGETFADMIN"]._serialized_start = 527
    _globals["_EVENTCHANGETFADMIN"]._serialized_end = 613
    _globals["_EVENTSETTFDENOMMETADATA"]._serialized_start = 615
    _globals["_EVENTSETTFDENOMMETADATA"]._serialized_end = 727
# @@protoc_insertion_point(module_scope)
