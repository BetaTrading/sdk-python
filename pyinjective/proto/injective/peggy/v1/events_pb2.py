# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/peggy/v1/events.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.injective.peggy.v1 import attestation_pb2 as injective_dot_peggy_dot_v1_dot_attestation__pb2
from pyinjective.proto.injective.peggy.v1 import types_pb2 as injective_dot_peggy_dot_v1_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1finjective/peggy/v1/events.proto\x12\x12injective.peggy.v1\x1a\x14gogoproto/gogo.proto\x1a$injective/peggy/v1/attestation.proto\x1a\x1einjective/peggy/v1/types.proto\"\xac\x01\n\x18\x45ventAttestationObserved\x12\x37\n\x10\x61ttestation_type\x18\x01 \x01(\x0e\x32\x1d.injective.peggy.v1.ClaimType\x12\x17\n\x0f\x62ridge_contract\x18\x02 \x01(\t\x12\x17\n\x0f\x62ridge_chain_id\x18\x03 \x01(\x04\x12\x16\n\x0e\x61ttestation_id\x18\x04 \x01(\x0c\x12\r\n\x05nonce\x18\x05 \x01(\x04\"O\n\x1b\x45ventBridgeWithdrawCanceled\x12\x17\n\x0f\x62ridge_contract\x18\x01 \x01(\t\x12\x17\n\x0f\x62ridge_chain_id\x18\x02 \x01(\x04\"\x83\x01\n\x12\x45ventOutgoingBatch\x12\r\n\x05\x64\x65nom\x18\x01 \x01(\t\x12\x1c\n\x14orchestrator_address\x18\x02 \x01(\t\x12\x13\n\x0b\x62\x61tch_nonce\x18\x03 \x01(\x04\x12\x15\n\rbatch_timeout\x18\x04 \x01(\x04\x12\x14\n\x0c\x62\x61tch_tx_ids\x18\x05 \x03(\x04\"o\n\x1a\x45ventOutgoingBatchCanceled\x12\x17\n\x0f\x62ridge_contract\x18\x01 \x01(\t\x12\x17\n\x0f\x62ridge_chain_id\x18\x02 \x01(\x04\x12\x10\n\x08\x62\x61tch_id\x18\x03 \x01(\x04\x12\r\n\x05nonce\x18\x04 \x01(\x04\"\xd0\x01\n\x18\x45ventValsetUpdateRequest\x12\x14\n\x0cvalset_nonce\x18\x01 \x01(\x04\x12\x15\n\rvalset_height\x18\x02 \x01(\x04\x12;\n\x0evalset_members\x18\x03 \x03(\x0b\x32#.injective.peggy.v1.BridgeValidator\x12\x34\n\rreward_amount\x18\x04 \x01(\tB\x1d\xc8\xde\x1f\x00\xda\xde\x1f\x15\x63osmossdk.io/math.Int\x12\x14\n\x0creward_token\x18\x05 \x01(\t\"v\n\x1d\x45ventSetOrchestratorAddresses\x12\x19\n\x11validator_address\x18\x01 \x01(\t\x12\x1c\n\x14orchestrator_address\x18\x02 \x01(\t\x12\x1c\n\x14operator_eth_address\x18\x03 \x01(\t\"H\n\x12\x45ventValsetConfirm\x12\x14\n\x0cvalset_nonce\x18\x01 \x01(\x04\x12\x1c\n\x14orchestrator_address\x18\x02 \x01(\t\"\xd0\x01\n\x0e\x45ventSendToEth\x12\x16\n\x0eoutgoing_tx_id\x18\x01 \x01(\x04\x12\x0e\n\x06sender\x18\x02 \x01(\t\x12\x10\n\x08receiver\x18\x03 \x01(\t\x12?\n\x06\x61mount\x18\x04 \x01(\tB/\xc8\xde\x1f\x00\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Coin\x12\x43\n\nbridge_fee\x18\x05 \x01(\tB/\xc8\xde\x1f\x00\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Coin\"F\n\x11\x45ventConfirmBatch\x12\x13\n\x0b\x62\x61tch_nonce\x18\x01 \x01(\x04\x12\x1c\n\x14orchestrator_address\x18\x02 \x01(\t\"R\n\x14\x45ventAttestationVote\x12\x13\n\x0b\x65vent_nonce\x18\x01 \x01(\x04\x12\x16\n\x0e\x61ttestation_id\x18\x02 \x01(\x0c\x12\r\n\x05voter\x18\x03 \x01(\t\"\xfb\x01\n\x11\x45ventDepositClaim\x12\x13\n\x0b\x65vent_nonce\x18\x01 \x01(\x04\x12\x14\n\x0c\x65vent_height\x18\x02 \x01(\x04\x12\x16\n\x0e\x61ttestation_id\x18\x03 \x01(\x0c\x12\x17\n\x0f\x65thereum_sender\x18\x04 \x01(\t\x12\x17\n\x0f\x63osmos_receiver\x18\x05 \x01(\t\x12\x16\n\x0etoken_contract\x18\x06 \x01(\t\x12-\n\x06\x61mount\x18\x07 \x01(\tB\x1d\xc8\xde\x1f\x00\xda\xde\x1f\x15\x63osmossdk.io/math.Int\x12\x1c\n\x14orchestrator_address\x18\x08 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\t \x01(\t\"\xa2\x01\n\x12\x45ventWithdrawClaim\x12\x13\n\x0b\x65vent_nonce\x18\x01 \x01(\x04\x12\x14\n\x0c\x65vent_height\x18\x02 \x01(\x04\x12\x16\n\x0e\x61ttestation_id\x18\x03 \x01(\x0c\x12\x13\n\x0b\x62\x61tch_nonce\x18\x04 \x01(\x04\x12\x16\n\x0etoken_contract\x18\x05 \x01(\t\x12\x1c\n\x14orchestrator_address\x18\x06 \x01(\t\"\xd8\x01\n\x17\x45ventERC20DeployedClaim\x12\x13\n\x0b\x65vent_nonce\x18\x01 \x01(\x04\x12\x14\n\x0c\x65vent_height\x18\x02 \x01(\x04\x12\x16\n\x0e\x61ttestation_id\x18\x03 \x01(\x0c\x12\x14\n\x0c\x63osmos_denom\x18\x04 \x01(\t\x12\x16\n\x0etoken_contract\x18\x05 \x01(\t\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x0e\n\x06symbol\x18\x07 \x01(\t\x12\x10\n\x08\x64\x65\x63imals\x18\x08 \x01(\x04\x12\x1c\n\x14orchestrator_address\x18\t \x01(\t\"\x98\x02\n\x16\x45ventValsetUpdateClaim\x12\x13\n\x0b\x65vent_nonce\x18\x01 \x01(\x04\x12\x14\n\x0c\x65vent_height\x18\x02 \x01(\x04\x12\x16\n\x0e\x61ttestation_id\x18\x03 \x01(\x0c\x12\x14\n\x0cvalset_nonce\x18\x04 \x01(\x04\x12;\n\x0evalset_members\x18\x05 \x03(\x0b\x32#.injective.peggy.v1.BridgeValidator\x12\x34\n\rreward_amount\x18\x06 \x01(\tB\x1d\xc8\xde\x1f\x00\xda\xde\x1f\x15\x63osmossdk.io/math.Int\x12\x14\n\x0creward_token\x18\x07 \x01(\t\x12\x1c\n\x14orchestrator_address\x18\x08 \x01(\t\".\n\x14\x45ventCancelSendToEth\x12\x16\n\x0eoutgoing_tx_id\x18\x01 \x01(\x04\"_\n\x1f\x45ventSubmitBadSignatureEvidence\x12\x19\n\x11\x62\x61\x64_eth_signature\x18\x01 \x01(\t\x12!\n\x19\x62\x61\x64_eth_signature_subject\x18\x02 \x01(\t\"z\n\x13\x45ventValidatorSlash\x12\r\n\x05power\x18\x01 \x01(\x03\x12\x0e\n\x06reason\x18\x02 \x01(\t\x12\x19\n\x11\x63onsensus_address\x18\x03 \x01(\t\x12\x18\n\x10operator_address\x18\x04 \x01(\t\x12\x0f\n\x07moniker\x18\x05 \x01(\tBMZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/peggy/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.peggy.v1.events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/peggy/types'
  _globals['_EVENTVALSETUPDATEREQUEST'].fields_by_name['reward_amount']._loaded_options = None
  _globals['_EVENTVALSETUPDATEREQUEST'].fields_by_name['reward_amount']._serialized_options = b'\310\336\037\000\332\336\037\025cosmossdk.io/math.Int'
  _globals['_EVENTSENDTOETH'].fields_by_name['amount']._loaded_options = None
  _globals['_EVENTSENDTOETH'].fields_by_name['amount']._serialized_options = b'\310\336\037\000\332\336\037\'github.com/cosmos/cosmos-sdk/types.Coin'
  _globals['_EVENTSENDTOETH'].fields_by_name['bridge_fee']._loaded_options = None
  _globals['_EVENTSENDTOETH'].fields_by_name['bridge_fee']._serialized_options = b'\310\336\037\000\332\336\037\'github.com/cosmos/cosmos-sdk/types.Coin'
  _globals['_EVENTDEPOSITCLAIM'].fields_by_name['amount']._loaded_options = None
  _globals['_EVENTDEPOSITCLAIM'].fields_by_name['amount']._serialized_options = b'\310\336\037\000\332\336\037\025cosmossdk.io/math.Int'
  _globals['_EVENTVALSETUPDATECLAIM'].fields_by_name['reward_amount']._loaded_options = None
  _globals['_EVENTVALSETUPDATECLAIM'].fields_by_name['reward_amount']._serialized_options = b'\310\336\037\000\332\336\037\025cosmossdk.io/math.Int'
  _globals['_EVENTATTESTATIONOBSERVED']._serialized_start=148
  _globals['_EVENTATTESTATIONOBSERVED']._serialized_end=320
  _globals['_EVENTBRIDGEWITHDRAWCANCELED']._serialized_start=322
  _globals['_EVENTBRIDGEWITHDRAWCANCELED']._serialized_end=401
  _globals['_EVENTOUTGOINGBATCH']._serialized_start=404
  _globals['_EVENTOUTGOINGBATCH']._serialized_end=535
  _globals['_EVENTOUTGOINGBATCHCANCELED']._serialized_start=537
  _globals['_EVENTOUTGOINGBATCHCANCELED']._serialized_end=648
  _globals['_EVENTVALSETUPDATEREQUEST']._serialized_start=651
  _globals['_EVENTVALSETUPDATEREQUEST']._serialized_end=859
  _globals['_EVENTSETORCHESTRATORADDRESSES']._serialized_start=861
  _globals['_EVENTSETORCHESTRATORADDRESSES']._serialized_end=979
  _globals['_EVENTVALSETCONFIRM']._serialized_start=981
  _globals['_EVENTVALSETCONFIRM']._serialized_end=1053
  _globals['_EVENTSENDTOETH']._serialized_start=1056
  _globals['_EVENTSENDTOETH']._serialized_end=1264
  _globals['_EVENTCONFIRMBATCH']._serialized_start=1266
  _globals['_EVENTCONFIRMBATCH']._serialized_end=1336
  _globals['_EVENTATTESTATIONVOTE']._serialized_start=1338
  _globals['_EVENTATTESTATIONVOTE']._serialized_end=1420
  _globals['_EVENTDEPOSITCLAIM']._serialized_start=1423
  _globals['_EVENTDEPOSITCLAIM']._serialized_end=1674
  _globals['_EVENTWITHDRAWCLAIM']._serialized_start=1677
  _globals['_EVENTWITHDRAWCLAIM']._serialized_end=1839
  _globals['_EVENTERC20DEPLOYEDCLAIM']._serialized_start=1842
  _globals['_EVENTERC20DEPLOYEDCLAIM']._serialized_end=2058
  _globals['_EVENTVALSETUPDATECLAIM']._serialized_start=2061
  _globals['_EVENTVALSETUPDATECLAIM']._serialized_end=2341
  _globals['_EVENTCANCELSENDTOETH']._serialized_start=2343
  _globals['_EVENTCANCELSENDTOETH']._serialized_end=2389
  _globals['_EVENTSUBMITBADSIGNATUREEVIDENCE']._serialized_start=2391
  _globals['_EVENTSUBMITBADSIGNATUREEVIDENCE']._serialized_end=2486
  _globals['_EVENTVALIDATORSLASH']._serialized_start=2488
  _globals['_EVENTVALIDATORSLASH']._serialized_end=2610
# @@protoc_insertion_point(module_scope)
