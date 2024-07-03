# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/gov/v1beta1/gov.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from pyinjective.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from pyinjective.proto.amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x63osmos/gov/v1beta1/gov.proto\x12\x12\x63osmos.gov.v1beta1\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19google/protobuf/any.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x11\x61mino/amino.proto\"\x8c\x01\n\x12WeightedVoteOption\x12.\n\x06option\x18\x01 \x01(\x0e\x32\x1e.cosmos.gov.v1beta1.VoteOption\x12\x46\n\x06weight\x18\x02 \x01(\tB6\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.Dec\xa8\xe7\xb0*\x01\"r\n\x0cTextProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t:>\xe8\xa0\x1f\x01\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\x8a\xe7\xb0*\x17\x63osmos-sdk/TextProposal\"\xb7\x01\n\x07\x44\x65posit\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\x12+\n\tdepositor\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12`\n\x06\x61mount\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB5\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xa8\xe7\xb0*\x01:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\"\xe0\x04\n\x08Proposal\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\x12\x45\n\x07\x63ontent\x18\x02 \x01(\x0b\x32\x14.google.protobuf.AnyB\x1e\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\x12\x32\n\x06status\x18\x03 \x01(\x0e\x32\".cosmos.gov.v1beta1.ProposalStatus\x12\x46\n\x12\x66inal_tally_result\x18\x04 \x01(\x0b\x32\x1f.cosmos.gov.v1beta1.TallyResultB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12>\n\x0bsubmit_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\r\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01\x12\x43\n\x10\x64\x65posit_end_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\r\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01\x12g\n\rtotal_deposit\x18\x07 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB5\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xa8\xe7\xb0*\x01\x12\x44\n\x11voting_start_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\r\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01\x12\x42\n\x0fvoting_end_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampB\r\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01:\x04\xe8\xa0\x1f\x01\"\x87\x02\n\x0bTallyResult\x12\x38\n\x03yes\x18\x01 \x01(\tB+\xc8\xde\x1f\x00\xda\xde\x1f\x15\x63osmossdk.io/math.Int\xd2\xb4-\ncosmos.Int\x12<\n\x07\x61\x62stain\x18\x02 \x01(\tB+\xc8\xde\x1f\x00\xda\xde\x1f\x15\x63osmossdk.io/math.Int\xd2\xb4-\ncosmos.Int\x12\x37\n\x02no\x18\x03 \x01(\tB+\xc8\xde\x1f\x00\xda\xde\x1f\x15\x63osmossdk.io/math.Int\xd2\xb4-\ncosmos.Int\x12\x41\n\x0cno_with_veto\x18\x04 \x01(\tB+\xc8\xde\x1f\x00\xda\xde\x1f\x15\x63osmossdk.io/math.Int\xd2\xb4-\ncosmos.Int:\x04\xe8\xa0\x1f\x01\"\xd6\x01\n\x04Vote\x12\'\n\x0bproposal_id\x18\x01 \x01(\x04\x42\x12\xea\xde\x1f\x02id\xa2\xe7\xb0*\x02id\xa8\xe7\xb0*\x01\x12\'\n\x05voter\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x32\n\x06option\x18\x03 \x01(\x0e\x32\x1e.cosmos.gov.v1beta1.VoteOptionB\x02\x18\x01\x12\x42\n\x07options\x18\x04 \x03(\x0b\x32&.cosmos.gov.v1beta1.WeightedVoteOptionB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:\x04\xe8\xa0\x1f\x00\"\xeb\x01\n\rDepositParams\x12y\n\x0bmin_deposit\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBI\xc8\xde\x1f\x00\xea\xde\x1f\x15min_deposit,omitempty\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12_\n\x12max_deposit_period\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB(\xc8\xde\x1f\x00\xea\xde\x1f\x1cmax_deposit_period,omitempty\x98\xdf\x1f\x01\"e\n\x0cVotingParams\x12U\n\rvoting_period\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB#\xc8\xde\x1f\x00\xea\xde\x1f\x17voting_period,omitempty\x98\xdf\x1f\x01\"\xa8\x02\n\x0bTallyParams\x12U\n\x06quorum\x18\x01 \x01(\x0c\x42\x45\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\xea\xde\x1f\x10quorum,omitempty\xd2\xb4-\ncosmos.Dec\x12[\n\tthreshold\x18\x02 \x01(\x0c\x42H\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\xea\xde\x1f\x13threshold,omitempty\xd2\xb4-\ncosmos.Dec\x12\x65\n\x0eveto_threshold\x18\x03 \x01(\x0c\x42M\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\xea\xde\x1f\x18veto_threshold,omitempty\xd2\xb4-\ncosmos.Dec*\xe6\x01\n\nVoteOption\x12,\n\x17VOTE_OPTION_UNSPECIFIED\x10\x00\x1a\x0f\x8a\x9d \x0bOptionEmpty\x12\"\n\x0fVOTE_OPTION_YES\x10\x01\x1a\r\x8a\x9d \tOptionYes\x12*\n\x13VOTE_OPTION_ABSTAIN\x10\x02\x1a\x11\x8a\x9d \rOptionAbstain\x12 \n\x0eVOTE_OPTION_NO\x10\x03\x1a\x0c\x8a\x9d \x08OptionNo\x12\x32\n\x18VOTE_OPTION_NO_WITH_VETO\x10\x04\x1a\x14\x8a\x9d \x10OptionNoWithVeto\x1a\x04\x88\xa3\x1e\x00*\xcc\x02\n\x0eProposalStatus\x12.\n\x1bPROPOSAL_STATUS_UNSPECIFIED\x10\x00\x1a\r\x8a\x9d \tStatusNil\x12;\n\x1ePROPOSAL_STATUS_DEPOSIT_PERIOD\x10\x01\x1a\x17\x8a\x9d \x13StatusDepositPeriod\x12\x39\n\x1dPROPOSAL_STATUS_VOTING_PERIOD\x10\x02\x1a\x16\x8a\x9d \x12StatusVotingPeriod\x12,\n\x16PROPOSAL_STATUS_PASSED\x10\x03\x1a\x10\x8a\x9d \x0cStatusPassed\x12\x30\n\x18PROPOSAL_STATUS_REJECTED\x10\x04\x1a\x12\x8a\x9d \x0eStatusRejected\x12,\n\x16PROPOSAL_STATUS_FAILED\x10\x05\x1a\x10\x8a\x9d \x0cStatusFailed\x1a\x04\x88\xa3\x1e\x00\x42\x36Z0github.com/cosmos/cosmos-sdk/x/gov/types/v1beta1\xc8\xe1\x1e\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.gov.v1beta1.gov_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z0github.com/cosmos/cosmos-sdk/x/gov/types/v1beta1\310\341\036\000'
  _globals['_VOTEOPTION']._loaded_options = None
  _globals['_VOTEOPTION']._serialized_options = b'\210\243\036\000'
  _globals['_VOTEOPTION'].values_by_name["VOTE_OPTION_UNSPECIFIED"]._loaded_options = None
  _globals['_VOTEOPTION'].values_by_name["VOTE_OPTION_UNSPECIFIED"]._serialized_options = b'\212\235 \013OptionEmpty'
  _globals['_VOTEOPTION'].values_by_name["VOTE_OPTION_YES"]._loaded_options = None
  _globals['_VOTEOPTION'].values_by_name["VOTE_OPTION_YES"]._serialized_options = b'\212\235 \tOptionYes'
  _globals['_VOTEOPTION'].values_by_name["VOTE_OPTION_ABSTAIN"]._loaded_options = None
  _globals['_VOTEOPTION'].values_by_name["VOTE_OPTION_ABSTAIN"]._serialized_options = b'\212\235 \rOptionAbstain'
  _globals['_VOTEOPTION'].values_by_name["VOTE_OPTION_NO"]._loaded_options = None
  _globals['_VOTEOPTION'].values_by_name["VOTE_OPTION_NO"]._serialized_options = b'\212\235 \010OptionNo'
  _globals['_VOTEOPTION'].values_by_name["VOTE_OPTION_NO_WITH_VETO"]._loaded_options = None
  _globals['_VOTEOPTION'].values_by_name["VOTE_OPTION_NO_WITH_VETO"]._serialized_options = b'\212\235 \020OptionNoWithVeto'
  _globals['_PROPOSALSTATUS']._loaded_options = None
  _globals['_PROPOSALSTATUS']._serialized_options = b'\210\243\036\000'
  _globals['_PROPOSALSTATUS'].values_by_name["PROPOSAL_STATUS_UNSPECIFIED"]._loaded_options = None
  _globals['_PROPOSALSTATUS'].values_by_name["PROPOSAL_STATUS_UNSPECIFIED"]._serialized_options = b'\212\235 \tStatusNil'
  _globals['_PROPOSALSTATUS'].values_by_name["PROPOSAL_STATUS_DEPOSIT_PERIOD"]._loaded_options = None
  _globals['_PROPOSALSTATUS'].values_by_name["PROPOSAL_STATUS_DEPOSIT_PERIOD"]._serialized_options = b'\212\235 \023StatusDepositPeriod'
  _globals['_PROPOSALSTATUS'].values_by_name["PROPOSAL_STATUS_VOTING_PERIOD"]._loaded_options = None
  _globals['_PROPOSALSTATUS'].values_by_name["PROPOSAL_STATUS_VOTING_PERIOD"]._serialized_options = b'\212\235 \022StatusVotingPeriod'
  _globals['_PROPOSALSTATUS'].values_by_name["PROPOSAL_STATUS_PASSED"]._loaded_options = None
  _globals['_PROPOSALSTATUS'].values_by_name["PROPOSAL_STATUS_PASSED"]._serialized_options = b'\212\235 \014StatusPassed'
  _globals['_PROPOSALSTATUS'].values_by_name["PROPOSAL_STATUS_REJECTED"]._loaded_options = None
  _globals['_PROPOSALSTATUS'].values_by_name["PROPOSAL_STATUS_REJECTED"]._serialized_options = b'\212\235 \016StatusRejected'
  _globals['_PROPOSALSTATUS'].values_by_name["PROPOSAL_STATUS_FAILED"]._loaded_options = None
  _globals['_PROPOSALSTATUS'].values_by_name["PROPOSAL_STATUS_FAILED"]._serialized_options = b'\212\235 \014StatusFailed'
  _globals['_WEIGHTEDVOTEOPTION'].fields_by_name['weight']._loaded_options = None
  _globals['_WEIGHTEDVOTEOPTION'].fields_by_name['weight']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec\322\264-\ncosmos.Dec\250\347\260*\001'
  _globals['_TEXTPROPOSAL']._loaded_options = None
  _globals['_TEXTPROPOSAL']._serialized_options = b'\350\240\037\001\312\264-\032cosmos.gov.v1beta1.Content\212\347\260*\027cosmos-sdk/TextProposal'
  _globals['_DEPOSIT'].fields_by_name['depositor']._loaded_options = None
  _globals['_DEPOSIT'].fields_by_name['depositor']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_DEPOSIT'].fields_by_name['amount']._loaded_options = None
  _globals['_DEPOSIT'].fields_by_name['amount']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\250\347\260*\001'
  _globals['_DEPOSIT']._loaded_options = None
  _globals['_DEPOSIT']._serialized_options = b'\210\240\037\000\350\240\037\000'
  _globals['_PROPOSAL'].fields_by_name['content']._loaded_options = None
  _globals['_PROPOSAL'].fields_by_name['content']._serialized_options = b'\312\264-\032cosmos.gov.v1beta1.Content'
  _globals['_PROPOSAL'].fields_by_name['final_tally_result']._loaded_options = None
  _globals['_PROPOSAL'].fields_by_name['final_tally_result']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_PROPOSAL'].fields_by_name['submit_time']._loaded_options = None
  _globals['_PROPOSAL'].fields_by_name['submit_time']._serialized_options = b'\310\336\037\000\220\337\037\001\250\347\260*\001'
  _globals['_PROPOSAL'].fields_by_name['deposit_end_time']._loaded_options = None
  _globals['_PROPOSAL'].fields_by_name['deposit_end_time']._serialized_options = b'\310\336\037\000\220\337\037\001\250\347\260*\001'
  _globals['_PROPOSAL'].fields_by_name['total_deposit']._loaded_options = None
  _globals['_PROPOSAL'].fields_by_name['total_deposit']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\250\347\260*\001'
  _globals['_PROPOSAL'].fields_by_name['voting_start_time']._loaded_options = None
  _globals['_PROPOSAL'].fields_by_name['voting_start_time']._serialized_options = b'\310\336\037\000\220\337\037\001\250\347\260*\001'
  _globals['_PROPOSAL'].fields_by_name['voting_end_time']._loaded_options = None
  _globals['_PROPOSAL'].fields_by_name['voting_end_time']._serialized_options = b'\310\336\037\000\220\337\037\001\250\347\260*\001'
  _globals['_PROPOSAL']._loaded_options = None
  _globals['_PROPOSAL']._serialized_options = b'\350\240\037\001'
  _globals['_TALLYRESULT'].fields_by_name['yes']._loaded_options = None
  _globals['_TALLYRESULT'].fields_by_name['yes']._serialized_options = b'\310\336\037\000\332\336\037\025cosmossdk.io/math.Int\322\264-\ncosmos.Int'
  _globals['_TALLYRESULT'].fields_by_name['abstain']._loaded_options = None
  _globals['_TALLYRESULT'].fields_by_name['abstain']._serialized_options = b'\310\336\037\000\332\336\037\025cosmossdk.io/math.Int\322\264-\ncosmos.Int'
  _globals['_TALLYRESULT'].fields_by_name['no']._loaded_options = None
  _globals['_TALLYRESULT'].fields_by_name['no']._serialized_options = b'\310\336\037\000\332\336\037\025cosmossdk.io/math.Int\322\264-\ncosmos.Int'
  _globals['_TALLYRESULT'].fields_by_name['no_with_veto']._loaded_options = None
  _globals['_TALLYRESULT'].fields_by_name['no_with_veto']._serialized_options = b'\310\336\037\000\332\336\037\025cosmossdk.io/math.Int\322\264-\ncosmos.Int'
  _globals['_TALLYRESULT']._loaded_options = None
  _globals['_TALLYRESULT']._serialized_options = b'\350\240\037\001'
  _globals['_VOTE'].fields_by_name['proposal_id']._loaded_options = None
  _globals['_VOTE'].fields_by_name['proposal_id']._serialized_options = b'\352\336\037\002id\242\347\260*\002id\250\347\260*\001'
  _globals['_VOTE'].fields_by_name['voter']._loaded_options = None
  _globals['_VOTE'].fields_by_name['voter']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_VOTE'].fields_by_name['option']._loaded_options = None
  _globals['_VOTE'].fields_by_name['option']._serialized_options = b'\030\001'
  _globals['_VOTE'].fields_by_name['options']._loaded_options = None
  _globals['_VOTE'].fields_by_name['options']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_VOTE']._loaded_options = None
  _globals['_VOTE']._serialized_options = b'\350\240\037\000'
  _globals['_DEPOSITPARAMS'].fields_by_name['min_deposit']._loaded_options = None
  _globals['_DEPOSITPARAMS'].fields_by_name['min_deposit']._serialized_options = b'\310\336\037\000\352\336\037\025min_deposit,omitempty\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _globals['_DEPOSITPARAMS'].fields_by_name['max_deposit_period']._loaded_options = None
  _globals['_DEPOSITPARAMS'].fields_by_name['max_deposit_period']._serialized_options = b'\310\336\037\000\352\336\037\034max_deposit_period,omitempty\230\337\037\001'
  _globals['_VOTINGPARAMS'].fields_by_name['voting_period']._loaded_options = None
  _globals['_VOTINGPARAMS'].fields_by_name['voting_period']._serialized_options = b'\310\336\037\000\352\336\037\027voting_period,omitempty\230\337\037\001'
  _globals['_TALLYPARAMS'].fields_by_name['quorum']._loaded_options = None
  _globals['_TALLYPARAMS'].fields_by_name['quorum']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec\352\336\037\020quorum,omitempty\322\264-\ncosmos.Dec'
  _globals['_TALLYPARAMS'].fields_by_name['threshold']._loaded_options = None
  _globals['_TALLYPARAMS'].fields_by_name['threshold']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec\352\336\037\023threshold,omitempty\322\264-\ncosmos.Dec'
  _globals['_TALLYPARAMS'].fields_by_name['veto_threshold']._loaded_options = None
  _globals['_TALLYPARAMS'].fields_by_name['veto_threshold']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec\352\336\037\030veto_threshold,omitempty\322\264-\ncosmos.Dec'
  _globals['_VOTEOPTION']._serialized_start=2424
  _globals['_VOTEOPTION']._serialized_end=2654
  _globals['_PROPOSALSTATUS']._serialized_start=2657
  _globals['_PROPOSALSTATUS']._serialized_end=2989
  _globals['_WEIGHTEDVOTEOPTION']._serialized_start=245
  _globals['_WEIGHTEDVOTEOPTION']._serialized_end=385
  _globals['_TEXTPROPOSAL']._serialized_start=387
  _globals['_TEXTPROPOSAL']._serialized_end=501
  _globals['_DEPOSIT']._serialized_start=504
  _globals['_DEPOSIT']._serialized_end=687
  _globals['_PROPOSAL']._serialized_start=690
  _globals['_PROPOSAL']._serialized_end=1298
  _globals['_TALLYRESULT']._serialized_start=1301
  _globals['_TALLYRESULT']._serialized_end=1564
  _globals['_VOTE']._serialized_start=1567
  _globals['_VOTE']._serialized_end=1781
  _globals['_DEPOSITPARAMS']._serialized_start=1784
  _globals['_DEPOSITPARAMS']._serialized_end=2019
  _globals['_VOTINGPARAMS']._serialized_start=2021
  _globals['_VOTINGPARAMS']._serialized_end=2122
  _globals['_TALLYPARAMS']._serialized_start=2125
  _globals['_TALLYPARAMS']._serialized_end=2421
# @@protoc_insertion_point(module_scope)
