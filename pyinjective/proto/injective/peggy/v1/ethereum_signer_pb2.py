# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/peggy/v1/ethereum_signer.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b"\n(injective/peggy/v1/ethereum_signer.proto\x12\x12injective.peggy.v1\x1a\x14gogoproto/gogo.proto*\x91\x01\n\x08SignType\x12\x15\n\x11SIGN_TYPE_UNKNOWN\x10\x00\x12\x32\n.SIGN_TYPE_ORCHESTRATOR_SIGNED_MULTI_SIG_UPDATE\x10\x01\x12\x30\n,SIGN_TYPE_ORCHESTRATOR_SIGNED_WITHDRAW_BATCH\x10\x02\x1a\x08\x88\xa3\x1e\x00\xa8\xa4\x1e\x00\x42\xe4\x01\n\x16\x63om.injective.peggy.v1B\x13\x45thereumSignerProtoP\x01ZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/peggy/types\xa2\x02\x03IPX\xaa\x02\x12Injective.Peggy.V1\xca\x02\x12Injective\\Peggy\\V1\xe2\x02\x1eInjective\\Peggy\\V1\\GPBMetadata\xea\x02\x14Injective::Peggy::V1b\x06proto3"
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "injective.peggy.v1.ethereum_signer_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals["DESCRIPTOR"]._serialized_options = (
        b"\n\026com.injective.peggy.v1B\023EthereumSignerProtoP\001ZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/peggy/types\242\002\003IPX\252\002\022Injective.Peggy.V1\312\002\022Injective\\Peggy\\V1\342\002\036Injective\\Peggy\\V1\\GPBMetadata\352\002\024Injective::Peggy::V1"
    )
    _globals["_SIGNTYPE"]._loaded_options = None
    _globals["_SIGNTYPE"]._serialized_options = b"\210\243\036\000\250\244\036\000"
    _globals["_SIGNTYPE"]._serialized_start = 87
    _globals["_SIGNTYPE"]._serialized_end = 232
# @@protoc_insertion_point(module_scope)
