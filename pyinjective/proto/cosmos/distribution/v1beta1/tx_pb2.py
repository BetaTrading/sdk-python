# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/distribution/v1beta1/tx.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from pyinjective.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from pyinjective.proto.cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from pyinjective.proto.amino import amino_pb2 as amino_dot_amino__pb2
from pyinjective.proto.cosmos.distribution.v1beta1 import distribution_pb2 as cosmos_dot_distribution_dot_v1beta1_dot_distribution__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$cosmos/distribution/v1beta1/tx.proto\x12\x1b\x63osmos.distribution.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x11\x61mino/amino.proto\x1a.cosmos/distribution/v1beta1/distribution.proto\"\xc8\x01\n\x15MsgSetWithdrawAddress\x12\x33\n\x11\x64\x65legator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x32\n\x10withdraw_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString:F\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x11\x64\x65legator_address\x8a\xe7\xb0*#cosmos-sdk/MsgModifyWithdrawAddress\"\x1f\n\x1dMsgSetWithdrawAddressResponse\"\xda\x01\n\x1aMsgWithdrawDelegatorReward\x12\x33\n\x11\x64\x65legator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12<\n\x11validator_address\x18\x02 \x01(\tB!\xd2\xb4-\x1d\x63osmos.ValidatorAddressString:I\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x11\x64\x65legator_address\x8a\xe7\xb0*&cosmos-sdk/MsgWithdrawDelegationReward\"\x97\x01\n\"MsgWithdrawDelegatorRewardResponse\x12q\n\x06\x61mount\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01\"\xa6\x01\n\x1eMsgWithdrawValidatorCommission\x12<\n\x11validator_address\x18\x01 \x01(\tB!\xd2\xb4-\x1d\x63osmos.ValidatorAddressString:F\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x11validator_address\x8a\xe7\xb0*#cosmos-sdk/MsgWithdrawValCommission\"\x9b\x01\n&MsgWithdrawValidatorCommissionResponse\x12q\n\x06\x61mount\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01\"\xf2\x01\n\x14MsgFundCommunityPool\x12q\n\x06\x61mount\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01\x12+\n\tdepositor\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString::\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\tdepositor\x8a\xe7\xb0*\x1f\x63osmos-sdk/MsgFundCommunityPool\"\x1e\n\x1cMsgFundCommunityPoolResponse\"\xba\x01\n\x0fMsgUpdateParams\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12>\n\x06params\x18\x02 \x01(\x0b\x32#.cosmos.distribution.v1beta1.ParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01::\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*\'cosmos-sdk/distribution/MsgUpdateParams\"\x19\n\x17MsgUpdateParamsResponse\"\x85\x02\n\x15MsgCommunityPoolSpend\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x11\n\trecipient\x18\x02 \x01(\t\x12q\n\x06\x61mount\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01:9\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*&cosmos-sdk/distr/MsgCommunityPoolSpend\"\x1f\n\x1dMsgCommunityPoolSpendResponse\"\xc0\x02\n\x1eMsgDepositValidatorRewardsPool\x12+\n\tdepositor\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12<\n\x11validator_address\x18\x02 \x01(\tB!\xd2\xb4-\x1d\x63osmos.ValidatorAddressString\x12q\n\x06\x61mount\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01:@\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\tdepositor\x8a\xe7\xb0*%cosmos-sdk/distr/MsgDepositValRewards\"(\n&MsgDepositValidatorRewardsPoolResponse2\xec\x07\n\x03Msg\x12\x84\x01\n\x12SetWithdrawAddress\x12\x32.cosmos.distribution.v1beta1.MsgSetWithdrawAddress\x1a:.cosmos.distribution.v1beta1.MsgSetWithdrawAddressResponse\x12\x93\x01\n\x17WithdrawDelegatorReward\x12\x37.cosmos.distribution.v1beta1.MsgWithdrawDelegatorReward\x1a?.cosmos.distribution.v1beta1.MsgWithdrawDelegatorRewardResponse\x12\x9f\x01\n\x1bWithdrawValidatorCommission\x12;.cosmos.distribution.v1beta1.MsgWithdrawValidatorCommission\x1a\x43.cosmos.distribution.v1beta1.MsgWithdrawValidatorCommissionResponse\x12\x81\x01\n\x11\x46undCommunityPool\x12\x31.cosmos.distribution.v1beta1.MsgFundCommunityPool\x1a\x39.cosmos.distribution.v1beta1.MsgFundCommunityPoolResponse\x12r\n\x0cUpdateParams\x12,.cosmos.distribution.v1beta1.MsgUpdateParams\x1a\x34.cosmos.distribution.v1beta1.MsgUpdateParamsResponse\x12\x84\x01\n\x12\x43ommunityPoolSpend\x12\x32.cosmos.distribution.v1beta1.MsgCommunityPoolSpend\x1a:.cosmos.distribution.v1beta1.MsgCommunityPoolSpendResponse\x12\x9f\x01\n\x1b\x44\x65positValidatorRewardsPool\x12;.cosmos.distribution.v1beta1.MsgDepositValidatorRewardsPool\x1a\x43.cosmos.distribution.v1beta1.MsgDepositValidatorRewardsPoolResponse\x1a\x05\x80\xe7\xb0*\x01\x42\x37Z1github.com/cosmos/cosmos-sdk/x/distribution/types\xa8\xe2\x1e\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.distribution.v1beta1.tx_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z1github.com/cosmos/cosmos-sdk/x/distribution/types\250\342\036\001'
  _globals['_MSGSETWITHDRAWADDRESS'].fields_by_name['delegator_address']._loaded_options = None
  _globals['_MSGSETWITHDRAWADDRESS'].fields_by_name['delegator_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGSETWITHDRAWADDRESS'].fields_by_name['withdraw_address']._loaded_options = None
  _globals['_MSGSETWITHDRAWADDRESS'].fields_by_name['withdraw_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGSETWITHDRAWADDRESS']._loaded_options = None
  _globals['_MSGSETWITHDRAWADDRESS']._serialized_options = b'\210\240\037\000\350\240\037\000\202\347\260*\021delegator_address\212\347\260*#cosmos-sdk/MsgModifyWithdrawAddress'
  _globals['_MSGWITHDRAWDELEGATORREWARD'].fields_by_name['delegator_address']._loaded_options = None
  _globals['_MSGWITHDRAWDELEGATORREWARD'].fields_by_name['delegator_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGWITHDRAWDELEGATORREWARD'].fields_by_name['validator_address']._loaded_options = None
  _globals['_MSGWITHDRAWDELEGATORREWARD'].fields_by_name['validator_address']._serialized_options = b'\322\264-\035cosmos.ValidatorAddressString'
  _globals['_MSGWITHDRAWDELEGATORREWARD']._loaded_options = None
  _globals['_MSGWITHDRAWDELEGATORREWARD']._serialized_options = b'\210\240\037\000\350\240\037\000\202\347\260*\021delegator_address\212\347\260*&cosmos-sdk/MsgWithdrawDelegationReward'
  _globals['_MSGWITHDRAWDELEGATORREWARDRESPONSE'].fields_by_name['amount']._loaded_options = None
  _globals['_MSGWITHDRAWDELEGATORREWARDRESPONSE'].fields_by_name['amount']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\232\347\260*\014legacy_coins\250\347\260*\001'
  _globals['_MSGWITHDRAWVALIDATORCOMMISSION'].fields_by_name['validator_address']._loaded_options = None
  _globals['_MSGWITHDRAWVALIDATORCOMMISSION'].fields_by_name['validator_address']._serialized_options = b'\322\264-\035cosmos.ValidatorAddressString'
  _globals['_MSGWITHDRAWVALIDATORCOMMISSION']._loaded_options = None
  _globals['_MSGWITHDRAWVALIDATORCOMMISSION']._serialized_options = b'\210\240\037\000\350\240\037\000\202\347\260*\021validator_address\212\347\260*#cosmos-sdk/MsgWithdrawValCommission'
  _globals['_MSGWITHDRAWVALIDATORCOMMISSIONRESPONSE'].fields_by_name['amount']._loaded_options = None
  _globals['_MSGWITHDRAWVALIDATORCOMMISSIONRESPONSE'].fields_by_name['amount']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\232\347\260*\014legacy_coins\250\347\260*\001'
  _globals['_MSGFUNDCOMMUNITYPOOL'].fields_by_name['amount']._loaded_options = None
  _globals['_MSGFUNDCOMMUNITYPOOL'].fields_by_name['amount']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\232\347\260*\014legacy_coins\250\347\260*\001'
  _globals['_MSGFUNDCOMMUNITYPOOL'].fields_by_name['depositor']._loaded_options = None
  _globals['_MSGFUNDCOMMUNITYPOOL'].fields_by_name['depositor']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGFUNDCOMMUNITYPOOL']._loaded_options = None
  _globals['_MSGFUNDCOMMUNITYPOOL']._serialized_options = b'\210\240\037\000\350\240\037\000\202\347\260*\tdepositor\212\347\260*\037cosmos-sdk/MsgFundCommunityPool'
  _globals['_MSGUPDATEPARAMS'].fields_by_name['authority']._loaded_options = None
  _globals['_MSGUPDATEPARAMS'].fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGUPDATEPARAMS'].fields_by_name['params']._loaded_options = None
  _globals['_MSGUPDATEPARAMS'].fields_by_name['params']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_MSGUPDATEPARAMS']._loaded_options = None
  _globals['_MSGUPDATEPARAMS']._serialized_options = b'\202\347\260*\tauthority\212\347\260*\'cosmos-sdk/distribution/MsgUpdateParams'
  _globals['_MSGCOMMUNITYPOOLSPEND'].fields_by_name['authority']._loaded_options = None
  _globals['_MSGCOMMUNITYPOOLSPEND'].fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGCOMMUNITYPOOLSPEND'].fields_by_name['amount']._loaded_options = None
  _globals['_MSGCOMMUNITYPOOLSPEND'].fields_by_name['amount']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\232\347\260*\014legacy_coins\250\347\260*\001'
  _globals['_MSGCOMMUNITYPOOLSPEND']._loaded_options = None
  _globals['_MSGCOMMUNITYPOOLSPEND']._serialized_options = b'\202\347\260*\tauthority\212\347\260*&cosmos-sdk/distr/MsgCommunityPoolSpend'
  _globals['_MSGDEPOSITVALIDATORREWARDSPOOL'].fields_by_name['depositor']._loaded_options = None
  _globals['_MSGDEPOSITVALIDATORREWARDSPOOL'].fields_by_name['depositor']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGDEPOSITVALIDATORREWARDSPOOL'].fields_by_name['validator_address']._loaded_options = None
  _globals['_MSGDEPOSITVALIDATORREWARDSPOOL'].fields_by_name['validator_address']._serialized_options = b'\322\264-\035cosmos.ValidatorAddressString'
  _globals['_MSGDEPOSITVALIDATORREWARDSPOOL'].fields_by_name['amount']._loaded_options = None
  _globals['_MSGDEPOSITVALIDATORREWARDSPOOL'].fields_by_name['amount']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\232\347\260*\014legacy_coins\250\347\260*\001'
  _globals['_MSGDEPOSITVALIDATORREWARDSPOOL']._loaded_options = None
  _globals['_MSGDEPOSITVALIDATORREWARDSPOOL']._serialized_options = b'\210\240\037\000\350\240\037\000\202\347\260*\tdepositor\212\347\260*%cosmos-sdk/distr/MsgDepositValRewards'
  _globals['_MSG']._loaded_options = None
  _globals['_MSG']._serialized_options = b'\200\347\260*\001'
  _globals['_MSGSETWITHDRAWADDRESS']._serialized_start=243
  _globals['_MSGSETWITHDRAWADDRESS']._serialized_end=443
  _globals['_MSGSETWITHDRAWADDRESSRESPONSE']._serialized_start=445
  _globals['_MSGSETWITHDRAWADDRESSRESPONSE']._serialized_end=476
  _globals['_MSGWITHDRAWDELEGATORREWARD']._serialized_start=479
  _globals['_MSGWITHDRAWDELEGATORREWARD']._serialized_end=697
  _globals['_MSGWITHDRAWDELEGATORREWARDRESPONSE']._serialized_start=700
  _globals['_MSGWITHDRAWDELEGATORREWARDRESPONSE']._serialized_end=851
  _globals['_MSGWITHDRAWVALIDATORCOMMISSION']._serialized_start=854
  _globals['_MSGWITHDRAWVALIDATORCOMMISSION']._serialized_end=1020
  _globals['_MSGWITHDRAWVALIDATORCOMMISSIONRESPONSE']._serialized_start=1023
  _globals['_MSGWITHDRAWVALIDATORCOMMISSIONRESPONSE']._serialized_end=1178
  _globals['_MSGFUNDCOMMUNITYPOOL']._serialized_start=1181
  _globals['_MSGFUNDCOMMUNITYPOOL']._serialized_end=1423
  _globals['_MSGFUNDCOMMUNITYPOOLRESPONSE']._serialized_start=1425
  _globals['_MSGFUNDCOMMUNITYPOOLRESPONSE']._serialized_end=1455
  _globals['_MSGUPDATEPARAMS']._serialized_start=1458
  _globals['_MSGUPDATEPARAMS']._serialized_end=1644
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_start=1646
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_end=1671
  _globals['_MSGCOMMUNITYPOOLSPEND']._serialized_start=1674
  _globals['_MSGCOMMUNITYPOOLSPEND']._serialized_end=1935
  _globals['_MSGCOMMUNITYPOOLSPENDRESPONSE']._serialized_start=1937
  _globals['_MSGCOMMUNITYPOOLSPENDRESPONSE']._serialized_end=1968
  _globals['_MSGDEPOSITVALIDATORREWARDSPOOL']._serialized_start=1971
  _globals['_MSGDEPOSITVALIDATORREWARDSPOOL']._serialized_end=2291
  _globals['_MSGDEPOSITVALIDATORREWARDSPOOLRESPONSE']._serialized_start=2293
  _globals['_MSGDEPOSITVALIDATORREWARDSPOOLRESPONSE']._serialized_end=2333
  _globals['_MSG']._serialized_start=2336
  _globals['_MSG']._serialized_end=3340
# @@protoc_insertion_point(module_scope)
