# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/expr/v1alpha1/explain.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.google.api.expr.v1alpha1 import value_pb2 as google_dot_api_dot_expr_dot_v1alpha1_dot_value__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n&google/api/expr/v1alpha1/explain.proto\x12\x18google.api.expr.v1alpha1\x1a$google/api/expr/v1alpha1/value.proto"\xce\x01\n\x07\x45xplain\x12\x37\n\x06values\x18\x01 \x03(\x0b\x32\x1f.google.api.expr.v1alpha1.ValueR\x06values\x12I\n\nexpr_steps\x18\x02 \x03(\x0b\x32*.google.api.expr.v1alpha1.Explain.ExprStepR\texprSteps\x1a;\n\x08\x45xprStep\x12\x0e\n\x02id\x18\x01 \x01(\x03R\x02id\x12\x1f\n\x0bvalue_index\x18\x02 \x01(\x05R\nvalueIndex:\x02\x18\x01\x42\xf0\x01\n\x1c\x63om.google.api.expr.v1alpha1B\x0c\x45xplainProtoP\x01Z<google.golang.org/genproto/googleapis/api/expr/v1alpha1;expr\xf8\x01\x01\xa2\x02\x03GAE\xaa\x02\x18Google.Api.Expr.V1alpha1\xca\x02\x18Google\\Api\\Expr\\V1alpha1\xe2\x02$Google\\Api\\Expr\\V1alpha1\\GPBMetadata\xea\x02\x1bGoogle::Api::Expr::V1alpha1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "google.api.expr.v1alpha1.explain_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals["DESCRIPTOR"]._serialized_options = (
        b"\n\034com.google.api.expr.v1alpha1B\014ExplainProtoP\001Z<google.golang.org/genproto/googleapis/api/expr/v1alpha1;expr\370\001\001\242\002\003GAE\252\002\030Google.Api.Expr.V1alpha1\312\002\030Google\\Api\\Expr\\V1alpha1\342\002$Google\\Api\\Expr\\V1alpha1\\GPBMetadata\352\002\033Google::Api::Expr::V1alpha1"
    )
    _globals["_EXPLAIN"]._loaded_options = None
    _globals["_EXPLAIN"]._serialized_options = b"\030\001"
    _globals["_EXPLAIN"]._serialized_start = 107
    _globals["_EXPLAIN"]._serialized_end = 313
    _globals["_EXPLAIN_EXPRSTEP"]._serialized_start = 250
    _globals["_EXPLAIN_EXPRSTEP"]._serialized_end = 309
# @@protoc_insertion_point(module_scope)
