# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/staking/v1beta1/genesis.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.cosmos.staking.v1beta1 import staking_pb2 as cosmos_dot_staking_dot_v1beta1_dot_staking__pb2
from pyinjective.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from pyinjective.proto.amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$cosmos/staking/v1beta1/genesis.proto\x12\x16\x63osmos.staking.v1beta1\x1a\x14gogoproto/gogo.proto\x1a$cosmos/staking/v1beta1/staking.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x11\x61mino/amino.proto\"\xa2\x04\n\x0cGenesisState\x12\x39\n\x06params\x18\x01 \x01(\x0b\x32\x1e.cosmos.staking.v1beta1.ParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12J\n\x10last_total_power\x18\x02 \x01(\x0c\x42\x30\xc8\xde\x1f\x00\xda\xde\x1f\x15\x63osmossdk.io/math.Int\xd2\xb4-\ncosmos.Int\xa8\xe7\xb0*\x01\x12T\n\x15last_validator_powers\x18\x03 \x03(\x0b\x32*.cosmos.staking.v1beta1.LastValidatorPowerB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12@\n\nvalidators\x18\x04 \x03(\x0b\x32!.cosmos.staking.v1beta1.ValidatorB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12\x42\n\x0b\x64\x65legations\x18\x05 \x03(\x0b\x32\".cosmos.staking.v1beta1.DelegationB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12U\n\x15unbonding_delegations\x18\x06 \x03(\x0b\x32+.cosmos.staking.v1beta1.UnbondingDelegationB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12\x46\n\rredelegations\x18\x07 \x03(\x0b\x32$.cosmos.staking.v1beta1.RedelegationB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12\x10\n\x08\x65xported\x18\x08 \x01(\x08\"X\n\x12LastValidatorPower\x12)\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\r\n\x05power\x18\x02 \x01(\x03:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x42.Z,github.com/cosmos/cosmos-sdk/x/staking/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.staking.v1beta1.genesis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z,github.com/cosmos/cosmos-sdk/x/staking/types'
  _globals['_GENESISSTATE'].fields_by_name['params']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['params']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_GENESISSTATE'].fields_by_name['last_total_power']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['last_total_power']._serialized_options = b'\310\336\037\000\332\336\037\025cosmossdk.io/math.Int\322\264-\ncosmos.Int\250\347\260*\001'
  _globals['_GENESISSTATE'].fields_by_name['last_validator_powers']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['last_validator_powers']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_GENESISSTATE'].fields_by_name['validators']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['validators']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_GENESISSTATE'].fields_by_name['delegations']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['delegations']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_GENESISSTATE'].fields_by_name['unbonding_delegations']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['unbonding_delegations']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_GENESISSTATE'].fields_by_name['redelegations']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['redelegations']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_LASTVALIDATORPOWER'].fields_by_name['address']._loaded_options = None
  _globals['_LASTVALIDATORPOWER'].fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_LASTVALIDATORPOWER']._loaded_options = None
  _globals['_LASTVALIDATORPOWER']._serialized_options = b'\210\240\037\000\350\240\037\000'
  _globals['_GENESISSTATE']._serialized_start=171
  _globals['_GENESISSTATE']._serialized_end=717
  _globals['_LASTVALIDATORPOWER']._serialized_start=719
  _globals['_LASTVALIDATORPOWER']._serialized_end=807
# @@protoc_insertion_point(module_scope)
