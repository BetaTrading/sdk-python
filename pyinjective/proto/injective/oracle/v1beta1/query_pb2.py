# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/oracle/v1beta1/query.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from pyinjective.proto.injective.oracle.v1beta1 import oracle_pb2 as injective_dot_oracle_dot_v1beta1_dot_oracle__pb2
from pyinjective.proto.injective.oracle.v1beta1 import genesis_pb2 as injective_dot_oracle_dot_v1beta1_dot_genesis__pb2
from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$injective/oracle/v1beta1/query.proto\x12\x18injective.oracle.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a%injective/oracle/v1beta1/oracle.proto\x1a&injective/oracle/v1beta1/genesis.proto\x1a\x14gogoproto/gogo.proto\")\n\x15QueryPythPriceRequest\x12\x10\n\x08price_id\x18\x01 \x01(\t\"W\n\x16QueryPythPriceResponse\x12=\n\x0bprice_state\x18\x01 \x01(\x0b\x32(.injective.oracle.v1beta1.PythPriceState\"\x14\n\x12QueryParamsRequest\"M\n\x13QueryParamsResponse\x12\x36\n\x06params\x18\x01 \x01(\x0b\x32 .injective.oracle.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\"\x1a\n\x18QueryBandRelayersRequest\"-\n\x19QueryBandRelayersResponse\x12\x10\n\x08relayers\x18\x01 \x03(\t\"\x1d\n\x1bQueryBandPriceStatesRequest\"^\n\x1cQueryBandPriceStatesResponse\x12>\n\x0cprice_states\x18\x01 \x03(\x0b\x32(.injective.oracle.v1beta1.BandPriceState\" \n\x1eQueryBandIBCPriceStatesRequest\"a\n\x1fQueryBandIBCPriceStatesResponse\x12>\n\x0cprice_states\x18\x01 \x03(\x0b\x32(.injective.oracle.v1beta1.BandPriceState\"\"\n QueryPriceFeedPriceStatesRequest\"c\n!QueryPriceFeedPriceStatesResponse\x12>\n\x0cprice_states\x18\x01 \x03(\x0b\x32(.injective.oracle.v1beta1.PriceFeedState\"!\n\x1fQueryCoinbasePriceStatesRequest\"f\n QueryCoinbasePriceStatesResponse\x12\x42\n\x0cprice_states\x18\x01 \x03(\x0b\x32,.injective.oracle.v1beta1.CoinbasePriceState\"\x1d\n\x1bQueryPythPriceStatesRequest\"^\n\x1cQueryPythPriceStatesResponse\x12>\n\x0cprice_states\x18\x01 \x03(\x0b\x32(.injective.oracle.v1beta1.PythPriceState\"B\n\x1eQueryProviderPriceStateRequest\x12\x10\n\x08provider\x18\x01 \x01(\t\x12\x0e\n\x06symbol\x18\x02 \x01(\t\"\\\n\x1fQueryProviderPriceStateResponse\x12\x39\n\x0bprice_state\x18\x01 \x01(\x0b\x32$.injective.oracle.v1beta1.PriceState\"\x19\n\x17QueryModuleStateRequest\"Q\n\x18QueryModuleStateResponse\x12\x35\n\x05state\x18\x01 \x01(\x0b\x32&.injective.oracle.v1beta1.GenesisState\"m\n\"QueryHistoricalPriceRecordsRequest\x12\x34\n\x06oracle\x18\x01 \x01(\x0e\x32$.injective.oracle.v1beta1.OracleType\x12\x11\n\tsymbol_id\x18\x02 \x01(\t\"d\n#QueryHistoricalPriceRecordsResponse\x12=\n\rprice_records\x18\x01 \x03(\x0b\x32&.injective.oracle.v1beta1.PriceRecords\"^\n\x14OracleHistoryOptions\x12\x0f\n\x07max_age\x18\x01 \x01(\x04\x12\x1b\n\x13include_raw_history\x18\x02 \x01(\x08\x12\x18\n\x10include_metadata\x18\x03 \x01(\x08\"\xe1\x01\n\x1cQueryOracleVolatilityRequest\x12\x37\n\tbase_info\x18\x01 \x01(\x0b\x32$.injective.oracle.v1beta1.OracleInfo\x12\x38\n\nquote_info\x18\x02 \x01(\x0b\x32$.injective.oracle.v1beta1.OracleInfo\x12N\n\x16oracle_history_options\x18\x03 \x01(\x0b\x32..injective.oracle.v1beta1.OracleHistoryOptions\"\xd8\x01\n\x1dQueryOracleVolatilityResponse\x12\x33\n\nvolatility\x18\x01 \x01(\tB\x1f\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\x12\x46\n\x10history_metadata\x18\x02 \x01(\x0b\x32,.injective.oracle.v1beta1.MetadataStatistics\x12:\n\x0braw_history\x18\x03 \x03(\x0b\x32%.injective.oracle.v1beta1.PriceRecord\"!\n\x1fQueryOracleProvidersInfoRequest\"]\n QueryOracleProvidersInfoResponse\x12\x39\n\tproviders\x18\x01 \x03(\x0b\x32&.injective.oracle.v1beta1.ProviderInfo\"4\n QueryOracleProviderPricesRequest\x12\x10\n\x08provider\x18\x01 \x01(\t\"c\n!QueryOracleProviderPricesResponse\x12>\n\rproviderState\x18\x01 \x03(\x0b\x32\'.injective.oracle.v1beta1.ProviderState\"?\n\x0eScalingOptions\x12\x15\n\rbase_decimals\x18\x01 \x01(\r\x12\x16\n\x0equote_decimals\x18\x02 \x01(\r\"\xba\x01\n\x17QueryOraclePriceRequest\x12\x39\n\x0boracle_type\x18\x01 \x01(\x0e\x32$.injective.oracle.v1beta1.OracleType\x12\x0c\n\x04\x62\x61se\x18\x02 \x01(\t\x12\r\n\x05quote\x18\x03 \x01(\t\x12G\n\x0fscaling_options\x18\x04 \x01(\x0b\x32(.injective.oracle.v1beta1.ScalingOptionsB\x04\xc8\xde\x1f\x01\"\xf6\x02\n\x0ePricePairState\x12\x37\n\npair_price\x18\x01 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\x12\x37\n\nbase_price\x18\x02 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\x12\x38\n\x0bquote_price\x18\x03 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\x12\x42\n\x15\x62\x61se_cumulative_price\x18\x04 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\x12\x43\n\x16quote_cumulative_price\x18\x05 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\x12\x16\n\x0e\x62\x61se_timestamp\x18\x06 \x01(\x03\x12\x17\n\x0fquote_timestamp\x18\x07 \x01(\x03\"^\n\x18QueryOraclePriceResponse\x12\x42\n\x10price_pair_state\x18\x01 \x01(\x0b\x32(.injective.oracle.v1beta1.PricePairState2\xda\x15\n\x05Query\x12\x8f\x01\n\x06Params\x12,.injective.oracle.v1beta1.QueryParamsRequest\x1a-.injective.oracle.v1beta1.QueryParamsResponse\"(\x82\xd3\xe4\x93\x02\"\x12 /injective/oracle/v1beta1/params\x12\xa8\x01\n\x0c\x42\x61ndRelayers\x12\x32.injective.oracle.v1beta1.QueryBandRelayersRequest\x1a\x33.injective.oracle.v1beta1.QueryBandRelayersResponse\"/\x82\xd3\xe4\x93\x02)\x12\'/injective/oracle/v1beta1/band_relayers\x12\xb5\x01\n\x0f\x42\x61ndPriceStates\x12\x35.injective.oracle.v1beta1.QueryBandPriceStatesRequest\x1a\x36.injective.oracle.v1beta1.QueryBandPriceStatesResponse\"3\x82\xd3\xe4\x93\x02-\x12+/injective/oracle/v1beta1/band_price_states\x12\xc2\x01\n\x12\x42\x61ndIBCPriceStates\x12\x38.injective.oracle.v1beta1.QueryBandIBCPriceStatesRequest\x1a\x39.injective.oracle.v1beta1.QueryBandIBCPriceStatesResponse\"7\x82\xd3\xe4\x93\x02\x31\x12//injective/oracle/v1beta1/band_ibc_price_states\x12\xc9\x01\n\x14PriceFeedPriceStates\x12:.injective.oracle.v1beta1.QueryPriceFeedPriceStatesRequest\x1a;.injective.oracle.v1beta1.QueryPriceFeedPriceStatesResponse\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/injective/oracle/v1beta1/pricefeed_price_states\x12\xc5\x01\n\x13\x43oinbasePriceStates\x12\x39.injective.oracle.v1beta1.QueryCoinbasePriceStatesRequest\x1a:.injective.oracle.v1beta1.QueryCoinbasePriceStatesResponse\"7\x82\xd3\xe4\x93\x02\x31\x12//injective/oracle/v1beta1/coinbase_price_states\x12\xb5\x01\n\x0fPythPriceStates\x12\x35.injective.oracle.v1beta1.QueryPythPriceStatesRequest\x1a\x36.injective.oracle.v1beta1.QueryPythPriceStatesResponse\"3\x82\xd3\xe4\x93\x02-\x12+/injective/oracle/v1beta1/pyth_price_states\x12\xd5\x01\n\x12ProviderPriceState\x12\x38.injective.oracle.v1beta1.QueryProviderPriceStateRequest\x1a\x39.injective.oracle.v1beta1.QueryProviderPriceStateResponse\"J\x82\xd3\xe4\x93\x02\x44\x12\x42/injective/oracle/v1beta1/provider_price_state/{provider}/{symbol}\x12\xaa\x01\n\x11OracleModuleState\x12\x31.injective.oracle.v1beta1.QueryModuleStateRequest\x1a\x32.injective.oracle.v1beta1.QueryModuleStateResponse\".\x82\xd3\xe4\x93\x02(\x12&/injective/oracle/v1beta1/module_state\x12\xd1\x01\n\x16HistoricalPriceRecords\x12<.injective.oracle.v1beta1.QueryHistoricalPriceRecordsRequest\x1a=.injective.oracle.v1beta1.QueryHistoricalPriceRecordsResponse\":\x82\xd3\xe4\x93\x02\x34\x12\x32/injective/oracle/v1beta1/historical_price_records\x12\xb1\x01\n\x10OracleVolatility\x12\x36.injective.oracle.v1beta1.QueryOracleVolatilityRequest\x1a\x37.injective.oracle.v1beta1.QueryOracleVolatilityResponse\",\x82\xd3\xe4\x93\x02&\x12$/injective/oracle/v1beta1/volatility\x12\xb9\x01\n\x13OracleProvidersInfo\x12\x39.injective.oracle.v1beta1.QueryOracleProvidersInfoRequest\x1a:.injective.oracle.v1beta1.QueryOracleProvidersInfoResponse\"+\x82\xd3\xe4\x93\x02%\x12#/injective/oracle/v1beta1/providers\x12\xc2\x01\n\x14OracleProviderPrices\x12:.injective.oracle.v1beta1.QueryOracleProviderPricesRequest\x1a;.injective.oracle.v1beta1.QueryOracleProviderPricesResponse\"1\x82\xd3\xe4\x93\x02+\x12)/injective/oracle/v1beta1/provider_prices\x12\x9d\x01\n\x0bOraclePrice\x12\x31.injective.oracle.v1beta1.QueryOraclePriceRequest\x1a\x32.injective.oracle.v1beta1.QueryOraclePriceResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/injective/oracle/v1beta1/price\x12\x9c\x01\n\tPythPrice\x12/.injective.oracle.v1beta1.QueryPythPriceRequest\x1a\x30.injective.oracle.v1beta1.QueryPythPriceResponse\",\x82\xd3\xe4\x93\x02&\x12$/injective/oracle/v1beta1/pyth_priceBNZLgithub.com/InjectiveLabs/injective-core/injective-chain/modules/oracle/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.oracle.v1beta1.query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZLgithub.com/InjectiveLabs/injective-core/injective-chain/modules/oracle/types'
  _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._loaded_options = None
  _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYORACLEVOLATILITYRESPONSE'].fields_by_name['volatility']._loaded_options = None
  _globals['_QUERYORACLEVOLATILITYRESPONSE'].fields_by_name['volatility']._serialized_options = b'\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_QUERYORACLEPRICEREQUEST'].fields_by_name['scaling_options']._loaded_options = None
  _globals['_QUERYORACLEPRICEREQUEST'].fields_by_name['scaling_options']._serialized_options = b'\310\336\037\001'
  _globals['_PRICEPAIRSTATE'].fields_by_name['pair_price']._loaded_options = None
  _globals['_PRICEPAIRSTATE'].fields_by_name['pair_price']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_PRICEPAIRSTATE'].fields_by_name['base_price']._loaded_options = None
  _globals['_PRICEPAIRSTATE'].fields_by_name['base_price']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_PRICEPAIRSTATE'].fields_by_name['quote_price']._loaded_options = None
  _globals['_PRICEPAIRSTATE'].fields_by_name['quote_price']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_PRICEPAIRSTATE'].fields_by_name['base_cumulative_price']._loaded_options = None
  _globals['_PRICEPAIRSTATE'].fields_by_name['base_cumulative_price']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_PRICEPAIRSTATE'].fields_by_name['quote_cumulative_price']._loaded_options = None
  _globals['_PRICEPAIRSTATE'].fields_by_name['quote_cumulative_price']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec'
  _globals['_QUERY'].methods_by_name['Params']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Params']._serialized_options = b'\202\323\344\223\002\"\022 /injective/oracle/v1beta1/params'
  _globals['_QUERY'].methods_by_name['BandRelayers']._loaded_options = None
  _globals['_QUERY'].methods_by_name['BandRelayers']._serialized_options = b'\202\323\344\223\002)\022\'/injective/oracle/v1beta1/band_relayers'
  _globals['_QUERY'].methods_by_name['BandPriceStates']._loaded_options = None
  _globals['_QUERY'].methods_by_name['BandPriceStates']._serialized_options = b'\202\323\344\223\002-\022+/injective/oracle/v1beta1/band_price_states'
  _globals['_QUERY'].methods_by_name['BandIBCPriceStates']._loaded_options = None
  _globals['_QUERY'].methods_by_name['BandIBCPriceStates']._serialized_options = b'\202\323\344\223\0021\022//injective/oracle/v1beta1/band_ibc_price_states'
  _globals['_QUERY'].methods_by_name['PriceFeedPriceStates']._loaded_options = None
  _globals['_QUERY'].methods_by_name['PriceFeedPriceStates']._serialized_options = b'\202\323\344\223\0022\0220/injective/oracle/v1beta1/pricefeed_price_states'
  _globals['_QUERY'].methods_by_name['CoinbasePriceStates']._loaded_options = None
  _globals['_QUERY'].methods_by_name['CoinbasePriceStates']._serialized_options = b'\202\323\344\223\0021\022//injective/oracle/v1beta1/coinbase_price_states'
  _globals['_QUERY'].methods_by_name['PythPriceStates']._loaded_options = None
  _globals['_QUERY'].methods_by_name['PythPriceStates']._serialized_options = b'\202\323\344\223\002-\022+/injective/oracle/v1beta1/pyth_price_states'
  _globals['_QUERY'].methods_by_name['ProviderPriceState']._loaded_options = None
  _globals['_QUERY'].methods_by_name['ProviderPriceState']._serialized_options = b'\202\323\344\223\002D\022B/injective/oracle/v1beta1/provider_price_state/{provider}/{symbol}'
  _globals['_QUERY'].methods_by_name['OracleModuleState']._loaded_options = None
  _globals['_QUERY'].methods_by_name['OracleModuleState']._serialized_options = b'\202\323\344\223\002(\022&/injective/oracle/v1beta1/module_state'
  _globals['_QUERY'].methods_by_name['HistoricalPriceRecords']._loaded_options = None
  _globals['_QUERY'].methods_by_name['HistoricalPriceRecords']._serialized_options = b'\202\323\344\223\0024\0222/injective/oracle/v1beta1/historical_price_records'
  _globals['_QUERY'].methods_by_name['OracleVolatility']._loaded_options = None
  _globals['_QUERY'].methods_by_name['OracleVolatility']._serialized_options = b'\202\323\344\223\002&\022$/injective/oracle/v1beta1/volatility'
  _globals['_QUERY'].methods_by_name['OracleProvidersInfo']._loaded_options = None
  _globals['_QUERY'].methods_by_name['OracleProvidersInfo']._serialized_options = b'\202\323\344\223\002%\022#/injective/oracle/v1beta1/providers'
  _globals['_QUERY'].methods_by_name['OracleProviderPrices']._loaded_options = None
  _globals['_QUERY'].methods_by_name['OracleProviderPrices']._serialized_options = b'\202\323\344\223\002+\022)/injective/oracle/v1beta1/provider_prices'
  _globals['_QUERY'].methods_by_name['OraclePrice']._loaded_options = None
  _globals['_QUERY'].methods_by_name['OraclePrice']._serialized_options = b'\202\323\344\223\002!\022\037/injective/oracle/v1beta1/price'
  _globals['_QUERY'].methods_by_name['PythPrice']._loaded_options = None
  _globals['_QUERY'].methods_by_name['PythPrice']._serialized_options = b'\202\323\344\223\002&\022$/injective/oracle/v1beta1/pyth_price'
  _globals['_QUERYPYTHPRICEREQUEST']._serialized_start=197
  _globals['_QUERYPYTHPRICEREQUEST']._serialized_end=238
  _globals['_QUERYPYTHPRICERESPONSE']._serialized_start=240
  _globals['_QUERYPYTHPRICERESPONSE']._serialized_end=327
  _globals['_QUERYPARAMSREQUEST']._serialized_start=329
  _globals['_QUERYPARAMSREQUEST']._serialized_end=349
  _globals['_QUERYPARAMSRESPONSE']._serialized_start=351
  _globals['_QUERYPARAMSRESPONSE']._serialized_end=428
  _globals['_QUERYBANDRELAYERSREQUEST']._serialized_start=430
  _globals['_QUERYBANDRELAYERSREQUEST']._serialized_end=456
  _globals['_QUERYBANDRELAYERSRESPONSE']._serialized_start=458
  _globals['_QUERYBANDRELAYERSRESPONSE']._serialized_end=503
  _globals['_QUERYBANDPRICESTATESREQUEST']._serialized_start=505
  _globals['_QUERYBANDPRICESTATESREQUEST']._serialized_end=534
  _globals['_QUERYBANDPRICESTATESRESPONSE']._serialized_start=536
  _globals['_QUERYBANDPRICESTATESRESPONSE']._serialized_end=630
  _globals['_QUERYBANDIBCPRICESTATESREQUEST']._serialized_start=632
  _globals['_QUERYBANDIBCPRICESTATESREQUEST']._serialized_end=664
  _globals['_QUERYBANDIBCPRICESTATESRESPONSE']._serialized_start=666
  _globals['_QUERYBANDIBCPRICESTATESRESPONSE']._serialized_end=763
  _globals['_QUERYPRICEFEEDPRICESTATESREQUEST']._serialized_start=765
  _globals['_QUERYPRICEFEEDPRICESTATESREQUEST']._serialized_end=799
  _globals['_QUERYPRICEFEEDPRICESTATESRESPONSE']._serialized_start=801
  _globals['_QUERYPRICEFEEDPRICESTATESRESPONSE']._serialized_end=900
  _globals['_QUERYCOINBASEPRICESTATESREQUEST']._serialized_start=902
  _globals['_QUERYCOINBASEPRICESTATESREQUEST']._serialized_end=935
  _globals['_QUERYCOINBASEPRICESTATESRESPONSE']._serialized_start=937
  _globals['_QUERYCOINBASEPRICESTATESRESPONSE']._serialized_end=1039
  _globals['_QUERYPYTHPRICESTATESREQUEST']._serialized_start=1041
  _globals['_QUERYPYTHPRICESTATESREQUEST']._serialized_end=1070
  _globals['_QUERYPYTHPRICESTATESRESPONSE']._serialized_start=1072
  _globals['_QUERYPYTHPRICESTATESRESPONSE']._serialized_end=1166
  _globals['_QUERYPROVIDERPRICESTATEREQUEST']._serialized_start=1168
  _globals['_QUERYPROVIDERPRICESTATEREQUEST']._serialized_end=1234
  _globals['_QUERYPROVIDERPRICESTATERESPONSE']._serialized_start=1236
  _globals['_QUERYPROVIDERPRICESTATERESPONSE']._serialized_end=1328
  _globals['_QUERYMODULESTATEREQUEST']._serialized_start=1330
  _globals['_QUERYMODULESTATEREQUEST']._serialized_end=1355
  _globals['_QUERYMODULESTATERESPONSE']._serialized_start=1357
  _globals['_QUERYMODULESTATERESPONSE']._serialized_end=1438
  _globals['_QUERYHISTORICALPRICERECORDSREQUEST']._serialized_start=1440
  _globals['_QUERYHISTORICALPRICERECORDSREQUEST']._serialized_end=1549
  _globals['_QUERYHISTORICALPRICERECORDSRESPONSE']._serialized_start=1551
  _globals['_QUERYHISTORICALPRICERECORDSRESPONSE']._serialized_end=1651
  _globals['_ORACLEHISTORYOPTIONS']._serialized_start=1653
  _globals['_ORACLEHISTORYOPTIONS']._serialized_end=1747
  _globals['_QUERYORACLEVOLATILITYREQUEST']._serialized_start=1750
  _globals['_QUERYORACLEVOLATILITYREQUEST']._serialized_end=1975
  _globals['_QUERYORACLEVOLATILITYRESPONSE']._serialized_start=1978
  _globals['_QUERYORACLEVOLATILITYRESPONSE']._serialized_end=2194
  _globals['_QUERYORACLEPROVIDERSINFOREQUEST']._serialized_start=2196
  _globals['_QUERYORACLEPROVIDERSINFOREQUEST']._serialized_end=2229
  _globals['_QUERYORACLEPROVIDERSINFORESPONSE']._serialized_start=2231
  _globals['_QUERYORACLEPROVIDERSINFORESPONSE']._serialized_end=2324
  _globals['_QUERYORACLEPROVIDERPRICESREQUEST']._serialized_start=2326
  _globals['_QUERYORACLEPROVIDERPRICESREQUEST']._serialized_end=2378
  _globals['_QUERYORACLEPROVIDERPRICESRESPONSE']._serialized_start=2380
  _globals['_QUERYORACLEPROVIDERPRICESRESPONSE']._serialized_end=2479
  _globals['_SCALINGOPTIONS']._serialized_start=2481
  _globals['_SCALINGOPTIONS']._serialized_end=2544
  _globals['_QUERYORACLEPRICEREQUEST']._serialized_start=2547
  _globals['_QUERYORACLEPRICEREQUEST']._serialized_end=2733
  _globals['_PRICEPAIRSTATE']._serialized_start=2736
  _globals['_PRICEPAIRSTATE']._serialized_end=3110
  _globals['_QUERYORACLEPRICERESPONSE']._serialized_start=3112
  _globals['_QUERYORACLEPRICERESPONSE']._serialized_end=3206
  _globals['_QUERY']._serialized_start=3209
  _globals['_QUERY']._serialized_end=5987
# @@protoc_insertion_point(module_scope)
