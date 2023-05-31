# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from injective.peggy.v1 import query_pb2 as injective_dot_peggy_dot_v1_dot_query__pb2


class QueryStub(object):
    """Query defines the gRPC querier service
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Params = channel.unary_unary(
                '/injective.peggy.v1.Query/Params',
                request_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryParamsRequest.SerializeToString,
                response_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryParamsResponse.FromString,
                )
        self.CurrentValset = channel.unary_unary(
                '/injective.peggy.v1.Query/CurrentValset',
                request_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryCurrentValsetRequest.SerializeToString,
                response_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryCurrentValsetResponse.FromString,
                )
        self.ValsetRequest = channel.unary_unary(
                '/injective.peggy.v1.Query/ValsetRequest',
                request_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryValsetRequestRequest.SerializeToString,
                response_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryValsetRequestResponse.FromString,
                )
        self.ValsetConfirm = channel.unary_unary(
                '/injective.peggy.v1.Query/ValsetConfirm',
                request_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryValsetConfirmRequest.SerializeToString,
                response_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryValsetConfirmResponse.FromString,
                )
        self.ValsetConfirmsByNonce = channel.unary_unary(
                '/injective.peggy.v1.Query/ValsetConfirmsByNonce',
                request_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryValsetConfirmsByNonceRequest.SerializeToString,
                response_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryValsetConfirmsByNonceResponse.FromString,
                )
        self.LastValsetRequests = channel.unary_unary(
                '/injective.peggy.v1.Query/LastValsetRequests',
                request_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryLastValsetRequestsRequest.SerializeToString,
                response_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryLastValsetRequestsResponse.FromString,
                )
        self.LastPendingValsetRequestByAddr = channel.unary_unary(
                '/injective.peggy.v1.Query/LastPendingValsetRequestByAddr',
                request_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryLastPendingValsetRequestByAddrRequest.SerializeToString,
                response_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryLastPendingValsetRequestByAddrResponse.FromString,
                )
        self.LastEventByAddr = channel.unary_unary(
                '/injective.peggy.v1.Query/LastEventByAddr',
                request_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryLastEventByAddrRequest.SerializeToString,
                response_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryLastEventByAddrResponse.FromString,
                )
        self.GetPendingSendToEth = channel.unary_unary(
                '/injective.peggy.v1.Query/GetPendingSendToEth',
                request_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryPendingSendToEth.SerializeToString,
                response_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryPendingSendToEthResponse.FromString,
                )
        self.BatchFees = channel.unary_unary(
                '/injective.peggy.v1.Query/BatchFees',
                request_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryBatchFeeRequest.SerializeToString,
                response_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryBatchFeeResponse.FromString,
                )
        self.OutgoingTxBatches = channel.unary_unary(
                '/injective.peggy.v1.Query/OutgoingTxBatches',
                request_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryOutgoingTxBatchesRequest.SerializeToString,
                response_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryOutgoingTxBatchesResponse.FromString,
                )
        self.LastPendingBatchRequestByAddr = channel.unary_unary(
                '/injective.peggy.v1.Query/LastPendingBatchRequestByAddr',
                request_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryLastPendingBatchRequestByAddrRequest.SerializeToString,
                response_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryLastPendingBatchRequestByAddrResponse.FromString,
                )
        self.BatchRequestByNonce = channel.unary_unary(
                '/injective.peggy.v1.Query/BatchRequestByNonce',
                request_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryBatchRequestByNonceRequest.SerializeToString,
                response_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryBatchRequestByNonceResponse.FromString,
                )
        self.BatchConfirms = channel.unary_unary(
                '/injective.peggy.v1.Query/BatchConfirms',
                request_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryBatchConfirmsRequest.SerializeToString,
                response_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryBatchConfirmsResponse.FromString,
                )
        self.ERC20ToDenom = channel.unary_unary(
                '/injective.peggy.v1.Query/ERC20ToDenom',
                request_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryERC20ToDenomRequest.SerializeToString,
                response_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryERC20ToDenomResponse.FromString,
                )
        self.DenomToERC20 = channel.unary_unary(
                '/injective.peggy.v1.Query/DenomToERC20',
                request_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryDenomToERC20Request.SerializeToString,
                response_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryDenomToERC20Response.FromString,
                )
        self.GetDelegateKeyByValidator = channel.unary_unary(
                '/injective.peggy.v1.Query/GetDelegateKeyByValidator',
                request_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryDelegateKeysByValidatorAddress.SerializeToString,
                response_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryDelegateKeysByValidatorAddressResponse.FromString,
                )
        self.GetDelegateKeyByEth = channel.unary_unary(
                '/injective.peggy.v1.Query/GetDelegateKeyByEth',
                request_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryDelegateKeysByEthAddress.SerializeToString,
                response_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryDelegateKeysByEthAddressResponse.FromString,
                )
        self.GetDelegateKeyByOrchestrator = channel.unary_unary(
                '/injective.peggy.v1.Query/GetDelegateKeyByOrchestrator',
                request_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryDelegateKeysByOrchestratorAddress.SerializeToString,
                response_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryDelegateKeysByOrchestratorAddressResponse.FromString,
                )
        self.PeggyModuleState = channel.unary_unary(
                '/injective.peggy.v1.Query/PeggyModuleState',
                request_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryModuleStateRequest.SerializeToString,
                response_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryModuleStateResponse.FromString,
                )
        self.MissingPeggoNonces = channel.unary_unary(
                '/injective.peggy.v1.Query/MissingPeggoNonces',
                request_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.MissingNoncesRequest.SerializeToString,
                response_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.MissingNoncesResponse.FromString,
                )


class QueryServicer(object):
    """Query defines the gRPC querier service
    """

    def Params(self, request, context):
        """Deployments queries deployments
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CurrentValset(self, request, context):
        """valset
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ValsetRequest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ValsetConfirm(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ValsetConfirmsByNonce(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LastValsetRequests(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LastPendingValsetRequestByAddr(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LastEventByAddr(self, request, context):
        """claim
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPendingSendToEth(self, request, context):
        """batch
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchFees(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OutgoingTxBatches(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LastPendingBatchRequestByAddr(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchRequestByNonce(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchConfirms(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ERC20ToDenom(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DenomToERC20(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDelegateKeyByValidator(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDelegateKeyByEth(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDelegateKeyByOrchestrator(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PeggyModuleState(self, request, context):
        """Retrieves the entire peggy module's state
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MissingPeggoNonces(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Params': grpc.unary_unary_rpc_method_handler(
                    servicer.Params,
                    request_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryParamsRequest.FromString,
                    response_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryParamsResponse.SerializeToString,
            ),
            'CurrentValset': grpc.unary_unary_rpc_method_handler(
                    servicer.CurrentValset,
                    request_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryCurrentValsetRequest.FromString,
                    response_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryCurrentValsetResponse.SerializeToString,
            ),
            'ValsetRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.ValsetRequest,
                    request_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryValsetRequestRequest.FromString,
                    response_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryValsetRequestResponse.SerializeToString,
            ),
            'ValsetConfirm': grpc.unary_unary_rpc_method_handler(
                    servicer.ValsetConfirm,
                    request_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryValsetConfirmRequest.FromString,
                    response_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryValsetConfirmResponse.SerializeToString,
            ),
            'ValsetConfirmsByNonce': grpc.unary_unary_rpc_method_handler(
                    servicer.ValsetConfirmsByNonce,
                    request_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryValsetConfirmsByNonceRequest.FromString,
                    response_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryValsetConfirmsByNonceResponse.SerializeToString,
            ),
            'LastValsetRequests': grpc.unary_unary_rpc_method_handler(
                    servicer.LastValsetRequests,
                    request_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryLastValsetRequestsRequest.FromString,
                    response_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryLastValsetRequestsResponse.SerializeToString,
            ),
            'LastPendingValsetRequestByAddr': grpc.unary_unary_rpc_method_handler(
                    servicer.LastPendingValsetRequestByAddr,
                    request_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryLastPendingValsetRequestByAddrRequest.FromString,
                    response_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryLastPendingValsetRequestByAddrResponse.SerializeToString,
            ),
            'LastEventByAddr': grpc.unary_unary_rpc_method_handler(
                    servicer.LastEventByAddr,
                    request_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryLastEventByAddrRequest.FromString,
                    response_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryLastEventByAddrResponse.SerializeToString,
            ),
            'GetPendingSendToEth': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPendingSendToEth,
                    request_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryPendingSendToEth.FromString,
                    response_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryPendingSendToEthResponse.SerializeToString,
            ),
            'BatchFees': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchFees,
                    request_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryBatchFeeRequest.FromString,
                    response_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryBatchFeeResponse.SerializeToString,
            ),
            'OutgoingTxBatches': grpc.unary_unary_rpc_method_handler(
                    servicer.OutgoingTxBatches,
                    request_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryOutgoingTxBatchesRequest.FromString,
                    response_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryOutgoingTxBatchesResponse.SerializeToString,
            ),
            'LastPendingBatchRequestByAddr': grpc.unary_unary_rpc_method_handler(
                    servicer.LastPendingBatchRequestByAddr,
                    request_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryLastPendingBatchRequestByAddrRequest.FromString,
                    response_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryLastPendingBatchRequestByAddrResponse.SerializeToString,
            ),
            'BatchRequestByNonce': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchRequestByNonce,
                    request_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryBatchRequestByNonceRequest.FromString,
                    response_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryBatchRequestByNonceResponse.SerializeToString,
            ),
            'BatchConfirms': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchConfirms,
                    request_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryBatchConfirmsRequest.FromString,
                    response_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryBatchConfirmsResponse.SerializeToString,
            ),
            'ERC20ToDenom': grpc.unary_unary_rpc_method_handler(
                    servicer.ERC20ToDenom,
                    request_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryERC20ToDenomRequest.FromString,
                    response_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryERC20ToDenomResponse.SerializeToString,
            ),
            'DenomToERC20': grpc.unary_unary_rpc_method_handler(
                    servicer.DenomToERC20,
                    request_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryDenomToERC20Request.FromString,
                    response_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryDenomToERC20Response.SerializeToString,
            ),
            'GetDelegateKeyByValidator': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDelegateKeyByValidator,
                    request_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryDelegateKeysByValidatorAddress.FromString,
                    response_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryDelegateKeysByValidatorAddressResponse.SerializeToString,
            ),
            'GetDelegateKeyByEth': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDelegateKeyByEth,
                    request_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryDelegateKeysByEthAddress.FromString,
                    response_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryDelegateKeysByEthAddressResponse.SerializeToString,
            ),
            'GetDelegateKeyByOrchestrator': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDelegateKeyByOrchestrator,
                    request_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryDelegateKeysByOrchestratorAddress.FromString,
                    response_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryDelegateKeysByOrchestratorAddressResponse.SerializeToString,
            ),
            'PeggyModuleState': grpc.unary_unary_rpc_method_handler(
                    servicer.PeggyModuleState,
                    request_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryModuleStateRequest.FromString,
                    response_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.QueryModuleStateResponse.SerializeToString,
            ),
            'MissingPeggoNonces': grpc.unary_unary_rpc_method_handler(
                    servicer.MissingPeggoNonces,
                    request_deserializer=injective_dot_peggy_dot_v1_dot_query__pb2.MissingNoncesRequest.FromString,
                    response_serializer=injective_dot_peggy_dot_v1_dot_query__pb2.MissingNoncesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'injective.peggy.v1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Query(object):
    """Query defines the gRPC querier service
    """

    @staticmethod
    def Params(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.peggy.v1.Query/Params',
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryParamsRequest.SerializeToString,
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryParamsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CurrentValset(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.peggy.v1.Query/CurrentValset',
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryCurrentValsetRequest.SerializeToString,
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryCurrentValsetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ValsetRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.peggy.v1.Query/ValsetRequest',
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryValsetRequestRequest.SerializeToString,
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryValsetRequestResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ValsetConfirm(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.peggy.v1.Query/ValsetConfirm',
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryValsetConfirmRequest.SerializeToString,
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryValsetConfirmResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ValsetConfirmsByNonce(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.peggy.v1.Query/ValsetConfirmsByNonce',
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryValsetConfirmsByNonceRequest.SerializeToString,
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryValsetConfirmsByNonceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LastValsetRequests(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.peggy.v1.Query/LastValsetRequests',
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryLastValsetRequestsRequest.SerializeToString,
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryLastValsetRequestsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LastPendingValsetRequestByAddr(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.peggy.v1.Query/LastPendingValsetRequestByAddr',
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryLastPendingValsetRequestByAddrRequest.SerializeToString,
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryLastPendingValsetRequestByAddrResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LastEventByAddr(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.peggy.v1.Query/LastEventByAddr',
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryLastEventByAddrRequest.SerializeToString,
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryLastEventByAddrResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPendingSendToEth(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.peggy.v1.Query/GetPendingSendToEth',
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryPendingSendToEth.SerializeToString,
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryPendingSendToEthResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BatchFees(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.peggy.v1.Query/BatchFees',
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryBatchFeeRequest.SerializeToString,
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryBatchFeeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OutgoingTxBatches(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.peggy.v1.Query/OutgoingTxBatches',
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryOutgoingTxBatchesRequest.SerializeToString,
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryOutgoingTxBatchesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LastPendingBatchRequestByAddr(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.peggy.v1.Query/LastPendingBatchRequestByAddr',
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryLastPendingBatchRequestByAddrRequest.SerializeToString,
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryLastPendingBatchRequestByAddrResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BatchRequestByNonce(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.peggy.v1.Query/BatchRequestByNonce',
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryBatchRequestByNonceRequest.SerializeToString,
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryBatchRequestByNonceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BatchConfirms(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.peggy.v1.Query/BatchConfirms',
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryBatchConfirmsRequest.SerializeToString,
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryBatchConfirmsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ERC20ToDenom(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.peggy.v1.Query/ERC20ToDenom',
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryERC20ToDenomRequest.SerializeToString,
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryERC20ToDenomResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DenomToERC20(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.peggy.v1.Query/DenomToERC20',
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryDenomToERC20Request.SerializeToString,
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryDenomToERC20Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDelegateKeyByValidator(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.peggy.v1.Query/GetDelegateKeyByValidator',
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryDelegateKeysByValidatorAddress.SerializeToString,
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryDelegateKeysByValidatorAddressResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDelegateKeyByEth(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.peggy.v1.Query/GetDelegateKeyByEth',
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryDelegateKeysByEthAddress.SerializeToString,
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryDelegateKeysByEthAddressResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDelegateKeyByOrchestrator(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.peggy.v1.Query/GetDelegateKeyByOrchestrator',
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryDelegateKeysByOrchestratorAddress.SerializeToString,
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryDelegateKeysByOrchestratorAddressResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PeggyModuleState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.peggy.v1.Query/PeggyModuleState',
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryModuleStateRequest.SerializeToString,
            injective_dot_peggy_dot_v1_dot_query__pb2.QueryModuleStateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MissingPeggoNonces(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.peggy.v1.Query/MissingPeggoNonces',
            injective_dot_peggy_dot_v1_dot_query__pb2.MissingNoncesRequest.SerializeToString,
            injective_dot_peggy_dot_v1_dot_query__pb2.MissingNoncesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
