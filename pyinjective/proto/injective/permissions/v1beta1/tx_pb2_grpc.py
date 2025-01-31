# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from pyinjective.proto.injective.permissions.v1beta1 import tx_pb2 as injective_dot_permissions_dot_v1beta1_dot_tx__pb2


class MsgStub(object):
    """Msg defines the permissions module's gRPC message service."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UpdateParams = channel.unary_unary(
            "/injective.permissions.v1beta1.Msg/UpdateParams",
            request_serializer=injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgUpdateParams.SerializeToString,
            response_deserializer=injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgUpdateParamsResponse.FromString,
            _registered_method=True,
        )
        self.CreateNamespace = channel.unary_unary(
            "/injective.permissions.v1beta1.Msg/CreateNamespace",
            request_serializer=injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgCreateNamespace.SerializeToString,
            response_deserializer=injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgCreateNamespaceResponse.FromString,
            _registered_method=True,
        )
        self.DeleteNamespace = channel.unary_unary(
            "/injective.permissions.v1beta1.Msg/DeleteNamespace",
            request_serializer=injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgDeleteNamespace.SerializeToString,
            response_deserializer=injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgDeleteNamespaceResponse.FromString,
            _registered_method=True,
        )
        self.UpdateNamespace = channel.unary_unary(
            "/injective.permissions.v1beta1.Msg/UpdateNamespace",
            request_serializer=injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgUpdateNamespace.SerializeToString,
            response_deserializer=injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgUpdateNamespaceResponse.FromString,
            _registered_method=True,
        )
        self.UpdateNamespaceRoles = channel.unary_unary(
            "/injective.permissions.v1beta1.Msg/UpdateNamespaceRoles",
            request_serializer=injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgUpdateNamespaceRoles.SerializeToString,
            response_deserializer=injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgUpdateNamespaceRolesResponse.FromString,
            _registered_method=True,
        )
        self.RevokeNamespaceRoles = channel.unary_unary(
            "/injective.permissions.v1beta1.Msg/RevokeNamespaceRoles",
            request_serializer=injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgRevokeNamespaceRoles.SerializeToString,
            response_deserializer=injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgRevokeNamespaceRolesResponse.FromString,
            _registered_method=True,
        )
        self.ClaimVoucher = channel.unary_unary(
            "/injective.permissions.v1beta1.Msg/ClaimVoucher",
            request_serializer=injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgClaimVoucher.SerializeToString,
            response_deserializer=injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgClaimVoucherResponse.FromString,
            _registered_method=True,
        )


class MsgServicer(object):
    """Msg defines the permissions module's gRPC message service."""

    def UpdateParams(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CreateNamespace(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteNamespace(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateNamespace(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateNamespaceRoles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def RevokeNamespaceRoles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ClaimVoucher(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "UpdateParams": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateParams,
            request_deserializer=injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgUpdateParams.FromString,
            response_serializer=injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgUpdateParamsResponse.SerializeToString,
        ),
        "CreateNamespace": grpc.unary_unary_rpc_method_handler(
            servicer.CreateNamespace,
            request_deserializer=injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgCreateNamespace.FromString,
            response_serializer=injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgCreateNamespaceResponse.SerializeToString,
        ),
        "DeleteNamespace": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteNamespace,
            request_deserializer=injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgDeleteNamespace.FromString,
            response_serializer=injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgDeleteNamespaceResponse.SerializeToString,
        ),
        "UpdateNamespace": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateNamespace,
            request_deserializer=injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgUpdateNamespace.FromString,
            response_serializer=injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgUpdateNamespaceResponse.SerializeToString,
        ),
        "UpdateNamespaceRoles": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateNamespaceRoles,
            request_deserializer=injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgUpdateNamespaceRoles.FromString,
            response_serializer=injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgUpdateNamespaceRolesResponse.SerializeToString,
        ),
        "RevokeNamespaceRoles": grpc.unary_unary_rpc_method_handler(
            servicer.RevokeNamespaceRoles,
            request_deserializer=injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgRevokeNamespaceRoles.FromString,
            response_serializer=injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgRevokeNamespaceRolesResponse.SerializeToString,
        ),
        "ClaimVoucher": grpc.unary_unary_rpc_method_handler(
            servicer.ClaimVoucher,
            request_deserializer=injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgClaimVoucher.FromString,
            response_serializer=injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgClaimVoucherResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler("injective.permissions.v1beta1.Msg", rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers("injective.permissions.v1beta1.Msg", rpc_method_handlers)


# This class is part of an EXPERIMENTAL API.
class Msg(object):
    """Msg defines the permissions module's gRPC message service."""

    @staticmethod
    def UpdateParams(
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
            "/injective.permissions.v1beta1.Msg/UpdateParams",
            injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgUpdateParams.SerializeToString,
            injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgUpdateParamsResponse.FromString,
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
    def CreateNamespace(
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
            "/injective.permissions.v1beta1.Msg/CreateNamespace",
            injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgCreateNamespace.SerializeToString,
            injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgCreateNamespaceResponse.FromString,
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
    def DeleteNamespace(
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
            "/injective.permissions.v1beta1.Msg/DeleteNamespace",
            injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgDeleteNamespace.SerializeToString,
            injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgDeleteNamespaceResponse.FromString,
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
    def UpdateNamespace(
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
            "/injective.permissions.v1beta1.Msg/UpdateNamespace",
            injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgUpdateNamespace.SerializeToString,
            injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgUpdateNamespaceResponse.FromString,
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
    def UpdateNamespaceRoles(
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
            "/injective.permissions.v1beta1.Msg/UpdateNamespaceRoles",
            injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgUpdateNamespaceRoles.SerializeToString,
            injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgUpdateNamespaceRolesResponse.FromString,
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
    def RevokeNamespaceRoles(
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
            "/injective.permissions.v1beta1.Msg/RevokeNamespaceRoles",
            injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgRevokeNamespaceRoles.SerializeToString,
            injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgRevokeNamespaceRolesResponse.FromString,
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
    def ClaimVoucher(
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
            "/injective.permissions.v1beta1.Msg/ClaimVoucher",
            injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgClaimVoucher.SerializeToString,
            injective_dot_permissions_dot_v1beta1_dot_tx__pb2.MsgClaimVoucherResponse.FromString,
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
