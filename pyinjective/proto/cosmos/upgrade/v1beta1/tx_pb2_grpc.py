# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from pyinjective.proto.cosmos.upgrade.v1beta1 import tx_pb2 as cosmos_dot_upgrade_dot_v1beta1_dot_tx__pb2


class MsgStub(object):
    """Msg defines the upgrade Msg service."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SoftwareUpgrade = channel.unary_unary(
            "/cosmos.upgrade.v1beta1.Msg/SoftwareUpgrade",
            request_serializer=cosmos_dot_upgrade_dot_v1beta1_dot_tx__pb2.MsgSoftwareUpgrade.SerializeToString,
            response_deserializer=cosmos_dot_upgrade_dot_v1beta1_dot_tx__pb2.MsgSoftwareUpgradeResponse.FromString,
            _registered_method=True,
        )
        self.CancelUpgrade = channel.unary_unary(
            "/cosmos.upgrade.v1beta1.Msg/CancelUpgrade",
            request_serializer=cosmos_dot_upgrade_dot_v1beta1_dot_tx__pb2.MsgCancelUpgrade.SerializeToString,
            response_deserializer=cosmos_dot_upgrade_dot_v1beta1_dot_tx__pb2.MsgCancelUpgradeResponse.FromString,
            _registered_method=True,
        )


class MsgServicer(object):
    """Msg defines the upgrade Msg service."""

    def SoftwareUpgrade(self, request, context):
        """SoftwareUpgrade is a governance operation for initiating a software upgrade.

        Since: cosmos-sdk 0.46
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CancelUpgrade(self, request, context):
        """CancelUpgrade is a governance operation for cancelling a previously
        approved software upgrade.

        Since: cosmos-sdk 0.46
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "SoftwareUpgrade": grpc.unary_unary_rpc_method_handler(
            servicer.SoftwareUpgrade,
            request_deserializer=cosmos_dot_upgrade_dot_v1beta1_dot_tx__pb2.MsgSoftwareUpgrade.FromString,
            response_serializer=cosmos_dot_upgrade_dot_v1beta1_dot_tx__pb2.MsgSoftwareUpgradeResponse.SerializeToString,
        ),
        "CancelUpgrade": grpc.unary_unary_rpc_method_handler(
            servicer.CancelUpgrade,
            request_deserializer=cosmos_dot_upgrade_dot_v1beta1_dot_tx__pb2.MsgCancelUpgrade.FromString,
            response_serializer=cosmos_dot_upgrade_dot_v1beta1_dot_tx__pb2.MsgCancelUpgradeResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler("cosmos.upgrade.v1beta1.Msg", rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers("cosmos.upgrade.v1beta1.Msg", rpc_method_handlers)


# This class is part of an EXPERIMENTAL API.
class Msg(object):
    """Msg defines the upgrade Msg service."""

    @staticmethod
    def SoftwareUpgrade(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/cosmos.upgrade.v1beta1.Msg/SoftwareUpgrade",
            cosmos_dot_upgrade_dot_v1beta1_dot_tx__pb2.MsgSoftwareUpgrade.SerializeToString,
            cosmos_dot_upgrade_dot_v1beta1_dot_tx__pb2.MsgSoftwareUpgradeResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def CancelUpgrade(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/cosmos.upgrade.v1beta1.Msg/CancelUpgrade",
            cosmos_dot_upgrade_dot_v1beta1_dot_tx__pb2.MsgCancelUpgrade.SerializeToString,
            cosmos_dot_upgrade_dot_v1beta1_dot_tx__pb2.MsgCancelUpgradeResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )
