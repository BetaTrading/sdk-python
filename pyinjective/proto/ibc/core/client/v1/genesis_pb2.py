# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/core/client/v1/genesis.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.ibc.core.client.v1 import client_pb2 as ibc_dot_core_dot_client_dot_v1_dot_client__pb2
from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n ibc/core/client/v1/genesis.proto\x12\x12ibc.core.client.v1\x1a\x1fibc/core/client/v1/client.proto\x1a\x14gogoproto/gogo.proto\"\x8d\x03\n\x0cGenesisState\x12Z\n\x07\x63lients\x18\x01 \x03(\x0b\x32).ibc.core.client.v1.IdentifiedClientStateB\x1e\xc8\xde\x1f\x00\xaa\xdf\x1f\x16IdentifiedClientStates\x12\x64\n\x11\x63lients_consensus\x18\x02 \x03(\x0b\x32).ibc.core.client.v1.ClientConsensusStatesB\x1e\xc8\xde\x1f\x00\xaa\xdf\x1f\x16\x43lientsConsensusStates\x12M\n\x10\x63lients_metadata\x18\x03 \x03(\x0b\x32-.ibc.core.client.v1.IdentifiedGenesisMetadataB\x04\xc8\xde\x1f\x00\x12\x30\n\x06params\x18\x04 \x01(\x0b\x32\x1a.ibc.core.client.v1.ParamsB\x04\xc8\xde\x1f\x00\x12\x1c\n\x10\x63reate_localhost\x18\x05 \x01(\x08\x42\x02\x18\x01\x12\x1c\n\x14next_client_sequence\x18\x06 \x01(\x04\"3\n\x0fGenesisMetadata\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c:\x04\x88\xa0\x1f\x00\"r\n\x19IdentifiedGenesisMetadata\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x42\n\x0f\x63lient_metadata\x18\x02 \x03(\x0b\x32#.ibc.core.client.v1.GenesisMetadataB\x04\xc8\xde\x1f\x00\x42:Z8github.com/cosmos/ibc-go/v8/modules/core/02-client/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.core.client.v1.genesis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z8github.com/cosmos/ibc-go/v8/modules/core/02-client/types'
  _globals['_GENESISSTATE'].fields_by_name['clients']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['clients']._serialized_options = b'\310\336\037\000\252\337\037\026IdentifiedClientStates'
  _globals['_GENESISSTATE'].fields_by_name['clients_consensus']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['clients_consensus']._serialized_options = b'\310\336\037\000\252\337\037\026ClientsConsensusStates'
  _globals['_GENESISSTATE'].fields_by_name['clients_metadata']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['clients_metadata']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE'].fields_by_name['params']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE'].fields_by_name['create_localhost']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['create_localhost']._serialized_options = b'\030\001'
  _globals['_GENESISMETADATA']._loaded_options = None
  _globals['_GENESISMETADATA']._serialized_options = b'\210\240\037\000'
  _globals['_IDENTIFIEDGENESISMETADATA'].fields_by_name['client_metadata']._loaded_options = None
  _globals['_IDENTIFIEDGENESISMETADATA'].fields_by_name['client_metadata']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE']._serialized_start=112
  _globals['_GENESISSTATE']._serialized_end=509
  _globals['_GENESISMETADATA']._serialized_start=511
  _globals['_GENESISMETADATA']._serialized_end=562
  _globals['_IDENTIFIEDGENESISMETADATA']._serialized_start=564
  _globals['_IDENTIFIEDGENESISMETADATA']._serialized_end=678
# @@protoc_insertion_point(module_scope)
