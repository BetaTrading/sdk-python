# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/auth/v1beta1/tx.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from pyinjective.proto.cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from pyinjective.proto.amino import amino_pb2 as amino_dot_amino__pb2
from pyinjective.proto.cosmos.auth.v1beta1 import auth_pb2 as cosmos_dot_auth_dot_v1beta1_dot_auth__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1c\x63osmos/auth/v1beta1/tx.proto\x12\x13\x63osmos.auth.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x11\x61mino/amino.proto\x1a\x1e\x63osmos/auth/v1beta1/auth.proto"\xbf\x01\n\x0fMsgUpdateParams\x12\x36\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\tauthority\x12>\n\x06params\x18\x02 \x01(\x0b\x32\x1b.cosmos.auth.v1beta1.ParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x06params:4\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*!cosmos-sdk/x/auth/MsgUpdateParams"\x19\n\x17MsgUpdateParamsResponse2p\n\x03Msg\x12\x62\n\x0cUpdateParams\x12$.cosmos.auth.v1beta1.MsgUpdateParams\x1a,.cosmos.auth.v1beta1.MsgUpdateParamsResponse\x1a\x05\x80\xe7\xb0*\x01\x42\xbb\x01\n\x17\x63om.cosmos.auth.v1beta1B\x07TxProtoP\x01Z)github.com/cosmos/cosmos-sdk/x/auth/types\xa2\x02\x03\x43\x41X\xaa\x02\x13\x43osmos.Auth.V1beta1\xca\x02\x13\x43osmos\\Auth\\V1beta1\xe2\x02\x1f\x43osmos\\Auth\\V1beta1\\GPBMetadata\xea\x02\x15\x43osmos::Auth::V1beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "cosmos.auth.v1beta1.tx_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals["DESCRIPTOR"]._serialized_options = (
        b"\n\027com.cosmos.auth.v1beta1B\007TxProtoP\001Z)github.com/cosmos/cosmos-sdk/x/auth/types\242\002\003CAX\252\002\023Cosmos.Auth.V1beta1\312\002\023Cosmos\\Auth\\V1beta1\342\002\037Cosmos\\Auth\\V1beta1\\GPBMetadata\352\002\025Cosmos::Auth::V1beta1"
    )
    _globals["_MSGUPDATEPARAMS"].fields_by_name["authority"]._loaded_options = None
    _globals["_MSGUPDATEPARAMS"].fields_by_name["authority"]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_MSGUPDATEPARAMS"].fields_by_name["params"]._loaded_options = None
    _globals["_MSGUPDATEPARAMS"].fields_by_name["params"]._serialized_options = b"\310\336\037\000\250\347\260*\001"
    _globals["_MSGUPDATEPARAMS"]._loaded_options = None
    _globals["_MSGUPDATEPARAMS"]._serialized_options = (
        b"\202\347\260*\tauthority\212\347\260*!cosmos-sdk/x/auth/MsgUpdateParams"
    )
    _globals["_MSG"]._loaded_options = None
    _globals["_MSG"]._serialized_options = b"\200\347\260*\001"
    _globals["_MSGUPDATEPARAMS"]._serialized_start = 179
    _globals["_MSGUPDATEPARAMS"]._serialized_end = 370
    _globals["_MSGUPDATEPARAMSRESPONSE"]._serialized_start = 372
    _globals["_MSGUPDATEPARAMSRESPONSE"]._serialized_end = 397
    _globals["_MSG"]._serialized_start = 399
    _globals["_MSG"]._serialized_end = 511
# @@protoc_insertion_point(module_scope)
