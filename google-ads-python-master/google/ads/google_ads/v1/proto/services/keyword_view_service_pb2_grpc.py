# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v1.proto.resources import keyword_view_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_keyword__view__pb2
from google.ads.google_ads.v1.proto.services import keyword_view_service_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_keyword__view__service__pb2


class KeywordViewServiceStub(object):
  """Proto file describing the Keyword View service.

  Service to manage keyword views.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetKeywordView = channel.unary_unary(
        '/google.ads.googleads.v1.services.KeywordViewService/GetKeywordView',
        request_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_keyword__view__service__pb2.GetKeywordViewRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_keyword__view__pb2.KeywordView.FromString,
        )


class KeywordViewServiceServicer(object):
  """Proto file describing the Keyword View service.

  Service to manage keyword views.
  """

  def GetKeywordView(self, request, context):
    """Returns the requested keyword view in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_KeywordViewServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetKeywordView': grpc.unary_unary_rpc_method_handler(
          servicer.GetKeywordView,
          request_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_keyword__view__service__pb2.GetKeywordViewRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_keyword__view__pb2.KeywordView.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v1.services.KeywordViewService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
