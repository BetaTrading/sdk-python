# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/core/connection/v1/connection.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ibc.core.commitment.v1 import commitment_pb2 as ibc_dot_core_dot_commitment_dot_v1_dot_commitment__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'ibc/core/connection/v1/connection.proto\x12\x16ibc.core.connection.v1\x1a\x14gogoproto/gogo.proto\x1a\'ibc/core/commitment/v1/commitment.proto\"\xe1\x01\n\rConnectionEnd\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x31\n\x08versions\x18\x02 \x03(\x0b\x32\x1f.ibc.core.connection.v1.Version\x12,\n\x05state\x18\x03 \x01(\x0e\x32\x1d.ibc.core.connection.v1.State\x12@\n\x0c\x63ounterparty\x18\x04 \x01(\x0b\x32$.ibc.core.connection.v1.CounterpartyB\x04\xc8\xde\x1f\x00\x12\x14\n\x0c\x64\x65lay_period\x18\x05 \x01(\x04:\x04\x88\xa0\x1f\x00\"\xf4\x01\n\x14IdentifiedConnection\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tclient_id\x18\x02 \x01(\t\x12\x31\n\x08versions\x18\x03 \x03(\x0b\x32\x1f.ibc.core.connection.v1.Version\x12,\n\x05state\x18\x04 \x01(\x0e\x32\x1d.ibc.core.connection.v1.State\x12@\n\x0c\x63ounterparty\x18\x05 \x01(\x0b\x32$.ibc.core.connection.v1.CounterpartyB\x04\xc8\xde\x1f\x00\x12\x14\n\x0c\x64\x65lay_period\x18\x06 \x01(\x04:\x04\x88\xa0\x1f\x00\"z\n\x0c\x43ounterparty\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x15\n\rconnection_id\x18\x02 \x01(\t\x12:\n\x06prefix\x18\x03 \x01(\x0b\x32$.ibc.core.commitment.v1.MerklePrefixB\x04\xc8\xde\x1f\x00:\x04\x88\xa0\x1f\x00\"\x1c\n\x0b\x43lientPaths\x12\r\n\x05paths\x18\x01 \x03(\t\"3\n\x0f\x43onnectionPaths\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\r\n\x05paths\x18\x02 \x03(\t\"5\n\x07Version\x12\x12\n\nidentifier\x18\x01 \x01(\t\x12\x10\n\x08\x66\x65\x61tures\x18\x02 \x03(\t:\x04\x88\xa0\x1f\x00\"-\n\x06Params\x12#\n\x1bmax_expected_time_per_block\x18\x01 \x01(\x04*\x99\x01\n\x05State\x12\x36\n\x1fSTATE_UNINITIALIZED_UNSPECIFIED\x10\x00\x1a\x11\x8a\x9d \rUNINITIALIZED\x12\x18\n\nSTATE_INIT\x10\x01\x1a\x08\x8a\x9d \x04INIT\x12\x1e\n\rSTATE_TRYOPEN\x10\x02\x1a\x0b\x8a\x9d \x07TRYOPEN\x12\x18\n\nSTATE_OPEN\x10\x03\x1a\x08\x8a\x9d \x04OPEN\x1a\x04\x88\xa3\x1e\x00\x42>Z<github.com/cosmos/ibc-go/v7/modules/core/03-connection/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.core.connection.v1.connection_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z<github.com/cosmos/ibc-go/v7/modules/core/03-connection/types'
  _STATE._options = None
  _STATE._serialized_options = b'\210\243\036\000'
  _STATE.values_by_name["STATE_UNINITIALIZED_UNSPECIFIED"]._options = None
  _STATE.values_by_name["STATE_UNINITIALIZED_UNSPECIFIED"]._serialized_options = b'\212\235 \rUNINITIALIZED'
  _STATE.values_by_name["STATE_INIT"]._options = None
  _STATE.values_by_name["STATE_INIT"]._serialized_options = b'\212\235 \004INIT'
  _STATE.values_by_name["STATE_TRYOPEN"]._options = None
  _STATE.values_by_name["STATE_TRYOPEN"]._serialized_options = b'\212\235 \007TRYOPEN'
  _STATE.values_by_name["STATE_OPEN"]._options = None
  _STATE.values_by_name["STATE_OPEN"]._serialized_options = b'\212\235 \004OPEN'
  _CONNECTIONEND.fields_by_name['counterparty']._options = None
  _CONNECTIONEND.fields_by_name['counterparty']._serialized_options = b'\310\336\037\000'
  _CONNECTIONEND._options = None
  _CONNECTIONEND._serialized_options = b'\210\240\037\000'
  _IDENTIFIEDCONNECTION.fields_by_name['counterparty']._options = None
  _IDENTIFIEDCONNECTION.fields_by_name['counterparty']._serialized_options = b'\310\336\037\000'
  _IDENTIFIEDCONNECTION._options = None
  _IDENTIFIEDCONNECTION._serialized_options = b'\210\240\037\000'
  _COUNTERPARTY.fields_by_name['prefix']._options = None
  _COUNTERPARTY.fields_by_name['prefix']._serialized_options = b'\310\336\037\000'
  _COUNTERPARTY._options = None
  _COUNTERPARTY._serialized_options = b'\210\240\037\000'
  _VERSION._options = None
  _VERSION._serialized_options = b'\210\240\037\000'
  _STATE._serialized_start=915
  _STATE._serialized_end=1068
  _CONNECTIONEND._serialized_start=131
  _CONNECTIONEND._serialized_end=356
  _IDENTIFIEDCONNECTION._serialized_start=359
  _IDENTIFIEDCONNECTION._serialized_end=603
  _COUNTERPARTY._serialized_start=605
  _COUNTERPARTY._serialized_end=727
  _CLIENTPATHS._serialized_start=729
  _CLIENTPATHS._serialized_end=757
  _CONNECTIONPATHS._serialized_start=759
  _CONNECTIONPATHS._serialized_end=810
  _VERSION._serialized_start=812
  _VERSION._serialized_end=865
  _PARAMS._serialized_start=867
  _PARAMS._serialized_end=912
# @@protoc_insertion_point(module_scope)
