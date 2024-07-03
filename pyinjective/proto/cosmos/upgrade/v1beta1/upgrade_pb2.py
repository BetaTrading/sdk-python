# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/upgrade/v1beta1/upgrade.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from pyinjective.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from pyinjective.proto.amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$cosmos/upgrade/v1beta1/upgrade.proto\x12\x16\x63osmos.upgrade.v1beta1\x1a\x19google/protobuf/any.proto\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x11\x61mino/amino.proto\"\xc0\x01\n\x04Plan\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x39\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x0f\x18\x01\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01\x12\x0e\n\x06height\x18\x03 \x01(\x03\x12\x0c\n\x04info\x18\x04 \x01(\t\x12\x37\n\x15upgraded_client_state\x18\x05 \x01(\x0b\x32\x14.google.protobuf.AnyB\x02\x18\x01:\x18\xe8\xa0\x1f\x01\x8a\xe7\xb0*\x0f\x63osmos-sdk/Plan\"\xc1\x01\n\x17SoftwareUpgradeProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x35\n\x04plan\x18\x03 \x01(\x0b\x32\x1c.cosmos.upgrade.v1beta1.PlanB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:K\x18\x01\xe8\xa0\x1f\x01\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\x8a\xe7\xb0*\"cosmos-sdk/SoftwareUpgradeProposal\"\x96\x01\n\x1d\x43\x61ncelSoftwareUpgradeProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t:Q\x18\x01\xe8\xa0\x1f\x01\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\x8a\xe7\xb0*(cosmos-sdk/CancelSoftwareUpgradeProposal\"4\n\rModuleVersion\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x04:\x04\xe8\xa0\x1f\x01\x42\"Z\x1c\x63osmossdk.io/x/upgrade/types\xc8\xe1\x1e\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.upgrade.v1beta1.upgrade_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\034cosmossdk.io/x/upgrade/types\310\341\036\000'
  _globals['_PLAN'].fields_by_name['time']._loaded_options = None
  _globals['_PLAN'].fields_by_name['time']._serialized_options = b'\030\001\310\336\037\000\220\337\037\001\250\347\260*\001'
  _globals['_PLAN'].fields_by_name['upgraded_client_state']._loaded_options = None
  _globals['_PLAN'].fields_by_name['upgraded_client_state']._serialized_options = b'\030\001'
  _globals['_PLAN']._loaded_options = None
  _globals['_PLAN']._serialized_options = b'\350\240\037\001\212\347\260*\017cosmos-sdk/Plan'
  _globals['_SOFTWAREUPGRADEPROPOSAL'].fields_by_name['plan']._loaded_options = None
  _globals['_SOFTWAREUPGRADEPROPOSAL'].fields_by_name['plan']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_SOFTWAREUPGRADEPROPOSAL']._loaded_options = None
  _globals['_SOFTWAREUPGRADEPROPOSAL']._serialized_options = b'\030\001\350\240\037\001\312\264-\032cosmos.gov.v1beta1.Content\212\347\260*\"cosmos-sdk/SoftwareUpgradeProposal'
  _globals['_CANCELSOFTWAREUPGRADEPROPOSAL']._loaded_options = None
  _globals['_CANCELSOFTWAREUPGRADEPROPOSAL']._serialized_options = b'\030\001\350\240\037\001\312\264-\032cosmos.gov.v1beta1.Content\212\347\260*(cosmos-sdk/CancelSoftwareUpgradeProposal'
  _globals['_MODULEVERSION']._loaded_options = None
  _globals['_MODULEVERSION']._serialized_options = b'\350\240\037\001'
  _globals['_PLAN']._serialized_start=193
  _globals['_PLAN']._serialized_end=385
  _globals['_SOFTWAREUPGRADEPROPOSAL']._serialized_start=388
  _globals['_SOFTWAREUPGRADEPROPOSAL']._serialized_end=581
  _globals['_CANCELSOFTWAREUPGRADEPROPOSAL']._serialized_start=584
  _globals['_CANCELSOFTWAREUPGRADEPROPOSAL']._serialized_end=734
  _globals['_MODULEVERSION']._serialized_start=736
  _globals['_MODULEVERSION']._serialized_end=788
# @@protoc_insertion_point(module_scope)
