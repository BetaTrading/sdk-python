# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/auction/v1beta1/query.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from pyinjective.proto.injective.auction.v1beta1 import (
    auction_pb2 as injective_dot_auction_dot_v1beta1_dot_auction__pb2,
)
from pyinjective.proto.injective.auction.v1beta1 import (
    genesis_pb2 as injective_dot_auction_dot_v1beta1_dot_genesis__pb2,
)
from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n%injective/auction/v1beta1/query.proto\x12\x19injective.auction.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\'injective/auction/v1beta1/auction.proto\x1a\'injective/auction/v1beta1/genesis.proto\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto"\x1b\n\x19QueryAuctionParamsRequest"]\n\x1aQueryAuctionParamsResponse\x12?\n\x06params\x18\x01 \x01(\x0b\x32!.injective.auction.v1beta1.ParamsB\x04\xc8\xde\x1f\x00R\x06params""\n QueryCurrentAuctionBasketRequest"\xcd\x02\n!QueryCurrentAuctionBasketResponse\x12\x63\n\x06\x61mount\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.CoinsR\x06\x61mount\x12"\n\x0c\x61uctionRound\x18\x02 \x01(\x04R\x0c\x61uctionRound\x12.\n\x12\x61uctionClosingTime\x18\x03 \x01(\x03R\x12\x61uctionClosingTime\x12$\n\rhighestBidder\x18\x04 \x01(\tR\rhighestBidder\x12I\n\x10highestBidAmount\x18\x05 \x01(\tB\x1d\xc8\xde\x1f\x00\xda\xde\x1f\x15\x63osmossdk.io/math.IntR\x10highestBidAmount"\x19\n\x17QueryModuleStateRequest"Y\n\x18QueryModuleStateResponse\x12=\n\x05state\x18\x01 \x01(\x0b\x32\'.injective.auction.v1beta1.GenesisStateR\x05state"\x1f\n\x1dQueryLastAuctionResultRequest"~\n\x1eQueryLastAuctionResultResponse\x12\\\n\x13last_auction_result\x18\x01 \x01(\x0b\x32,.injective.auction.v1beta1.LastAuctionResultR\x11lastAuctionResult2\xe4\x05\n\x05Query\x12\xa7\x01\n\rAuctionParams\x12\x34.injective.auction.v1beta1.QueryAuctionParamsRequest\x1a\x35.injective.auction.v1beta1.QueryAuctionParamsResponse")\x82\xd3\xe4\x93\x02#\x12!/injective/auction/v1beta1/params\x12\xbc\x01\n\x14\x43urrentAuctionBasket\x12;.injective.auction.v1beta1.QueryCurrentAuctionBasketRequest\x1a<.injective.auction.v1beta1.QueryCurrentAuctionBasketResponse")\x82\xd3\xe4\x93\x02#\x12!/injective/auction/v1beta1/basket\x12\xae\x01\n\x12\x41uctionModuleState\x12\x32.injective.auction.v1beta1.QueryModuleStateRequest\x1a\x33.injective.auction.v1beta1.QueryModuleStateResponse"/\x82\xd3\xe4\x93\x02)\x12\'/injective/auction/v1beta1/module_state\x12\xc0\x01\n\x11LastAuctionResult\x12\x38.injective.auction.v1beta1.QueryLastAuctionResultRequest\x1a\x39.injective.auction.v1beta1.QueryLastAuctionResultResponse"6\x82\xd3\xe4\x93\x02\x30\x12./injective/auction/v1beta1/last_auction_resultB\x80\x02\n\x1d\x63om.injective.auction.v1beta1B\nQueryProtoP\x01ZMgithub.com/InjectiveLabs/injective-core/injective-chain/modules/auction/types\xa2\x02\x03IAX\xaa\x02\x19Injective.Auction.V1beta1\xca\x02\x19Injective\\Auction\\V1beta1\xe2\x02%Injective\\Auction\\V1beta1\\GPBMetadata\xea\x02\x1bInjective::Auction::V1beta1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "injective.auction.v1beta1.query_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals["DESCRIPTOR"]._serialized_options = (
        b"\n\035com.injective.auction.v1beta1B\nQueryProtoP\001ZMgithub.com/InjectiveLabs/injective-core/injective-chain/modules/auction/types\242\002\003IAX\252\002\031Injective.Auction.V1beta1\312\002\031Injective\\Auction\\V1beta1\342\002%Injective\\Auction\\V1beta1\\GPBMetadata\352\002\033Injective::Auction::V1beta1"
    )
    _globals["_QUERYAUCTIONPARAMSRESPONSE"].fields_by_name["params"]._loaded_options = None
    _globals["_QUERYAUCTIONPARAMSRESPONSE"].fields_by_name["params"]._serialized_options = b"\310\336\037\000"
    _globals["_QUERYCURRENTAUCTIONBASKETRESPONSE"].fields_by_name["amount"]._loaded_options = None
    _globals["_QUERYCURRENTAUCTIONBASKETRESPONSE"].fields_by_name[
        "amount"
    ]._serialized_options = b"\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins"
    _globals["_QUERYCURRENTAUCTIONBASKETRESPONSE"].fields_by_name["highestBidAmount"]._loaded_options = None
    _globals["_QUERYCURRENTAUCTIONBASKETRESPONSE"].fields_by_name[
        "highestBidAmount"
    ]._serialized_options = b"\310\336\037\000\332\336\037\025cosmossdk.io/math.Int"
    _globals["_QUERY"].methods_by_name["AuctionParams"]._loaded_options = None
    _globals["_QUERY"].methods_by_name[
        "AuctionParams"
    ]._serialized_options = b"\202\323\344\223\002#\022!/injective/auction/v1beta1/params"
    _globals["_QUERY"].methods_by_name["CurrentAuctionBasket"]._loaded_options = None
    _globals["_QUERY"].methods_by_name[
        "CurrentAuctionBasket"
    ]._serialized_options = b"\202\323\344\223\002#\022!/injective/auction/v1beta1/basket"
    _globals["_QUERY"].methods_by_name["AuctionModuleState"]._loaded_options = None
    _globals["_QUERY"].methods_by_name[
        "AuctionModuleState"
    ]._serialized_options = b"\202\323\344\223\002)\022'/injective/auction/v1beta1/module_state"
    _globals["_QUERY"].methods_by_name["LastAuctionResult"]._loaded_options = None
    _globals["_QUERY"].methods_by_name[
        "LastAuctionResult"
    ]._serialized_options = b"\202\323\344\223\0020\022./injective/auction/v1beta1/last_auction_result"
    _globals["_QUERYAUCTIONPARAMSREQUEST"]._serialized_start = 234
    _globals["_QUERYAUCTIONPARAMSREQUEST"]._serialized_end = 261
    _globals["_QUERYAUCTIONPARAMSRESPONSE"]._serialized_start = 263
    _globals["_QUERYAUCTIONPARAMSRESPONSE"]._serialized_end = 356
    _globals["_QUERYCURRENTAUCTIONBASKETREQUEST"]._serialized_start = 358
    _globals["_QUERYCURRENTAUCTIONBASKETREQUEST"]._serialized_end = 392
    _globals["_QUERYCURRENTAUCTIONBASKETRESPONSE"]._serialized_start = 395
    _globals["_QUERYCURRENTAUCTIONBASKETRESPONSE"]._serialized_end = 728
    _globals["_QUERYMODULESTATEREQUEST"]._serialized_start = 730
    _globals["_QUERYMODULESTATEREQUEST"]._serialized_end = 755
    _globals["_QUERYMODULESTATERESPONSE"]._serialized_start = 757
    _globals["_QUERYMODULESTATERESPONSE"]._serialized_end = 846
    _globals["_QUERYLASTAUCTIONRESULTREQUEST"]._serialized_start = 848
    _globals["_QUERYLASTAUCTIONRESULTREQUEST"]._serialized_end = 879
    _globals["_QUERYLASTAUCTIONRESULTRESPONSE"]._serialized_start = 881
    _globals["_QUERYLASTAUCTIONRESULTRESPONSE"]._serialized_end = 1007
    _globals["_QUERY"]._serialized_start = 1010
    _globals["_QUERY"]._serialized_end = 1750
# @@protoc_insertion_point(module_scope)
