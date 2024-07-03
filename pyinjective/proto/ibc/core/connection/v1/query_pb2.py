# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/core/connection/v1/query.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from pyinjective.proto.ibc.core.client.v1 import client_pb2 as ibc_dot_core_dot_client_dot_v1_dot_client__pb2
from pyinjective.proto.ibc.core.connection.v1 import connection_pb2 as ibc_dot_core_dot_connection_dot_v1_dot_connection__pb2
from pyinjective.proto.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"ibc/core/connection/v1/query.proto\x12\x16ibc.core.connection.v1\x1a\x14gogoproto/gogo.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1fibc/core/client/v1/client.proto\x1a\'ibc/core/connection/v1/connection.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/protobuf/any.proto\"/\n\x16QueryConnectionRequest\x12\x15\n\rconnection_id\x18\x01 \x01(\t\"\x9b\x01\n\x17QueryConnectionResponse\x12\x39\n\nconnection\x18\x01 \x01(\x0b\x32%.ibc.core.connection.v1.ConnectionEnd\x12\r\n\x05proof\x18\x02 \x01(\x0c\x12\x36\n\x0cproof_height\x18\x03 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00\"U\n\x17QueryConnectionsRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\xcc\x01\n\x18QueryConnectionsResponse\x12\x41\n\x0b\x63onnections\x18\x01 \x03(\x0b\x32,.ibc.core.connection.v1.IdentifiedConnection\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\x12\x30\n\x06height\x18\x03 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00\"2\n\x1dQueryClientConnectionsRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\"\x81\x01\n\x1eQueryClientConnectionsResponse\x12\x18\n\x10\x63onnection_paths\x18\x01 \x03(\t\x12\r\n\x05proof\x18\x02 \x01(\x0c\x12\x36\n\x0cproof_height\x18\x03 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00\":\n!QueryConnectionClientStateRequest\x12\x15\n\rconnection_id\x18\x01 \x01(\t\"\xb7\x01\n\"QueryConnectionClientStateResponse\x12J\n\x17identified_client_state\x18\x01 \x01(\x0b\x32).ibc.core.client.v1.IdentifiedClientState\x12\r\n\x05proof\x18\x02 \x01(\x0c\x12\x36\n\x0cproof_height\x18\x03 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00\"o\n$QueryConnectionConsensusStateRequest\x12\x15\n\rconnection_id\x18\x01 \x01(\t\x12\x17\n\x0frevision_number\x18\x02 \x01(\x04\x12\x17\n\x0frevision_height\x18\x03 \x01(\x04\"\xb0\x01\n%QueryConnectionConsensusStateResponse\x12-\n\x0f\x63onsensus_state\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x11\n\tclient_id\x18\x02 \x01(\t\x12\r\n\x05proof\x18\x03 \x01(\x0c\x12\x36\n\x0cproof_height\x18\x04 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00\"\x1e\n\x1cQueryConnectionParamsRequest\"O\n\x1dQueryConnectionParamsResponse\x12.\n\x06params\x18\x01 \x01(\x0b\x32\x1e.ibc.core.connection.v1.Params2\xb9\t\n\x05Query\x12\xaa\x01\n\nConnection\x12..ibc.core.connection.v1.QueryConnectionRequest\x1a/.ibc.core.connection.v1.QueryConnectionResponse\";\x82\xd3\xe4\x93\x02\x35\x12\x33/ibc/core/connection/v1/connections/{connection_id}\x12\x9d\x01\n\x0b\x43onnections\x12/.ibc.core.connection.v1.QueryConnectionsRequest\x1a\x30.ibc.core.connection.v1.QueryConnectionsResponse\"+\x82\xd3\xe4\x93\x02%\x12#/ibc/core/connection/v1/connections\x12\xc2\x01\n\x11\x43lientConnections\x12\x35.ibc.core.connection.v1.QueryClientConnectionsRequest\x1a\x36.ibc.core.connection.v1.QueryClientConnectionsResponse\">\x82\xd3\xe4\x93\x02\x38\x12\x36/ibc/core/connection/v1/client_connections/{client_id}\x12\xd8\x01\n\x15\x43onnectionClientState\x12\x39.ibc.core.connection.v1.QueryConnectionClientStateRequest\x1a:.ibc.core.connection.v1.QueryConnectionClientStateResponse\"H\x82\xd3\xe4\x93\x02\x42\x12@/ibc/core/connection/v1/connections/{connection_id}/client_state\x12\x98\x02\n\x18\x43onnectionConsensusState\x12<.ibc.core.connection.v1.QueryConnectionConsensusStateRequest\x1a=.ibc.core.connection.v1.QueryConnectionConsensusStateResponse\"\x7f\x82\xd3\xe4\x93\x02y\x12w/ibc/core/connection/v1/connections/{connection_id}/consensus_state/revision/{revision_number}/height/{revision_height}\x12\xa7\x01\n\x10\x43onnectionParams\x12\x34.ibc.core.connection.v1.QueryConnectionParamsRequest\x1a\x35.ibc.core.connection.v1.QueryConnectionParamsResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/ibc/core/connection/v1/paramsB>Z<github.com/cosmos/ibc-go/v8/modules/core/03-connection/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.core.connection.v1.query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z<github.com/cosmos/ibc-go/v8/modules/core/03-connection/types'
  _globals['_QUERYCONNECTIONRESPONSE'].fields_by_name['proof_height']._loaded_options = None
  _globals['_QUERYCONNECTIONRESPONSE'].fields_by_name['proof_height']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYCONNECTIONSRESPONSE'].fields_by_name['height']._loaded_options = None
  _globals['_QUERYCONNECTIONSRESPONSE'].fields_by_name['height']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYCLIENTCONNECTIONSRESPONSE'].fields_by_name['proof_height']._loaded_options = None
  _globals['_QUERYCLIENTCONNECTIONSRESPONSE'].fields_by_name['proof_height']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYCONNECTIONCLIENTSTATERESPONSE'].fields_by_name['proof_height']._loaded_options = None
  _globals['_QUERYCONNECTIONCLIENTSTATERESPONSE'].fields_by_name['proof_height']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYCONNECTIONCONSENSUSSTATERESPONSE'].fields_by_name['proof_height']._loaded_options = None
  _globals['_QUERYCONNECTIONCONSENSUSSTATERESPONSE'].fields_by_name['proof_height']._serialized_options = b'\310\336\037\000'
  _globals['_QUERY'].methods_by_name['Connection']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Connection']._serialized_options = b'\202\323\344\223\0025\0223/ibc/core/connection/v1/connections/{connection_id}'
  _globals['_QUERY'].methods_by_name['Connections']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Connections']._serialized_options = b'\202\323\344\223\002%\022#/ibc/core/connection/v1/connections'
  _globals['_QUERY'].methods_by_name['ClientConnections']._loaded_options = None
  _globals['_QUERY'].methods_by_name['ClientConnections']._serialized_options = b'\202\323\344\223\0028\0226/ibc/core/connection/v1/client_connections/{client_id}'
  _globals['_QUERY'].methods_by_name['ConnectionClientState']._loaded_options = None
  _globals['_QUERY'].methods_by_name['ConnectionClientState']._serialized_options = b'\202\323\344\223\002B\022@/ibc/core/connection/v1/connections/{connection_id}/client_state'
  _globals['_QUERY'].methods_by_name['ConnectionConsensusState']._loaded_options = None
  _globals['_QUERY'].methods_by_name['ConnectionConsensusState']._serialized_options = b'\202\323\344\223\002y\022w/ibc/core/connection/v1/connections/{connection_id}/consensus_state/revision/{revision_number}/height/{revision_height}'
  _globals['_QUERY'].methods_by_name['ConnectionParams']._loaded_options = None
  _globals['_QUERY'].methods_by_name['ConnectionParams']._serialized_options = b'\202\323\344\223\002 \022\036/ibc/core/connection/v1/params'
  _globals['_QUERYCONNECTIONREQUEST']._serialized_start=259
  _globals['_QUERYCONNECTIONREQUEST']._serialized_end=306
  _globals['_QUERYCONNECTIONRESPONSE']._serialized_start=309
  _globals['_QUERYCONNECTIONRESPONSE']._serialized_end=464
  _globals['_QUERYCONNECTIONSREQUEST']._serialized_start=466
  _globals['_QUERYCONNECTIONSREQUEST']._serialized_end=551
  _globals['_QUERYCONNECTIONSRESPONSE']._serialized_start=554
  _globals['_QUERYCONNECTIONSRESPONSE']._serialized_end=758
  _globals['_QUERYCLIENTCONNECTIONSREQUEST']._serialized_start=760
  _globals['_QUERYCLIENTCONNECTIONSREQUEST']._serialized_end=810
  _globals['_QUERYCLIENTCONNECTIONSRESPONSE']._serialized_start=813
  _globals['_QUERYCLIENTCONNECTIONSRESPONSE']._serialized_end=942
  _globals['_QUERYCONNECTIONCLIENTSTATEREQUEST']._serialized_start=944
  _globals['_QUERYCONNECTIONCLIENTSTATEREQUEST']._serialized_end=1002
  _globals['_QUERYCONNECTIONCLIENTSTATERESPONSE']._serialized_start=1005
  _globals['_QUERYCONNECTIONCLIENTSTATERESPONSE']._serialized_end=1188
  _globals['_QUERYCONNECTIONCONSENSUSSTATEREQUEST']._serialized_start=1190
  _globals['_QUERYCONNECTIONCONSENSUSSTATEREQUEST']._serialized_end=1301
  _globals['_QUERYCONNECTIONCONSENSUSSTATERESPONSE']._serialized_start=1304
  _globals['_QUERYCONNECTIONCONSENSUSSTATERESPONSE']._serialized_end=1480
  _globals['_QUERYCONNECTIONPARAMSREQUEST']._serialized_start=1482
  _globals['_QUERYCONNECTIONPARAMSREQUEST']._serialized_end=1512
  _globals['_QUERYCONNECTIONPARAMSRESPONSE']._serialized_start=1514
  _globals['_QUERYCONNECTIONPARAMSRESPONSE']._serialized_end=1593
  _globals['_QUERY']._serialized_start=1596
  _globals['_QUERY']._serialized_end=2805
# @@protoc_insertion_point(module_scope)
