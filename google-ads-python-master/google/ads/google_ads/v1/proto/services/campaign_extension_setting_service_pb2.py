# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/services/campaign_extension_setting_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v1.proto.resources import campaign_extension_setting_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_campaign__extension__setting__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v1/proto/services/campaign_extension_setting_service.proto',
  package='google.ads.googleads.v1.services',
  syntax='proto3',
  serialized_options=_b('\n$com.google.ads.googleads.v1.servicesB$CampaignExtensionSettingServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v1/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V1.Services\312\002 Google\\Ads\\GoogleAds\\V1\\Services\352\002$Google::Ads::GoogleAds::V1::Services'),
  serialized_pb=_b('\nOgoogle/ads/googleads_v1/proto/services/campaign_extension_setting_service.proto\x12 google.ads.googleads.v1.services\x1aHgoogle/ads/googleads_v1/proto/resources/campaign_extension_setting.proto\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x17google/rpc/status.proto\";\n\"GetCampaignExtensionSettingRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t\"\xc6\x01\n&MutateCampaignExtensionSettingsRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\t\x12W\n\noperations\x18\x02 \x03(\x0b\x32\x43.google.ads.googleads.v1.services.CampaignExtensionSettingOperation\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\"\x91\x02\n!CampaignExtensionSettingOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12M\n\x06\x63reate\x18\x01 \x01(\x0b\x32;.google.ads.googleads.v1.resources.CampaignExtensionSettingH\x00\x12M\n\x06update\x18\x02 \x01(\x0b\x32;.google.ads.googleads.v1.resources.CampaignExtensionSettingH\x00\x12\x10\n\x06remove\x18\x03 \x01(\tH\x00\x42\x0b\n\toperation\"\xb5\x01\n\'MutateCampaignExtensionSettingsResponse\x12\x31\n\x15partial_failure_error\x18\x03 \x01(\x0b\x32\x12.google.rpc.Status\x12W\n\x07results\x18\x02 \x03(\x0b\x32\x46.google.ads.googleads.v1.services.MutateCampaignExtensionSettingResult\"=\n$MutateCampaignExtensionSettingResult\x12\x15\n\rresource_name\x18\x01 \x01(\t2\x8d\x04\n\x1f\x43\x61mpaignExtensionSettingService\x12\xe5\x01\n\x1bGetCampaignExtensionSetting\x12\x44.google.ads.googleads.v1.services.GetCampaignExtensionSettingRequest\x1a;.google.ads.googleads.v1.resources.CampaignExtensionSetting\"C\x82\xd3\xe4\x93\x02=\x12;/v1/{resource_name=customers/*/campaignExtensionSettings/*}\x12\x81\x02\n\x1fMutateCampaignExtensionSettings\x12H.google.ads.googleads.v1.services.MutateCampaignExtensionSettingsRequest\x1aI.google.ads.googleads.v1.services.MutateCampaignExtensionSettingsResponse\"I\x82\xd3\xe4\x93\x02\x43\">/v1/customers/{customer_id=*}/campaignExtensionSettings:mutate:\x01*B\x8b\x02\n$com.google.ads.googleads.v1.servicesB$CampaignExtensionSettingServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v1/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V1.Services\xca\x02 Google\\Ads\\GoogleAds\\V1\\Services\xea\x02$Google::Ads::GoogleAds::V1::Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_campaign__extension__setting__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])




_GETCAMPAIGNEXTENSIONSETTINGREQUEST = _descriptor.Descriptor(
  name='GetCampaignExtensionSettingRequest',
  full_name='google.ads.googleads.v1.services.GetCampaignExtensionSettingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v1.services.GetCampaignExtensionSettingRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=312,
  serialized_end=371,
)


_MUTATECAMPAIGNEXTENSIONSETTINGSREQUEST = _descriptor.Descriptor(
  name='MutateCampaignExtensionSettingsRequest',
  full_name='google.ads.googleads.v1.services.MutateCampaignExtensionSettingsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v1.services.MutateCampaignExtensionSettingsRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operations', full_name='google.ads.googleads.v1.services.MutateCampaignExtensionSettingsRequest.operations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partial_failure', full_name='google.ads.googleads.v1.services.MutateCampaignExtensionSettingsRequest.partial_failure', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validate_only', full_name='google.ads.googleads.v1.services.MutateCampaignExtensionSettingsRequest.validate_only', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=374,
  serialized_end=572,
)


_CAMPAIGNEXTENSIONSETTINGOPERATION = _descriptor.Descriptor(
  name='CampaignExtensionSettingOperation',
  full_name='google.ads.googleads.v1.services.CampaignExtensionSettingOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.ads.googleads.v1.services.CampaignExtensionSettingOperation.update_mask', index=0,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create', full_name='google.ads.googleads.v1.services.CampaignExtensionSettingOperation.create', index=1,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update', full_name='google.ads.googleads.v1.services.CampaignExtensionSettingOperation.update', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remove', full_name='google.ads.googleads.v1.services.CampaignExtensionSettingOperation.remove', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='operation', full_name='google.ads.googleads.v1.services.CampaignExtensionSettingOperation.operation',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=575,
  serialized_end=848,
)


_MUTATECAMPAIGNEXTENSIONSETTINGSRESPONSE = _descriptor.Descriptor(
  name='MutateCampaignExtensionSettingsResponse',
  full_name='google.ads.googleads.v1.services.MutateCampaignExtensionSettingsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='partial_failure_error', full_name='google.ads.googleads.v1.services.MutateCampaignExtensionSettingsResponse.partial_failure_error', index=0,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v1.services.MutateCampaignExtensionSettingsResponse.results', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=851,
  serialized_end=1032,
)


_MUTATECAMPAIGNEXTENSIONSETTINGRESULT = _descriptor.Descriptor(
  name='MutateCampaignExtensionSettingResult',
  full_name='google.ads.googleads.v1.services.MutateCampaignExtensionSettingResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v1.services.MutateCampaignExtensionSettingResult.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1034,
  serialized_end=1095,
)

_MUTATECAMPAIGNEXTENSIONSETTINGSREQUEST.fields_by_name['operations'].message_type = _CAMPAIGNEXTENSIONSETTINGOPERATION
_CAMPAIGNEXTENSIONSETTINGOPERATION.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_CAMPAIGNEXTENSIONSETTINGOPERATION.fields_by_name['create'].message_type = google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_campaign__extension__setting__pb2._CAMPAIGNEXTENSIONSETTING
_CAMPAIGNEXTENSIONSETTINGOPERATION.fields_by_name['update'].message_type = google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_campaign__extension__setting__pb2._CAMPAIGNEXTENSIONSETTING
_CAMPAIGNEXTENSIONSETTINGOPERATION.oneofs_by_name['operation'].fields.append(
  _CAMPAIGNEXTENSIONSETTINGOPERATION.fields_by_name['create'])
_CAMPAIGNEXTENSIONSETTINGOPERATION.fields_by_name['create'].containing_oneof = _CAMPAIGNEXTENSIONSETTINGOPERATION.oneofs_by_name['operation']
_CAMPAIGNEXTENSIONSETTINGOPERATION.oneofs_by_name['operation'].fields.append(
  _CAMPAIGNEXTENSIONSETTINGOPERATION.fields_by_name['update'])
_CAMPAIGNEXTENSIONSETTINGOPERATION.fields_by_name['update'].containing_oneof = _CAMPAIGNEXTENSIONSETTINGOPERATION.oneofs_by_name['operation']
_CAMPAIGNEXTENSIONSETTINGOPERATION.oneofs_by_name['operation'].fields.append(
  _CAMPAIGNEXTENSIONSETTINGOPERATION.fields_by_name['remove'])
_CAMPAIGNEXTENSIONSETTINGOPERATION.fields_by_name['remove'].containing_oneof = _CAMPAIGNEXTENSIONSETTINGOPERATION.oneofs_by_name['operation']
_MUTATECAMPAIGNEXTENSIONSETTINGSRESPONSE.fields_by_name['partial_failure_error'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_MUTATECAMPAIGNEXTENSIONSETTINGSRESPONSE.fields_by_name['results'].message_type = _MUTATECAMPAIGNEXTENSIONSETTINGRESULT
DESCRIPTOR.message_types_by_name['GetCampaignExtensionSettingRequest'] = _GETCAMPAIGNEXTENSIONSETTINGREQUEST
DESCRIPTOR.message_types_by_name['MutateCampaignExtensionSettingsRequest'] = _MUTATECAMPAIGNEXTENSIONSETTINGSREQUEST
DESCRIPTOR.message_types_by_name['CampaignExtensionSettingOperation'] = _CAMPAIGNEXTENSIONSETTINGOPERATION
DESCRIPTOR.message_types_by_name['MutateCampaignExtensionSettingsResponse'] = _MUTATECAMPAIGNEXTENSIONSETTINGSRESPONSE
DESCRIPTOR.message_types_by_name['MutateCampaignExtensionSettingResult'] = _MUTATECAMPAIGNEXTENSIONSETTINGRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetCampaignExtensionSettingRequest = _reflection.GeneratedProtocolMessageType('GetCampaignExtensionSettingRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETCAMPAIGNEXTENSIONSETTINGREQUEST,
  __module__ = 'google.ads.googleads_v1.proto.services.campaign_extension_setting_service_pb2'
  ,
  __doc__ = """Request message for
  [CampaignExtensionSettingService.GetCampaignExtensionSetting][google.ads.googleads.v1.services.CampaignExtensionSettingService.GetCampaignExtensionSetting].
  
  
  Attributes:
      resource_name:
          The resource name of the campaign extension setting to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.GetCampaignExtensionSettingRequest)
  ))
_sym_db.RegisterMessage(GetCampaignExtensionSettingRequest)

MutateCampaignExtensionSettingsRequest = _reflection.GeneratedProtocolMessageType('MutateCampaignExtensionSettingsRequest', (_message.Message,), dict(
  DESCRIPTOR = _MUTATECAMPAIGNEXTENSIONSETTINGSREQUEST,
  __module__ = 'google.ads.googleads_v1.proto.services.campaign_extension_setting_service_pb2'
  ,
  __doc__ = """Request message for
  [CampaignExtensionSettingService.MutateCampaignExtensionSettings][google.ads.googleads.v1.services.CampaignExtensionSettingService.MutateCampaignExtensionSettings].
  
  
  Attributes:
      customer_id:
          The ID of the customer whose campaign extension settings are
          being modified.
      operations:
          The list of operations to perform on individual campaign
          extension settings.
      partial_failure:
          If true, successful operations will be carried out and invalid
          operations will return errors. If false, all operations will
          be carried out in one transaction if and only if they are all
          valid. Default is false.
      validate_only:
          If true, the request is validated but not executed. Only
          errors are returned, not results.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.MutateCampaignExtensionSettingsRequest)
  ))
_sym_db.RegisterMessage(MutateCampaignExtensionSettingsRequest)

CampaignExtensionSettingOperation = _reflection.GeneratedProtocolMessageType('CampaignExtensionSettingOperation', (_message.Message,), dict(
  DESCRIPTOR = _CAMPAIGNEXTENSIONSETTINGOPERATION,
  __module__ = 'google.ads.googleads_v1.proto.services.campaign_extension_setting_service_pb2'
  ,
  __doc__ = """A single operation (create, update, remove) on a campaign extension
  setting.
  
  
  Attributes:
      update_mask:
          FieldMask that determines which resource fields are modified
          in an update.
      operation:
          The mutate operation.
      create:
          Create operation: No resource name is expected for the new
          campaign extension setting.
      update:
          Update operation: The campaign extension setting is expected
          to have a valid resource name.
      remove:
          Remove operation: A resource name for the removed campaign
          extension setting is expected, in this format:  ``customers/{c
          ustomer_id}/campaignExtensionSettings/{campaign_id}~{extension
          _type}``
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.CampaignExtensionSettingOperation)
  ))
_sym_db.RegisterMessage(CampaignExtensionSettingOperation)

MutateCampaignExtensionSettingsResponse = _reflection.GeneratedProtocolMessageType('MutateCampaignExtensionSettingsResponse', (_message.Message,), dict(
  DESCRIPTOR = _MUTATECAMPAIGNEXTENSIONSETTINGSRESPONSE,
  __module__ = 'google.ads.googleads_v1.proto.services.campaign_extension_setting_service_pb2'
  ,
  __doc__ = """Response message for a campaign extension setting mutate.
  
  
  Attributes:
      partial_failure_error:
          Errors that pertain to operation failures in the partial
          failure mode. Returned only when partial\_failure = true and
          all errors occur inside the operations. If any errors occur
          outside the operations (e.g. auth errors), we return an RPC
          level error.
      results:
          All results for the mutate.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.MutateCampaignExtensionSettingsResponse)
  ))
_sym_db.RegisterMessage(MutateCampaignExtensionSettingsResponse)

MutateCampaignExtensionSettingResult = _reflection.GeneratedProtocolMessageType('MutateCampaignExtensionSettingResult', (_message.Message,), dict(
  DESCRIPTOR = _MUTATECAMPAIGNEXTENSIONSETTINGRESULT,
  __module__ = 'google.ads.googleads_v1.proto.services.campaign_extension_setting_service_pb2'
  ,
  __doc__ = """The result for the campaign extension setting mutate.
  
  
  Attributes:
      resource_name:
          Returned for successful operations.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.MutateCampaignExtensionSettingResult)
  ))
_sym_db.RegisterMessage(MutateCampaignExtensionSettingResult)


DESCRIPTOR._options = None

_CAMPAIGNEXTENSIONSETTINGSERVICE = _descriptor.ServiceDescriptor(
  name='CampaignExtensionSettingService',
  full_name='google.ads.googleads.v1.services.CampaignExtensionSettingService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1098,
  serialized_end=1623,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetCampaignExtensionSetting',
    full_name='google.ads.googleads.v1.services.CampaignExtensionSettingService.GetCampaignExtensionSetting',
    index=0,
    containing_service=None,
    input_type=_GETCAMPAIGNEXTENSIONSETTINGREQUEST,
    output_type=google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_campaign__extension__setting__pb2._CAMPAIGNEXTENSIONSETTING,
    serialized_options=_b('\202\323\344\223\002=\022;/v1/{resource_name=customers/*/campaignExtensionSettings/*}'),
  ),
  _descriptor.MethodDescriptor(
    name='MutateCampaignExtensionSettings',
    full_name='google.ads.googleads.v1.services.CampaignExtensionSettingService.MutateCampaignExtensionSettings',
    index=1,
    containing_service=None,
    input_type=_MUTATECAMPAIGNEXTENSIONSETTINGSREQUEST,
    output_type=_MUTATECAMPAIGNEXTENSIONSETTINGSRESPONSE,
    serialized_options=_b('\202\323\344\223\002C\">/v1/customers/{customer_id=*}/campaignExtensionSettings:mutate:\001*'),
  ),
])
_sym_db.RegisterServiceDescriptor(_CAMPAIGNEXTENSIONSETTINGSERVICE)

DESCRIPTOR.services_by_name['CampaignExtensionSettingService'] = _CAMPAIGNEXTENSIONSETTINGSERVICE

# @@protoc_insertion_point(module_scope)
