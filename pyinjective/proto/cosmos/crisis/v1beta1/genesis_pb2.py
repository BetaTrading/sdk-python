# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/crisis/v1beta1/genesis.proto
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
from pyinjective.proto.amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#cosmos/crisis/v1beta1/genesis.proto\x12\x15\x63osmos.crisis.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x11\x61mino/amino.proto\"W\n\x0cGenesisState\x12G\n\x0c\x63onstant_fee\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x0b\x63onstantFeeB\xcc\x01\n\x19\x63om.cosmos.crisis.v1beta1B\x0cGenesisProtoP\x01Z+github.com/cosmos/cosmos-sdk/x/crisis/types\xa2\x02\x03\x43\x43X\xaa\x02\x15\x43osmos.Crisis.V1beta1\xca\x02\x15\x43osmos\\Crisis\\V1beta1\xe2\x02!Cosmos\\Crisis\\V1beta1\\GPBMetadata\xea\x02\x17\x43osmos::Crisis::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.crisis.v1beta1.genesis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031com.cosmos.crisis.v1beta1B\014GenesisProtoP\001Z+github.com/cosmos/cosmos-sdk/x/crisis/types\242\002\003CCX\252\002\025Cosmos.Crisis.V1beta1\312\002\025Cosmos\\Crisis\\V1beta1\342\002!Cosmos\\Crisis\\V1beta1\\GPBMetadata\352\002\027Cosmos::Crisis::V1beta1'
  _globals['_GENESISSTATE'].fields_by_name['constant_fee']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['constant_fee']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_GENESISSTATE']._serialized_start=135
  _globals['_GENESISSTATE']._serialized_end=222
# @@protoc_insertion_point(module_scope)
