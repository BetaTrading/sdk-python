# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/tx/v1beta1/service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from pyinjective.proto.cosmos.base.abci.v1beta1 import abci_pb2 as cosmos_dot_base_dot_abci_dot_v1beta1_dot_abci__pb2
from pyinjective.proto.cosmos.tx.v1beta1 import tx_pb2 as cosmos_dot_tx_dot_v1beta1_dot_tx__pb2
from pyinjective.proto.cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from pyinjective.proto.tendermint.types import block_pb2 as tendermint_dot_types_dot_block__pb2
from pyinjective.proto.tendermint.types import types_pb2 as tendermint_dot_types_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x63osmos/tx/v1beta1/service.proto\x12\x11\x63osmos.tx.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a#cosmos/base/abci/v1beta1/abci.proto\x1a\x1a\x63osmos/tx/v1beta1/tx.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1ctendermint/types/block.proto\x1a\x1ctendermint/types/types.proto\"\xc2\x01\n\x12GetTxsEventRequest\x12\x12\n\x06\x65vents\x18\x01 \x03(\tB\x02\x18\x01\x12>\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestB\x02\x18\x01\x12,\n\x08order_by\x18\x03 \x01(\x0e\x32\x1a.cosmos.tx.v1beta1.OrderBy\x12\x0c\n\x04page\x18\x04 \x01(\x04\x12\r\n\x05limit\x18\x05 \x01(\x04\x12\r\n\x05query\x18\x06 \x01(\t\"\xc5\x01\n\x13GetTxsEventResponse\x12\"\n\x03txs\x18\x01 \x03(\x0b\x32\x15.cosmos.tx.v1beta1.Tx\x12:\n\x0ctx_responses\x18\x02 \x03(\x0b\x32$.cosmos.base.abci.v1beta1.TxResponse\x12?\n\npagination\x18\x03 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseB\x02\x18\x01\x12\r\n\x05total\x18\x04 \x01(\x04\"V\n\x12\x42roadcastTxRequest\x12\x10\n\x08tx_bytes\x18\x01 \x01(\x0c\x12.\n\x04mode\x18\x02 \x01(\x0e\x32 .cosmos.tx.v1beta1.BroadcastMode\"P\n\x13\x42roadcastTxResponse\x12\x39\n\x0btx_response\x18\x01 \x01(\x0b\x32$.cosmos.base.abci.v1beta1.TxResponse\"J\n\x0fSimulateRequest\x12%\n\x02tx\x18\x01 \x01(\x0b\x32\x15.cosmos.tx.v1beta1.TxB\x02\x18\x01\x12\x10\n\x08tx_bytes\x18\x02 \x01(\x0c\"y\n\x10SimulateResponse\x12\x33\n\x08gas_info\x18\x01 \x01(\x0b\x32!.cosmos.base.abci.v1beta1.GasInfo\x12\x30\n\x06result\x18\x02 \x01(\x0b\x32 .cosmos.base.abci.v1beta1.Result\"\x1c\n\x0cGetTxRequest\x12\x0c\n\x04hash\x18\x01 \x01(\t\"m\n\rGetTxResponse\x12!\n\x02tx\x18\x01 \x01(\x0b\x32\x15.cosmos.tx.v1beta1.Tx\x12\x39\n\x0btx_response\x18\x02 \x01(\x0b\x32$.cosmos.base.abci.v1beta1.TxResponse\"d\n\x16GetBlockWithTxsRequest\x12\x0e\n\x06height\x18\x01 \x01(\x03\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\xcf\x01\n\x17GetBlockWithTxsResponse\x12\"\n\x03txs\x18\x01 \x03(\x0b\x32\x15.cosmos.tx.v1beta1.Tx\x12+\n\x08\x62lock_id\x18\x02 \x01(\x0b\x32\x19.tendermint.types.BlockID\x12&\n\x05\x62lock\x18\x03 \x01(\x0b\x32\x17.tendermint.types.Block\x12;\n\npagination\x18\x04 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"#\n\x0fTxDecodeRequest\x12\x10\n\x08tx_bytes\x18\x01 \x01(\x0c\"5\n\x10TxDecodeResponse\x12!\n\x02tx\x18\x01 \x01(\x0b\x32\x15.cosmos.tx.v1beta1.Tx\"4\n\x0fTxEncodeRequest\x12!\n\x02tx\x18\x01 \x01(\x0b\x32\x15.cosmos.tx.v1beta1.Tx\"$\n\x10TxEncodeResponse\x12\x10\n\x08tx_bytes\x18\x01 \x01(\x0c\"*\n\x14TxEncodeAminoRequest\x12\x12\n\namino_json\x18\x01 \x01(\t\"-\n\x15TxEncodeAminoResponse\x12\x14\n\x0c\x61mino_binary\x18\x01 \x01(\x0c\",\n\x14TxDecodeAminoRequest\x12\x14\n\x0c\x61mino_binary\x18\x01 \x01(\x0c\"+\n\x15TxDecodeAminoResponse\x12\x12\n\namino_json\x18\x01 \x01(\t*H\n\x07OrderBy\x12\x18\n\x14ORDER_BY_UNSPECIFIED\x10\x00\x12\x10\n\x0cORDER_BY_ASC\x10\x01\x12\x11\n\rORDER_BY_DESC\x10\x02*\x80\x01\n\rBroadcastMode\x12\x1e\n\x1a\x42ROADCAST_MODE_UNSPECIFIED\x10\x00\x12\x1c\n\x14\x42ROADCAST_MODE_BLOCK\x10\x01\x1a\x02\x08\x01\x12\x17\n\x13\x42ROADCAST_MODE_SYNC\x10\x02\x12\x18\n\x14\x42ROADCAST_MODE_ASYNC\x10\x03\x32\xaa\t\n\x07Service\x12{\n\x08Simulate\x12\".cosmos.tx.v1beta1.SimulateRequest\x1a#.cosmos.tx.v1beta1.SimulateResponse\"&\x82\xd3\xe4\x93\x02 \"\x1b/cosmos/tx/v1beta1/simulate:\x01*\x12q\n\x05GetTx\x12\x1f.cosmos.tx.v1beta1.GetTxRequest\x1a .cosmos.tx.v1beta1.GetTxResponse\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/cosmos/tx/v1beta1/txs/{hash}\x12\x7f\n\x0b\x42roadcastTx\x12%.cosmos.tx.v1beta1.BroadcastTxRequest\x1a&.cosmos.tx.v1beta1.BroadcastTxResponse\"!\x82\xd3\xe4\x93\x02\x1b\"\x16/cosmos/tx/v1beta1/txs:\x01*\x12|\n\x0bGetTxsEvent\x12%.cosmos.tx.v1beta1.GetTxsEventRequest\x1a&.cosmos.tx.v1beta1.GetTxsEventResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/cosmos/tx/v1beta1/txs\x12\x97\x01\n\x0fGetBlockWithTxs\x12).cosmos.tx.v1beta1.GetBlockWithTxsRequest\x1a*.cosmos.tx.v1beta1.GetBlockWithTxsResponse\"-\x82\xd3\xe4\x93\x02\'\x12%/cosmos/tx/v1beta1/txs/block/{height}\x12y\n\x08TxDecode\x12\".cosmos.tx.v1beta1.TxDecodeRequest\x1a#.cosmos.tx.v1beta1.TxDecodeResponse\"$\x82\xd3\xe4\x93\x02\x1e\"\x19/cosmos/tx/v1beta1/decode:\x01*\x12y\n\x08TxEncode\x12\".cosmos.tx.v1beta1.TxEncodeRequest\x1a#.cosmos.tx.v1beta1.TxEncodeResponse\"$\x82\xd3\xe4\x93\x02\x1e\"\x19/cosmos/tx/v1beta1/encode:\x01*\x12\x8e\x01\n\rTxEncodeAmino\x12\'.cosmos.tx.v1beta1.TxEncodeAminoRequest\x1a(.cosmos.tx.v1beta1.TxEncodeAminoResponse\"*\x82\xd3\xe4\x93\x02$\"\x1f/cosmos/tx/v1beta1/encode/amino:\x01*\x12\x8e\x01\n\rTxDecodeAmino\x12\'.cosmos.tx.v1beta1.TxDecodeAminoRequest\x1a(.cosmos.tx.v1beta1.TxDecodeAminoResponse\"*\x82\xd3\xe4\x93\x02$\"\x1f/cosmos/tx/v1beta1/decode/amino:\x01*B\'Z%github.com/cosmos/cosmos-sdk/types/txb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.tx.v1beta1.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z%github.com/cosmos/cosmos-sdk/types/tx'
  _globals['_BROADCASTMODE'].values_by_name["BROADCAST_MODE_BLOCK"]._loaded_options = None
  _globals['_BROADCASTMODE'].values_by_name["BROADCAST_MODE_BLOCK"]._serialized_options = b'\010\001'
  _globals['_GETTXSEVENTREQUEST'].fields_by_name['events']._loaded_options = None
  _globals['_GETTXSEVENTREQUEST'].fields_by_name['events']._serialized_options = b'\030\001'
  _globals['_GETTXSEVENTREQUEST'].fields_by_name['pagination']._loaded_options = None
  _globals['_GETTXSEVENTREQUEST'].fields_by_name['pagination']._serialized_options = b'\030\001'
  _globals['_GETTXSEVENTRESPONSE'].fields_by_name['pagination']._loaded_options = None
  _globals['_GETTXSEVENTRESPONSE'].fields_by_name['pagination']._serialized_options = b'\030\001'
  _globals['_SIMULATEREQUEST'].fields_by_name['tx']._loaded_options = None
  _globals['_SIMULATEREQUEST'].fields_by_name['tx']._serialized_options = b'\030\001'
  _globals['_SERVICE'].methods_by_name['Simulate']._loaded_options = None
  _globals['_SERVICE'].methods_by_name['Simulate']._serialized_options = b'\202\323\344\223\002 \"\033/cosmos/tx/v1beta1/simulate:\001*'
  _globals['_SERVICE'].methods_by_name['GetTx']._loaded_options = None
  _globals['_SERVICE'].methods_by_name['GetTx']._serialized_options = b'\202\323\344\223\002\037\022\035/cosmos/tx/v1beta1/txs/{hash}'
  _globals['_SERVICE'].methods_by_name['BroadcastTx']._loaded_options = None
  _globals['_SERVICE'].methods_by_name['BroadcastTx']._serialized_options = b'\202\323\344\223\002\033\"\026/cosmos/tx/v1beta1/txs:\001*'
  _globals['_SERVICE'].methods_by_name['GetTxsEvent']._loaded_options = None
  _globals['_SERVICE'].methods_by_name['GetTxsEvent']._serialized_options = b'\202\323\344\223\002\030\022\026/cosmos/tx/v1beta1/txs'
  _globals['_SERVICE'].methods_by_name['GetBlockWithTxs']._loaded_options = None
  _globals['_SERVICE'].methods_by_name['GetBlockWithTxs']._serialized_options = b'\202\323\344\223\002\'\022%/cosmos/tx/v1beta1/txs/block/{height}'
  _globals['_SERVICE'].methods_by_name['TxDecode']._loaded_options = None
  _globals['_SERVICE'].methods_by_name['TxDecode']._serialized_options = b'\202\323\344\223\002\036\"\031/cosmos/tx/v1beta1/decode:\001*'
  _globals['_SERVICE'].methods_by_name['TxEncode']._loaded_options = None
  _globals['_SERVICE'].methods_by_name['TxEncode']._serialized_options = b'\202\323\344\223\002\036\"\031/cosmos/tx/v1beta1/encode:\001*'
  _globals['_SERVICE'].methods_by_name['TxEncodeAmino']._loaded_options = None
  _globals['_SERVICE'].methods_by_name['TxEncodeAmino']._serialized_options = b'\202\323\344\223\002$\"\037/cosmos/tx/v1beta1/encode/amino:\001*'
  _globals['_SERVICE'].methods_by_name['TxDecodeAmino']._loaded_options = None
  _globals['_SERVICE'].methods_by_name['TxDecodeAmino']._serialized_options = b'\202\323\344\223\002$\"\037/cosmos/tx/v1beta1/decode/amino:\001*'
  _globals['_ORDERBY']._serialized_start=1838
  _globals['_ORDERBY']._serialized_end=1910
  _globals['_BROADCASTMODE']._serialized_start=1913
  _globals['_BROADCASTMODE']._serialized_end=2041
  _globals['_GETTXSEVENTREQUEST']._serialized_start=254
  _globals['_GETTXSEVENTREQUEST']._serialized_end=448
  _globals['_GETTXSEVENTRESPONSE']._serialized_start=451
  _globals['_GETTXSEVENTRESPONSE']._serialized_end=648
  _globals['_BROADCASTTXREQUEST']._serialized_start=650
  _globals['_BROADCASTTXREQUEST']._serialized_end=736
  _globals['_BROADCASTTXRESPONSE']._serialized_start=738
  _globals['_BROADCASTTXRESPONSE']._serialized_end=818
  _globals['_SIMULATEREQUEST']._serialized_start=820
  _globals['_SIMULATEREQUEST']._serialized_end=894
  _globals['_SIMULATERESPONSE']._serialized_start=896
  _globals['_SIMULATERESPONSE']._serialized_end=1017
  _globals['_GETTXREQUEST']._serialized_start=1019
  _globals['_GETTXREQUEST']._serialized_end=1047
  _globals['_GETTXRESPONSE']._serialized_start=1049
  _globals['_GETTXRESPONSE']._serialized_end=1158
  _globals['_GETBLOCKWITHTXSREQUEST']._serialized_start=1160
  _globals['_GETBLOCKWITHTXSREQUEST']._serialized_end=1260
  _globals['_GETBLOCKWITHTXSRESPONSE']._serialized_start=1263
  _globals['_GETBLOCKWITHTXSRESPONSE']._serialized_end=1470
  _globals['_TXDECODEREQUEST']._serialized_start=1472
  _globals['_TXDECODEREQUEST']._serialized_end=1507
  _globals['_TXDECODERESPONSE']._serialized_start=1509
  _globals['_TXDECODERESPONSE']._serialized_end=1562
  _globals['_TXENCODEREQUEST']._serialized_start=1564
  _globals['_TXENCODEREQUEST']._serialized_end=1616
  _globals['_TXENCODERESPONSE']._serialized_start=1618
  _globals['_TXENCODERESPONSE']._serialized_end=1654
  _globals['_TXENCODEAMINOREQUEST']._serialized_start=1656
  _globals['_TXENCODEAMINOREQUEST']._serialized_end=1698
  _globals['_TXENCODEAMINORESPONSE']._serialized_start=1700
  _globals['_TXENCODEAMINORESPONSE']._serialized_end=1745
  _globals['_TXDECODEAMINOREQUEST']._serialized_start=1747
  _globals['_TXDECODEAMINOREQUEST']._serialized_end=1791
  _globals['_TXDECODEAMINORESPONSE']._serialized_start=1793
  _globals['_TXDECODEAMINORESPONSE']._serialized_end=1836
  _globals['_SERVICE']._serialized_start=2044
  _globals['_SERVICE']._serialized_end=3238
# @@protoc_insertion_point(module_scope)
