# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from pyinjective.proto.exchange import injective_insurance_rpc_pb2 as exchange_dot_injective__insurance__rpc__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in exchange/injective_insurance_rpc_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class InjectiveInsuranceRPCStub(object):
    """InjectiveInsuranceRPC defines gRPC API of Insurance provider.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Funds = channel.unary_unary(
                '/injective_insurance_rpc.InjectiveInsuranceRPC/Funds',
                request_serializer=exchange_dot_injective__insurance__rpc__pb2.FundsRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__insurance__rpc__pb2.FundsResponse.FromString,
                _registered_method=True)
        self.Fund = channel.unary_unary(
                '/injective_insurance_rpc.InjectiveInsuranceRPC/Fund',
                request_serializer=exchange_dot_injective__insurance__rpc__pb2.FundRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__insurance__rpc__pb2.FundResponse.FromString,
                _registered_method=True)
        self.Redemptions = channel.unary_unary(
                '/injective_insurance_rpc.InjectiveInsuranceRPC/Redemptions',
                request_serializer=exchange_dot_injective__insurance__rpc__pb2.RedemptionsRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__insurance__rpc__pb2.RedemptionsResponse.FromString,
                _registered_method=True)


class InjectiveInsuranceRPCServicer(object):
    """InjectiveInsuranceRPC defines gRPC API of Insurance provider.
    """

    def Funds(self, request, context):
        """Funds lists all insurance funds.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Fund(self, request, context):
        """Funds returns an insurance fund for a given insurance fund token denom.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Redemptions(self, request, context):
        """PendingRedemptions lists all pending redemptions according to a filter
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InjectiveInsuranceRPCServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Funds': grpc.unary_unary_rpc_method_handler(
                    servicer.Funds,
                    request_deserializer=exchange_dot_injective__insurance__rpc__pb2.FundsRequest.FromString,
                    response_serializer=exchange_dot_injective__insurance__rpc__pb2.FundsResponse.SerializeToString,
            ),
            'Fund': grpc.unary_unary_rpc_method_handler(
                    servicer.Fund,
                    request_deserializer=exchange_dot_injective__insurance__rpc__pb2.FundRequest.FromString,
                    response_serializer=exchange_dot_injective__insurance__rpc__pb2.FundResponse.SerializeToString,
            ),
            'Redemptions': grpc.unary_unary_rpc_method_handler(
                    servicer.Redemptions,
                    request_deserializer=exchange_dot_injective__insurance__rpc__pb2.RedemptionsRequest.FromString,
                    response_serializer=exchange_dot_injective__insurance__rpc__pb2.RedemptionsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'injective_insurance_rpc.InjectiveInsuranceRPC', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('injective_insurance_rpc.InjectiveInsuranceRPC', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class InjectiveInsuranceRPC(object):
    """InjectiveInsuranceRPC defines gRPC API of Insurance provider.
    """

    @staticmethod
    def Funds(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/injective_insurance_rpc.InjectiveInsuranceRPC/Funds',
            exchange_dot_injective__insurance__rpc__pb2.FundsRequest.SerializeToString,
            exchange_dot_injective__insurance__rpc__pb2.FundsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Fund(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/injective_insurance_rpc.InjectiveInsuranceRPC/Fund',
            exchange_dot_injective__insurance__rpc__pb2.FundRequest.SerializeToString,
            exchange_dot_injective__insurance__rpc__pb2.FundResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Redemptions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/injective_insurance_rpc.InjectiveInsuranceRPC/Redemptions',
            exchange_dot_injective__insurance__rpc__pb2.RedemptionsRequest.SerializeToString,
            exchange_dot_injective__insurance__rpc__pb2.RedemptionsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
