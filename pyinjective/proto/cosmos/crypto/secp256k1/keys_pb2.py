# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/crypto/secp256k1/keys.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.amino import amino_pb2 as amino_dot_amino__pb2
from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"cosmos/crypto/secp256k1/keys.proto\x12\x17\x63osmos.crypto.secp256k1\x1a\x11\x61mino/amino.proto\x1a\x14gogoproto/gogo.proto\"M\n\x06PubKey\x12\x10\n\x03key\x18\x01 \x01(\x0cR\x03key:1\x98\xa0\x1f\x00\x8a\xe7\xb0*\x1atendermint/PubKeySecp256k1\x92\xe7\xb0*\tkey_field\"K\n\x07PrivKey\x12\x10\n\x03key\x18\x01 \x01(\x0cR\x03key:.\x8a\xe7\xb0*\x1btendermint/PrivKeySecp256k1\x92\xe7\xb0*\tkey_fieldB\xda\x01\n\x1b\x63om.cosmos.crypto.secp256k1B\tKeysProtoP\x01Z2github.com/cosmos/cosmos-sdk/crypto/keys/secp256k1\xa2\x02\x03\x43\x43S\xaa\x02\x17\x43osmos.Crypto.Secp256k1\xca\x02\x17\x43osmos\\Crypto\\Secp256k1\xe2\x02#Cosmos\\Crypto\\Secp256k1\\GPBMetadata\xea\x02\x19\x43osmos::Crypto::Secp256k1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.crypto.secp256k1.keys_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.cosmos.crypto.secp256k1B\tKeysProtoP\001Z2github.com/cosmos/cosmos-sdk/crypto/keys/secp256k1\242\002\003CCS\252\002\027Cosmos.Crypto.Secp256k1\312\002\027Cosmos\\Crypto\\Secp256k1\342\002#Cosmos\\Crypto\\Secp256k1\\GPBMetadata\352\002\031Cosmos::Crypto::Secp256k1'
  _globals['_PUBKEY']._loaded_options = None
  _globals['_PUBKEY']._serialized_options = b'\230\240\037\000\212\347\260*\032tendermint/PubKeySecp256k1\222\347\260*\tkey_field'
  _globals['_PRIVKEY']._loaded_options = None
  _globals['_PRIVKEY']._serialized_options = b'\212\347\260*\033tendermint/PrivKeySecp256k1\222\347\260*\tkey_field'
  _globals['_PUBKEY']._serialized_start=104
  _globals['_PUBKEY']._serialized_end=181
  _globals['_PRIVKEY']._serialized_start=183
  _globals['_PRIVKEY']._serialized_end=258
# @@protoc_insertion_point(module_scope)
