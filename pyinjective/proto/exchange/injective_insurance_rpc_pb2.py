# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exchange/injective_insurance_rpc.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&exchange/injective_insurance_rpc.proto\x12\x17injective_insurance_rpc\"\x0e\n\x0c\x46undsRequest\"F\n\rFundsResponse\x12\x35\n\x05\x66unds\x18\x01 \x03(\x0b\x32&.injective_insurance_rpc.InsuranceFund\"\xcb\x02\n\rInsuranceFund\x12\x15\n\rmarket_ticker\x18\x01 \x01(\t\x12\x11\n\tmarket_id\x18\x02 \x01(\t\x12\x15\n\rdeposit_denom\x18\x03 \x01(\t\x12\x18\n\x10pool_token_denom\x18\x04 \x01(\t\x12)\n!redemption_notice_period_duration\x18\x05 \x01(\x12\x12\x0f\n\x07\x62\x61lance\x18\x06 \x01(\t\x12\x13\n\x0btotal_share\x18\x07 \x01(\t\x12\x13\n\x0boracle_base\x18\x08 \x01(\t\x12\x14\n\x0coracle_quote\x18\t \x01(\t\x12\x13\n\x0boracle_type\x18\n \x01(\t\x12\x0e\n\x06\x65xpiry\x18\x0b \x01(\x12\x12>\n\x12\x64\x65posit_token_meta\x18\x0c \x01(\x0b\x32\".injective_insurance_rpc.TokenMeta\"n\n\tTokenMeta\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x0e\n\x06symbol\x18\x03 \x01(\t\x12\x0c\n\x04logo\x18\x04 \x01(\t\x12\x10\n\x08\x64\x65\x63imals\x18\x05 \x01(\x11\x12\x12\n\nupdated_at\x18\x06 \x01(\x12\"P\n\x12RedemptionsRequest\x12\x10\n\x08redeemer\x18\x01 \x01(\t\x12\x18\n\x10redemption_denom\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\"`\n\x13RedemptionsResponse\x12I\n\x14redemption_schedules\x18\x01 \x03(\x0b\x32+.injective_insurance_rpc.RedemptionSchedule\"\x84\x02\n\x12RedemptionSchedule\x12\x15\n\rredemption_id\x18\x01 \x01(\x04\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\x10\n\x08redeemer\x18\x03 \x01(\t\x12!\n\x19\x63laimable_redemption_time\x18\x04 \x01(\x12\x12\x19\n\x11redemption_amount\x18\x05 \x01(\t\x12\x18\n\x10redemption_denom\x18\x06 \x01(\t\x12\x14\n\x0crequested_at\x18\x07 \x01(\x12\x12\x18\n\x10\x64isbursed_amount\x18\x08 \x01(\t\x12\x17\n\x0f\x64isbursed_denom\x18\t \x01(\t\x12\x14\n\x0c\x64isbursed_at\x18\n \x01(\x12\x32\xd9\x01\n\x15InjectiveInsuranceRPC\x12V\n\x05\x46unds\x12%.injective_insurance_rpc.FundsRequest\x1a&.injective_insurance_rpc.FundsResponse\x12h\n\x0bRedemptions\x12+.injective_insurance_rpc.RedemptionsRequest\x1a,.injective_insurance_rpc.RedemptionsResponseB\x1cZ\x1a/injective_insurance_rpcpbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'exchange.injective_insurance_rpc_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\032/injective_insurance_rpcpb'
  _globals['_FUNDSREQUEST']._serialized_start=67
  _globals['_FUNDSREQUEST']._serialized_end=81
  _globals['_FUNDSRESPONSE']._serialized_start=83
  _globals['_FUNDSRESPONSE']._serialized_end=153
  _globals['_INSURANCEFUND']._serialized_start=156
  _globals['_INSURANCEFUND']._serialized_end=487
  _globals['_TOKENMETA']._serialized_start=489
  _globals['_TOKENMETA']._serialized_end=599
  _globals['_REDEMPTIONSREQUEST']._serialized_start=601
  _globals['_REDEMPTIONSREQUEST']._serialized_end=681
  _globals['_REDEMPTIONSRESPONSE']._serialized_start=683
  _globals['_REDEMPTIONSRESPONSE']._serialized_end=779
  _globals['_REDEMPTIONSCHEDULE']._serialized_start=782
  _globals['_REDEMPTIONSCHEDULE']._serialized_end=1042
  _globals['_INJECTIVEINSURANCERPC']._serialized_start=1045
  _globals['_INJECTIVEINSURANCERPC']._serialized_end=1262
# @@protoc_insertion_point(module_scope)
