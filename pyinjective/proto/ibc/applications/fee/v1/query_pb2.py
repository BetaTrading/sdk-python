# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/applications/fee/v1/query.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from pyinjective.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from pyinjective.proto.cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from pyinjective.proto.ibc.applications.fee.v1 import fee_pb2 as ibc_dot_applications_dot_fee_dot_v1_dot_fee__pb2
from pyinjective.proto.ibc.applications.fee.v1 import genesis_pb2 as ibc_dot_applications_dot_fee_dot_v1_dot_genesis__pb2
from pyinjective.proto.ibc.core.channel.v1 import channel_pb2 as ibc_dot_core_dot_channel_dot_v1_dot_channel__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#ibc/applications/fee/v1/query.proto\x12\x17ibc.applications.fee.v1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a!ibc/applications/fee/v1/fee.proto\x1a%ibc/applications/fee/v1/genesis.proto\x1a!ibc/core/channel/v1/channel.proto\"s\n\x1fQueryIncentivizedPacketsRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\x12\x14\n\x0cquery_height\x18\x02 \x01(\x04\"\xb2\x01\n QueryIncentivizedPacketsResponse\x12Q\n\x14incentivized_packets\x18\x01 \x03(\x0b\x32-.ibc.applications.fee.v1.IdentifiedPacketFeesB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"n\n\x1eQueryIncentivizedPacketRequest\x12\x36\n\tpacket_id\x18\x01 \x01(\x0b\x32\x1d.ibc.core.channel.v1.PacketIdB\x04\xc8\xde\x1f\x00\x12\x14\n\x0cquery_height\x18\x02 \x01(\x04\"s\n\x1fQueryIncentivizedPacketResponse\x12P\n\x13incentivized_packet\x18\x01 \x01(\x0b\x32-.ibc.applications.fee.v1.IdentifiedPacketFeesB\x04\xc8\xde\x1f\x00\"\xa2\x01\n)QueryIncentivizedPacketsForChannelRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\x12\x0f\n\x07port_id\x18\x02 \x01(\t\x12\x12\n\nchannel_id\x18\x03 \x01(\t\x12\x14\n\x0cquery_height\x18\x04 \x01(\x04\"\xb6\x01\n*QueryIncentivizedPacketsForChannelResponse\x12K\n\x14incentivized_packets\x18\x01 \x03(\x0b\x32-.ibc.applications.fee.v1.IdentifiedPacketFees\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"S\n\x19QueryTotalRecvFeesRequest\x12\x36\n\tpacket_id\x18\x01 \x01(\x0b\x32\x1d.ibc.core.channel.v1.PacketIdB\x04\xc8\xde\x1f\x00\"|\n\x1aQueryTotalRecvFeesResponse\x12^\n\trecv_fees\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\"R\n\x18QueryTotalAckFeesRequest\x12\x36\n\tpacket_id\x18\x01 \x01(\x0b\x32\x1d.ibc.core.channel.v1.PacketIdB\x04\xc8\xde\x1f\x00\"z\n\x19QueryTotalAckFeesResponse\x12]\n\x08\x61\x63k_fees\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\"V\n\x1cQueryTotalTimeoutFeesRequest\x12\x36\n\tpacket_id\x18\x01 \x01(\x0b\x32\x1d.ibc.core.channel.v1.PacketIdB\x04\xc8\xde\x1f\x00\"\x82\x01\n\x1dQueryTotalTimeoutFeesResponse\x12\x61\n\x0ctimeout_fees\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\"8\n\x11QueryPayeeRequest\x12\x12\n\nchannel_id\x18\x01 \x01(\t\x12\x0f\n\x07relayer\x18\x02 \x01(\t\"+\n\x12QueryPayeeResponse\x12\x15\n\rpayee_address\x18\x01 \x01(\t\"D\n\x1dQueryCounterpartyPayeeRequest\x12\x12\n\nchannel_id\x18\x01 \x01(\t\x12\x0f\n\x07relayer\x18\x02 \x01(\t\"<\n\x1eQueryCounterpartyPayeeResponse\x12\x1a\n\x12\x63ounterparty_payee\x18\x01 \x01(\t\"r\n\x1eQueryFeeEnabledChannelsRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\x12\x14\n\x0cquery_height\x18\x02 \x01(\x04\"\xae\x01\n\x1fQueryFeeEnabledChannelsResponse\x12N\n\x14\x66\x65\x65_enabled_channels\x18\x01 \x03(\x0b\x32*.ibc.applications.fee.v1.FeeEnabledChannelB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"D\n\x1dQueryFeeEnabledChannelRequest\x12\x0f\n\x07port_id\x18\x01 \x01(\t\x12\x12\n\nchannel_id\x18\x02 \x01(\t\"5\n\x1eQueryFeeEnabledChannelResponse\x12\x13\n\x0b\x66\x65\x65_enabled\x18\x01 \x01(\x08\x32\xe6\x11\n\x05Query\x12\xb9\x01\n\x13IncentivizedPackets\x12\x38.ibc.applications.fee.v1.QueryIncentivizedPacketsRequest\x1a\x39.ibc.applications.fee.v1.QueryIncentivizedPacketsResponse\"-\x82\xd3\xe4\x93\x02\'\x12%/ibc/apps/fee/v1/incentivized_packets\x12\x8f\x02\n\x12IncentivizedPacket\x12\x37.ibc.applications.fee.v1.QueryIncentivizedPacketRequest\x1a\x38.ibc.applications.fee.v1.QueryIncentivizedPacketResponse\"\x85\x01\x82\xd3\xe4\x93\x02\x7f\x12}/ibc/apps/fee/v1/channels/{packet_id.channel_id}/ports/{packet_id.port_id}/sequences/{packet_id.sequence}/incentivized_packet\x12\xfd\x01\n\x1dIncentivizedPacketsForChannel\x12\x42.ibc.applications.fee.v1.QueryIncentivizedPacketsForChannelRequest\x1a\x43.ibc.applications.fee.v1.QueryIncentivizedPacketsForChannelResponse\"S\x82\xd3\xe4\x93\x02M\x12K/ibc/apps/fee/v1/channels/{channel_id}/ports/{port_id}/incentivized_packets\x12\xfc\x01\n\rTotalRecvFees\x12\x32.ibc.applications.fee.v1.QueryTotalRecvFeesRequest\x1a\x33.ibc.applications.fee.v1.QueryTotalRecvFeesResponse\"\x81\x01\x82\xd3\xe4\x93\x02{\x12y/ibc/apps/fee/v1/channels/{packet_id.channel_id}/ports/{packet_id.port_id}/sequences/{packet_id.sequence}/total_recv_fees\x12\xf8\x01\n\x0cTotalAckFees\x12\x31.ibc.applications.fee.v1.QueryTotalAckFeesRequest\x1a\x32.ibc.applications.fee.v1.QueryTotalAckFeesResponse\"\x80\x01\x82\xd3\xe4\x93\x02z\x12x/ibc/apps/fee/v1/channels/{packet_id.channel_id}/ports/{packet_id.port_id}/sequences/{packet_id.sequence}/total_ack_fees\x12\x88\x02\n\x10TotalTimeoutFees\x12\x35.ibc.applications.fee.v1.QueryTotalTimeoutFeesRequest\x1a\x36.ibc.applications.fee.v1.QueryTotalTimeoutFeesResponse\"\x84\x01\x82\xd3\xe4\x93\x02~\x12|/ibc/apps/fee/v1/channels/{packet_id.channel_id}/ports/{packet_id.port_id}/sequences/{packet_id.sequence}/total_timeout_fees\x12\xa9\x01\n\x05Payee\x12*.ibc.applications.fee.v1.QueryPayeeRequest\x1a+.ibc.applications.fee.v1.QueryPayeeResponse\"G\x82\xd3\xe4\x93\x02\x41\x12?/ibc/apps/fee/v1/channels/{channel_id}/relayers/{relayer}/payee\x12\xda\x01\n\x11\x43ounterpartyPayee\x12\x36.ibc.applications.fee.v1.QueryCounterpartyPayeeRequest\x1a\x37.ibc.applications.fee.v1.QueryCounterpartyPayeeResponse\"T\x82\xd3\xe4\x93\x02N\x12L/ibc/apps/fee/v1/channels/{channel_id}/relayers/{relayer}/counterparty_payee\x12\xad\x01\n\x12\x46\x65\x65\x45nabledChannels\x12\x37.ibc.applications.fee.v1.QueryFeeEnabledChannelsRequest\x1a\x38.ibc.applications.fee.v1.QueryFeeEnabledChannelsResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/ibc/apps/fee/v1/fee_enabled\x12\xd0\x01\n\x11\x46\x65\x65\x45nabledChannel\x12\x36.ibc.applications.fee.v1.QueryFeeEnabledChannelRequest\x1a\x37.ibc.applications.fee.v1.QueryFeeEnabledChannelResponse\"J\x82\xd3\xe4\x93\x02\x44\x12\x42/ibc/apps/fee/v1/channels/{channel_id}/ports/{port_id}/fee_enabledB7Z5github.com/cosmos/ibc-go/v8/modules/apps/29-fee/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.applications.fee.v1.query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z5github.com/cosmos/ibc-go/v8/modules/apps/29-fee/types'
  _globals['_QUERYINCENTIVIZEDPACKETSRESPONSE'].fields_by_name['incentivized_packets']._loaded_options = None
  _globals['_QUERYINCENTIVIZEDPACKETSRESPONSE'].fields_by_name['incentivized_packets']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYINCENTIVIZEDPACKETREQUEST'].fields_by_name['packet_id']._loaded_options = None
  _globals['_QUERYINCENTIVIZEDPACKETREQUEST'].fields_by_name['packet_id']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYINCENTIVIZEDPACKETRESPONSE'].fields_by_name['incentivized_packet']._loaded_options = None
  _globals['_QUERYINCENTIVIZEDPACKETRESPONSE'].fields_by_name['incentivized_packet']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYTOTALRECVFEESREQUEST'].fields_by_name['packet_id']._loaded_options = None
  _globals['_QUERYTOTALRECVFEESREQUEST'].fields_by_name['packet_id']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYTOTALRECVFEESRESPONSE'].fields_by_name['recv_fees']._loaded_options = None
  _globals['_QUERYTOTALRECVFEESRESPONSE'].fields_by_name['recv_fees']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _globals['_QUERYTOTALACKFEESREQUEST'].fields_by_name['packet_id']._loaded_options = None
  _globals['_QUERYTOTALACKFEESREQUEST'].fields_by_name['packet_id']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYTOTALACKFEESRESPONSE'].fields_by_name['ack_fees']._loaded_options = None
  _globals['_QUERYTOTALACKFEESRESPONSE'].fields_by_name['ack_fees']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _globals['_QUERYTOTALTIMEOUTFEESREQUEST'].fields_by_name['packet_id']._loaded_options = None
  _globals['_QUERYTOTALTIMEOUTFEESREQUEST'].fields_by_name['packet_id']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYTOTALTIMEOUTFEESRESPONSE'].fields_by_name['timeout_fees']._loaded_options = None
  _globals['_QUERYTOTALTIMEOUTFEESRESPONSE'].fields_by_name['timeout_fees']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _globals['_QUERYFEEENABLEDCHANNELSRESPONSE'].fields_by_name['fee_enabled_channels']._loaded_options = None
  _globals['_QUERYFEEENABLEDCHANNELSRESPONSE'].fields_by_name['fee_enabled_channels']._serialized_options = b'\310\336\037\000'
  _globals['_QUERY'].methods_by_name['IncentivizedPackets']._loaded_options = None
  _globals['_QUERY'].methods_by_name['IncentivizedPackets']._serialized_options = b'\202\323\344\223\002\'\022%/ibc/apps/fee/v1/incentivized_packets'
  _globals['_QUERY'].methods_by_name['IncentivizedPacket']._loaded_options = None
  _globals['_QUERY'].methods_by_name['IncentivizedPacket']._serialized_options = b'\202\323\344\223\002\177\022}/ibc/apps/fee/v1/channels/{packet_id.channel_id}/ports/{packet_id.port_id}/sequences/{packet_id.sequence}/incentivized_packet'
  _globals['_QUERY'].methods_by_name['IncentivizedPacketsForChannel']._loaded_options = None
  _globals['_QUERY'].methods_by_name['IncentivizedPacketsForChannel']._serialized_options = b'\202\323\344\223\002M\022K/ibc/apps/fee/v1/channels/{channel_id}/ports/{port_id}/incentivized_packets'
  _globals['_QUERY'].methods_by_name['TotalRecvFees']._loaded_options = None
  _globals['_QUERY'].methods_by_name['TotalRecvFees']._serialized_options = b'\202\323\344\223\002{\022y/ibc/apps/fee/v1/channels/{packet_id.channel_id}/ports/{packet_id.port_id}/sequences/{packet_id.sequence}/total_recv_fees'
  _globals['_QUERY'].methods_by_name['TotalAckFees']._loaded_options = None
  _globals['_QUERY'].methods_by_name['TotalAckFees']._serialized_options = b'\202\323\344\223\002z\022x/ibc/apps/fee/v1/channels/{packet_id.channel_id}/ports/{packet_id.port_id}/sequences/{packet_id.sequence}/total_ack_fees'
  _globals['_QUERY'].methods_by_name['TotalTimeoutFees']._loaded_options = None
  _globals['_QUERY'].methods_by_name['TotalTimeoutFees']._serialized_options = b'\202\323\344\223\002~\022|/ibc/apps/fee/v1/channels/{packet_id.channel_id}/ports/{packet_id.port_id}/sequences/{packet_id.sequence}/total_timeout_fees'
  _globals['_QUERY'].methods_by_name['Payee']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Payee']._serialized_options = b'\202\323\344\223\002A\022?/ibc/apps/fee/v1/channels/{channel_id}/relayers/{relayer}/payee'
  _globals['_QUERY'].methods_by_name['CounterpartyPayee']._loaded_options = None
  _globals['_QUERY'].methods_by_name['CounterpartyPayee']._serialized_options = b'\202\323\344\223\002N\022L/ibc/apps/fee/v1/channels/{channel_id}/relayers/{relayer}/counterparty_payee'
  _globals['_QUERY'].methods_by_name['FeeEnabledChannels']._loaded_options = None
  _globals['_QUERY'].methods_by_name['FeeEnabledChannels']._serialized_options = b'\202\323\344\223\002\036\022\034/ibc/apps/fee/v1/fee_enabled'
  _globals['_QUERY'].methods_by_name['FeeEnabledChannel']._loaded_options = None
  _globals['_QUERY'].methods_by_name['FeeEnabledChannel']._serialized_options = b'\202\323\344\223\002D\022B/ibc/apps/fee/v1/channels/{channel_id}/ports/{port_id}/fee_enabled'
  _globals['_QUERYINCENTIVIZEDPACKETSREQUEST']._serialized_start=301
  _globals['_QUERYINCENTIVIZEDPACKETSREQUEST']._serialized_end=416
  _globals['_QUERYINCENTIVIZEDPACKETSRESPONSE']._serialized_start=419
  _globals['_QUERYINCENTIVIZEDPACKETSRESPONSE']._serialized_end=597
  _globals['_QUERYINCENTIVIZEDPACKETREQUEST']._serialized_start=599
  _globals['_QUERYINCENTIVIZEDPACKETREQUEST']._serialized_end=709
  _globals['_QUERYINCENTIVIZEDPACKETRESPONSE']._serialized_start=711
  _globals['_QUERYINCENTIVIZEDPACKETRESPONSE']._serialized_end=826
  _globals['_QUERYINCENTIVIZEDPACKETSFORCHANNELREQUEST']._serialized_start=829
  _globals['_QUERYINCENTIVIZEDPACKETSFORCHANNELREQUEST']._serialized_end=991
  _globals['_QUERYINCENTIVIZEDPACKETSFORCHANNELRESPONSE']._serialized_start=994
  _globals['_QUERYINCENTIVIZEDPACKETSFORCHANNELRESPONSE']._serialized_end=1176
  _globals['_QUERYTOTALRECVFEESREQUEST']._serialized_start=1178
  _globals['_QUERYTOTALRECVFEESREQUEST']._serialized_end=1261
  _globals['_QUERYTOTALRECVFEESRESPONSE']._serialized_start=1263
  _globals['_QUERYTOTALRECVFEESRESPONSE']._serialized_end=1387
  _globals['_QUERYTOTALACKFEESREQUEST']._serialized_start=1389
  _globals['_QUERYTOTALACKFEESREQUEST']._serialized_end=1471
  _globals['_QUERYTOTALACKFEESRESPONSE']._serialized_start=1473
  _globals['_QUERYTOTALACKFEESRESPONSE']._serialized_end=1595
  _globals['_QUERYTOTALTIMEOUTFEESREQUEST']._serialized_start=1597
  _globals['_QUERYTOTALTIMEOUTFEESREQUEST']._serialized_end=1683
  _globals['_QUERYTOTALTIMEOUTFEESRESPONSE']._serialized_start=1686
  _globals['_QUERYTOTALTIMEOUTFEESRESPONSE']._serialized_end=1816
  _globals['_QUERYPAYEEREQUEST']._serialized_start=1818
  _globals['_QUERYPAYEEREQUEST']._serialized_end=1874
  _globals['_QUERYPAYEERESPONSE']._serialized_start=1876
  _globals['_QUERYPAYEERESPONSE']._serialized_end=1919
  _globals['_QUERYCOUNTERPARTYPAYEEREQUEST']._serialized_start=1921
  _globals['_QUERYCOUNTERPARTYPAYEEREQUEST']._serialized_end=1989
  _globals['_QUERYCOUNTERPARTYPAYEERESPONSE']._serialized_start=1991
  _globals['_QUERYCOUNTERPARTYPAYEERESPONSE']._serialized_end=2051
  _globals['_QUERYFEEENABLEDCHANNELSREQUEST']._serialized_start=2053
  _globals['_QUERYFEEENABLEDCHANNELSREQUEST']._serialized_end=2167
  _globals['_QUERYFEEENABLEDCHANNELSRESPONSE']._serialized_start=2170
  _globals['_QUERYFEEENABLEDCHANNELSRESPONSE']._serialized_end=2344
  _globals['_QUERYFEEENABLEDCHANNELREQUEST']._serialized_start=2346
  _globals['_QUERYFEEENABLEDCHANNELREQUEST']._serialized_end=2414
  _globals['_QUERYFEEENABLEDCHANNELRESPONSE']._serialized_start=2416
  _globals['_QUERYFEEENABLEDCHANNELRESPONSE']._serialized_end=2469
  _globals['_QUERY']._serialized_start=2472
  _globals['_QUERY']._serialized_end=4750
# @@protoc_insertion_point(module_scope)
