# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/core/commitment/v1/commitment.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.cosmos.ics23.v1 import proofs_pb2 as cosmos_dot_ics23_dot_v1_dot_proofs__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'ibc/core/commitment/v1/commitment.proto\x12\x16ibc.core.commitment.v1\x1a\x14gogoproto/gogo.proto\x1a\x1c\x63osmos/ics23/v1/proofs.proto\" \n\nMerkleRoot\x12\x0c\n\x04hash\x18\x01 \x01(\x0c:\x04\x88\xa0\x1f\x00\"\"\n\x0cMerklePrefix\x12\x12\n\nkey_prefix\x18\x01 \x01(\x0c\"\x1e\n\nMerklePath\x12\x10\n\x08key_path\x18\x01 \x03(\t\"?\n\x0bMerkleProof\x12\x30\n\x06proofs\x18\x01 \x03(\x0b\x32 .cosmos.ics23.v1.CommitmentProofB>Z<github.com/cosmos/ibc-go/v8/modules/core/23-commitment/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.core.commitment.v1.commitment_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z<github.com/cosmos/ibc-go/v8/modules/core/23-commitment/types'
  _globals['_MERKLEROOT']._loaded_options = None
  _globals['_MERKLEROOT']._serialized_options = b'\210\240\037\000'
  _globals['_MERKLEROOT']._serialized_start=119
  _globals['_MERKLEROOT']._serialized_end=151
  _globals['_MERKLEPREFIX']._serialized_start=153
  _globals['_MERKLEPREFIX']._serialized_end=187
  _globals['_MERKLEPATH']._serialized_start=189
  _globals['_MERKLEPATH']._serialized_end=219
  _globals['_MERKLEPROOF']._serialized_start=221
  _globals['_MERKLEPROOF']._serialized_end=284
# @@protoc_insertion_point(module_scope)
