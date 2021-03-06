# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import digimons_pb2 as digimons__pb2


class DiginfoStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.search = channel.unary_unary(
                '/digimons.Diginfo/search',
                request_serializer=digimons__pb2.Digiquest.SerializeToString,
                response_deserializer=digimons__pb2.Digisponse.FromString,
                )


class DiginfoServicer(object):
    """Missing associated documentation comment in .proto file."""

    def search(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DiginfoServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'search': grpc.unary_unary_rpc_method_handler(
                    servicer.search,
                    request_deserializer=digimons__pb2.Digiquest.FromString,
                    response_serializer=digimons__pb2.Digisponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'digimons.Diginfo', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Diginfo(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def search(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/digimons.Diginfo/search',
            digimons__pb2.Digiquest.SerializeToString,
            digimons__pb2.Digisponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
