# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/app/runtime/v1alpha1/module.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.cosmos.app.v1alpha1 import module_pb2 as cosmos_dot_app_dot_v1alpha1_dot_module__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n(cosmos/app/runtime/v1alpha1/module.proto\x12\x1b\x63osmos.app.runtime.v1alpha1\x1a cosmos/app/v1alpha1/module.proto"\xdc\x03\n\x06Module\x12\x19\n\x08\x61pp_name\x18\x01 \x01(\tR\x07\x61ppName\x12%\n\x0e\x62\x65gin_blockers\x18\x02 \x03(\tR\rbeginBlockers\x12!\n\x0c\x65nd_blockers\x18\x03 \x03(\tR\x0b\x65ndBlockers\x12!\n\x0cinit_genesis\x18\x04 \x03(\tR\x0binitGenesis\x12%\n\x0e\x65xport_genesis\x18\x05 \x03(\tR\rexportGenesis\x12[\n\x13override_store_keys\x18\x06 \x03(\x0b\x32+.cosmos.app.runtime.v1alpha1.StoreKeyConfigR\x11overrideStoreKeys\x12)\n\x10order_migrations\x18\x07 \x03(\tR\x0forderMigrations\x12"\n\x0cprecommiters\x18\x08 \x03(\tR\x0cprecommiters\x12\x32\n\x15prepare_check_staters\x18\t \x03(\tR\x13prepareCheckStaters:C\xba\xc0\x96\xda\x01=\n$github.com/cosmos/cosmos-sdk/runtime\x12\x15\n\x13\x63osmos.app.v1alpha1"S\n\x0eStoreKeyConfig\x12\x1f\n\x0bmodule_name\x18\x01 \x01(\tR\nmoduleName\x12 \n\x0ckv_store_key\x18\x02 \x01(\tR\nkvStoreKeyB\xbd\x01\n\x1f\x63om.cosmos.app.runtime.v1alpha1B\x0bModuleProtoP\x01\xa2\x02\x03\x43\x41R\xaa\x02\x1b\x43osmos.App.Runtime.V1alpha1\xca\x02\x1b\x43osmos\\App\\Runtime\\V1alpha1\xe2\x02\'Cosmos\\App\\Runtime\\V1alpha1\\GPBMetadata\xea\x02\x1e\x43osmos::App::Runtime::V1alpha1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "cosmos.app.runtime.v1alpha1.module_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals["DESCRIPTOR"]._serialized_options = (
        b"\n\037com.cosmos.app.runtime.v1alpha1B\013ModuleProtoP\001\242\002\003CAR\252\002\033Cosmos.App.Runtime.V1alpha1\312\002\033Cosmos\\App\\Runtime\\V1alpha1\342\002'Cosmos\\App\\Runtime\\V1alpha1\\GPBMetadata\352\002\036Cosmos::App::Runtime::V1alpha1"
    )
    _globals["_MODULE"]._loaded_options = None
    _globals["_MODULE"]._serialized_options = (
        b"\272\300\226\332\001=\n$github.com/cosmos/cosmos-sdk/runtime\022\025\n\023cosmos.app.v1alpha1"
    )
    _globals["_MODULE"]._serialized_start = 108
    _globals["_MODULE"]._serialized_end = 584
    _globals["_STOREKEYCONFIG"]._serialized_start = 586
    _globals["_STOREKEYCONFIG"]._serialized_end = 669
# @@protoc_insertion_point(module_scope)
