# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mesh/v1alpha1/config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from mesh.v1alpha1 import proxy_pb2 as mesh_dot_v1alpha1_dot_proxy__pb2
from networking.v1alpha3 import destination_rule_pb2 as networking_dot_v1alpha3_dot_destination__rule__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mesh/v1alpha1/config.proto',
  package='istio.mesh.v1alpha1',
  syntax='proto3',
  serialized_options=_b('Z\032istio.io/api/mesh/v1alpha1'),
  serialized_pb=_b('\n\x1amesh/v1alpha1/config.proto\x12\x13istio.mesh.v1alpha1\x1a\x1egoogle/protobuf/duration.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x19mesh/v1alpha1/proxy.proto\x1a*networking/v1alpha3/destination_rule.proto\"\x8b\x13\n\nMeshConfig\x12\x1a\n\x12mixer_check_server\x18\x01 \x01(\t\x12\x1b\n\x13mixer_report_server\x18\x02 \x01(\t\x12\x1d\n\x15\x64isable_policy_checks\x18\x03 \x01(\x08\x12\"\n\x1a\x64isable_mixer_http_reports\x18\x30 \x01(\x08\x12\x1e\n\x16policy_check_fail_open\x18\x19 \x01(\x08\x12-\n%sidecar_to_telemetry_session_affinity\x18\x1e \x01(\x08\x12\x19\n\x11proxy_listen_port\x18\x04 \x01(\x05\x12\x17\n\x0fproxy_http_port\x18\x05 \x01(\x05\x12\x32\n\x0f\x63onnect_timeout\x18\x06 \x01(\x0b\x32\x19.google.protobuf.Duration\x12=\n\x1aprotocol_detection_timeout\x18* \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x61\n\rtcp_keepalive\x18\x1c \x01(\x0b\x32J.istio.networking.v1alpha3.ConnectionPoolSettings.TCPSettings.TcpKeepalive\x12\x15\n\ringress_class\x18\x07 \x01(\t\x12\x17\n\x0fingress_service\x18\x08 \x01(\t\x12V\n\x17ingress_controller_mode\x18\t \x01(\x0e\x32\x35.istio.mesh.v1alpha1.MeshConfig.IngressControllerMode\x12\x43\n\x0b\x61uth_policy\x18\n \x01(\x0e\x32*.istio.mesh.v1alpha1.MeshConfig.AuthPolicyB\x02\x18\x01\x12\x38\n\x11rds_refresh_delay\x18\x0b \x01(\x0b\x32\x19.google.protobuf.DurationB\x02\x18\x01\x12\x16\n\x0e\x65nable_tracing\x18\x0c \x01(\x08\x12\x17\n\x0f\x61\x63\x63\x65ss_log_file\x18\r \x01(\t\x12\x19\n\x11\x61\x63\x63\x65ss_log_format\x18\x18 \x01(\t\x12N\n\x13\x61\x63\x63\x65ss_log_encoding\x18\x1b \x01(\x0e\x32\x31.istio.mesh.v1alpha1.MeshConfig.AccessLogEncoding\x12\'\n\x1f\x65nable_envoy_access_log_service\x18( \x01(\x08\x12\x38\n\x0e\x64\x65\x66\x61ult_config\x18\x0e \x01(\x0b\x32 .istio.mesh.v1alpha1.ProxyConfig\x12\x19\n\rmixer_address\x18\x10 \x01(\tB\x02\x18\x01\x12V\n\x17outbound_traffic_policy\x18\x11 \x01(\x0b\x32\x35.istio.mesh.v1alpha1.MeshConfig.OutboundTrafficPolicy\x12\'\n\x1f\x65nable_client_side_policy_check\x18\x13 \x01(\x08\x12\x14\n\x0csds_uds_path\x18\x14 \x01(\t\x12\x38\n\x11sds_refresh_delay\x18\x15 \x01(\x0b\x32\x19.google.protobuf.DurationB\x02\x18\x01\x12\x39\n\x0e\x63onfig_sources\x18\x16 \x03(\x0b\x32!.istio.mesh.v1alpha1.ConfigSource\x12\x34\n\x10\x65nable_auto_mtls\x18+ \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x1e\n\x16\x65nable_sds_token_mount\x18\x17 \x01(\x08\x12\x1a\n\x12sds_use_k8s_sa_jwt\x18\x1d \x01(\x08\x12\x14\n\x0ctrust_domain\x18\x1a \x01(\t\x12\x1c\n\x14trust_domain_aliases\x18. \x03(\t\x12!\n\x19\x64\x65\x66\x61ult_service_export_to\x18\x1f \x03(\t\x12)\n!default_virtual_service_export_to\x18  \x03(\t\x12*\n\"default_destination_rule_export_to\x18! \x03(\t\x12\x16\n\x0eroot_namespace\x18\" \x01(\t\x12S\n\x13locality_lb_setting\x18# \x01(\x0b\x32\x36.istio.networking.v1alpha3.LocalityLoadBalancerSetting\x12\x33\n\x10\x64ns_refresh_rate\x18$ \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x1c\n\x14\x64isable_report_batch\x18% \x01(\x08\x12 \n\x18report_batch_max_entries\x18& \x01(\r\x12\x38\n\x15report_batch_max_time\x18\' \x01(\x0b\x32\x19.google.protobuf.Duration\x12J\n\x11h2_upgrade_policy\x18) \x01(\x0e\x32/.istio.mesh.v1alpha1.MeshConfig.H2UpgradePolicy\x12!\n\x19inbound_cluster_stat_name\x18, \x01(\t\x12\"\n\x1aoutbound_cluster_stat_name\x18- \x01(\t\x12\x36\n\x0c\x63\x65rtificates\x18/ \x03(\x0b\x32 .istio.mesh.v1alpha1.Certificate\x1a\xa7\x01\n\x15OutboundTrafficPolicy\x12H\n\x04mode\x18\x01 \x01(\x0e\x32:.istio.mesh.v1alpha1.MeshConfig.OutboundTrafficPolicy.Mode\"D\n\x04Mode\x12\x11\n\rREGISTRY_ONLY\x10\x00\x12\r\n\tALLOW_ANY\x10\x01\"\x04\x08\x02\x10\x02*\x14VIRTUAL_SERVICE_ONLY\"9\n\x15IngressControllerMode\x12\x07\n\x03OFF\x10\x00\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x01\x12\n\n\x06STRICT\x10\x02\"&\n\nAuthPolicy\x12\x08\n\x04NONE\x10\x00\x12\x0e\n\nMUTUAL_TLS\x10\x01\"\'\n\x11\x41\x63\x63\x65ssLogEncoding\x12\x08\n\x04TEXT\x10\x00\x12\x08\n\x04JSON\x10\x01\"2\n\x0fH2UpgradePolicy\x12\x12\n\x0e\x44O_NOT_UPGRADE\x10\x00\x12\x0b\n\x07UPGRADE\x10\x01J\x04\x08\x0f\x10\x10J\x04\x08\x12\x10\x13\"\x9a\x01\n\x0c\x43onfigSource\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12<\n\x0ctls_settings\x18\x02 \x01(\x0b\x32&.istio.networking.v1alpha3.TLSSettings\x12;\n\x14subscribed_resources\x18\x03 \x03(\x0e\x32\x1d.istio.mesh.v1alpha1.Resource\"5\n\x0b\x43\x65rtificate\x12\x13\n\x0bsecret_name\x18\x01 \x01(\t\x12\x11\n\tdns_names\x18\x02 \x03(\t* \n\x08Resource\x12\x14\n\x10SERVICE_REGISTRY\x10\x00\x42\x1cZ\x1aistio.io/api/mesh/v1alpha1b\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,mesh_dot_v1alpha1_dot_proxy__pb2.DESCRIPTOR,networking_dot_v1alpha3_dot_destination__rule__pb2.DESCRIPTOR,])

_RESOURCE = _descriptor.EnumDescriptor(
  name='Resource',
  full_name='istio.mesh.v1alpha1.Resource',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SERVICE_REGISTRY', index=0, number=0,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2844,
  serialized_end=2876,
)
_sym_db.RegisterEnumDescriptor(_RESOURCE)

Resource = enum_type_wrapper.EnumTypeWrapper(_RESOURCE)
SERVICE_REGISTRY = 0


_MESHCONFIG_OUTBOUNDTRAFFICPOLICY_MODE = _descriptor.EnumDescriptor(
  name='Mode',
  full_name='istio.mesh.v1alpha1.MeshConfig.OutboundTrafficPolicy.Mode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='REGISTRY_ONLY', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALLOW_ANY', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2358,
  serialized_end=2426,
)
_sym_db.RegisterEnumDescriptor(_MESHCONFIG_OUTBOUNDTRAFFICPOLICY_MODE)

_MESHCONFIG_INGRESSCONTROLLERMODE = _descriptor.EnumDescriptor(
  name='IngressControllerMode',
  full_name='istio.mesh.v1alpha1.MeshConfig.IngressControllerMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OFF', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEFAULT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRICT', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2428,
  serialized_end=2485,
)
_sym_db.RegisterEnumDescriptor(_MESHCONFIG_INGRESSCONTROLLERMODE)

_MESHCONFIG_AUTHPOLICY = _descriptor.EnumDescriptor(
  name='AuthPolicy',
  full_name='istio.mesh.v1alpha1.MeshConfig.AuthPolicy',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MUTUAL_TLS', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2487,
  serialized_end=2525,
)
_sym_db.RegisterEnumDescriptor(_MESHCONFIG_AUTHPOLICY)

_MESHCONFIG_ACCESSLOGENCODING = _descriptor.EnumDescriptor(
  name='AccessLogEncoding',
  full_name='istio.mesh.v1alpha1.MeshConfig.AccessLogEncoding',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TEXT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JSON', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2527,
  serialized_end=2566,
)
_sym_db.RegisterEnumDescriptor(_MESHCONFIG_ACCESSLOGENCODING)

_MESHCONFIG_H2UPGRADEPOLICY = _descriptor.EnumDescriptor(
  name='H2UpgradePolicy',
  full_name='istio.mesh.v1alpha1.MeshConfig.H2UpgradePolicy',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DO_NOT_UPGRADE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPGRADE', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2568,
  serialized_end=2618,
)
_sym_db.RegisterEnumDescriptor(_MESHCONFIG_H2UPGRADEPOLICY)


_MESHCONFIG_OUTBOUNDTRAFFICPOLICY = _descriptor.Descriptor(
  name='OutboundTrafficPolicy',
  full_name='istio.mesh.v1alpha1.MeshConfig.OutboundTrafficPolicy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mode', full_name='istio.mesh.v1alpha1.MeshConfig.OutboundTrafficPolicy.mode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MESHCONFIG_OUTBOUNDTRAFFICPOLICY_MODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2259,
  serialized_end=2426,
)

_MESHCONFIG = _descriptor.Descriptor(
  name='MeshConfig',
  full_name='istio.mesh.v1alpha1.MeshConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mixer_check_server', full_name='istio.mesh.v1alpha1.MeshConfig.mixer_check_server', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mixer_report_server', full_name='istio.mesh.v1alpha1.MeshConfig.mixer_report_server', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disable_policy_checks', full_name='istio.mesh.v1alpha1.MeshConfig.disable_policy_checks', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disable_mixer_http_reports', full_name='istio.mesh.v1alpha1.MeshConfig.disable_mixer_http_reports', index=3,
      number=48, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='policy_check_fail_open', full_name='istio.mesh.v1alpha1.MeshConfig.policy_check_fail_open', index=4,
      number=25, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sidecar_to_telemetry_session_affinity', full_name='istio.mesh.v1alpha1.MeshConfig.sidecar_to_telemetry_session_affinity', index=5,
      number=30, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proxy_listen_port', full_name='istio.mesh.v1alpha1.MeshConfig.proxy_listen_port', index=6,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proxy_http_port', full_name='istio.mesh.v1alpha1.MeshConfig.proxy_http_port', index=7,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connect_timeout', full_name='istio.mesh.v1alpha1.MeshConfig.connect_timeout', index=8,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='protocol_detection_timeout', full_name='istio.mesh.v1alpha1.MeshConfig.protocol_detection_timeout', index=9,
      number=42, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tcp_keepalive', full_name='istio.mesh.v1alpha1.MeshConfig.tcp_keepalive', index=10,
      number=28, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ingress_class', full_name='istio.mesh.v1alpha1.MeshConfig.ingress_class', index=11,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ingress_service', full_name='istio.mesh.v1alpha1.MeshConfig.ingress_service', index=12,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ingress_controller_mode', full_name='istio.mesh.v1alpha1.MeshConfig.ingress_controller_mode', index=13,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auth_policy', full_name='istio.mesh.v1alpha1.MeshConfig.auth_policy', index=14,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rds_refresh_delay', full_name='istio.mesh.v1alpha1.MeshConfig.rds_refresh_delay', index=15,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_tracing', full_name='istio.mesh.v1alpha1.MeshConfig.enable_tracing', index=16,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='access_log_file', full_name='istio.mesh.v1alpha1.MeshConfig.access_log_file', index=17,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='access_log_format', full_name='istio.mesh.v1alpha1.MeshConfig.access_log_format', index=18,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='access_log_encoding', full_name='istio.mesh.v1alpha1.MeshConfig.access_log_encoding', index=19,
      number=27, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_envoy_access_log_service', full_name='istio.mesh.v1alpha1.MeshConfig.enable_envoy_access_log_service', index=20,
      number=40, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default_config', full_name='istio.mesh.v1alpha1.MeshConfig.default_config', index=21,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mixer_address', full_name='istio.mesh.v1alpha1.MeshConfig.mixer_address', index=22,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outbound_traffic_policy', full_name='istio.mesh.v1alpha1.MeshConfig.outbound_traffic_policy', index=23,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_client_side_policy_check', full_name='istio.mesh.v1alpha1.MeshConfig.enable_client_side_policy_check', index=24,
      number=19, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sds_uds_path', full_name='istio.mesh.v1alpha1.MeshConfig.sds_uds_path', index=25,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sds_refresh_delay', full_name='istio.mesh.v1alpha1.MeshConfig.sds_refresh_delay', index=26,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config_sources', full_name='istio.mesh.v1alpha1.MeshConfig.config_sources', index=27,
      number=22, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_auto_mtls', full_name='istio.mesh.v1alpha1.MeshConfig.enable_auto_mtls', index=28,
      number=43, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_sds_token_mount', full_name='istio.mesh.v1alpha1.MeshConfig.enable_sds_token_mount', index=29,
      number=23, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sds_use_k8s_sa_jwt', full_name='istio.mesh.v1alpha1.MeshConfig.sds_use_k8s_sa_jwt', index=30,
      number=29, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trust_domain', full_name='istio.mesh.v1alpha1.MeshConfig.trust_domain', index=31,
      number=26, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trust_domain_aliases', full_name='istio.mesh.v1alpha1.MeshConfig.trust_domain_aliases', index=32,
      number=46, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default_service_export_to', full_name='istio.mesh.v1alpha1.MeshConfig.default_service_export_to', index=33,
      number=31, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default_virtual_service_export_to', full_name='istio.mesh.v1alpha1.MeshConfig.default_virtual_service_export_to', index=34,
      number=32, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default_destination_rule_export_to', full_name='istio.mesh.v1alpha1.MeshConfig.default_destination_rule_export_to', index=35,
      number=33, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='root_namespace', full_name='istio.mesh.v1alpha1.MeshConfig.root_namespace', index=36,
      number=34, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='locality_lb_setting', full_name='istio.mesh.v1alpha1.MeshConfig.locality_lb_setting', index=37,
      number=35, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dns_refresh_rate', full_name='istio.mesh.v1alpha1.MeshConfig.dns_refresh_rate', index=38,
      number=36, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disable_report_batch', full_name='istio.mesh.v1alpha1.MeshConfig.disable_report_batch', index=39,
      number=37, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='report_batch_max_entries', full_name='istio.mesh.v1alpha1.MeshConfig.report_batch_max_entries', index=40,
      number=38, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='report_batch_max_time', full_name='istio.mesh.v1alpha1.MeshConfig.report_batch_max_time', index=41,
      number=39, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='h2_upgrade_policy', full_name='istio.mesh.v1alpha1.MeshConfig.h2_upgrade_policy', index=42,
      number=41, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inbound_cluster_stat_name', full_name='istio.mesh.v1alpha1.MeshConfig.inbound_cluster_stat_name', index=43,
      number=44, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outbound_cluster_stat_name', full_name='istio.mesh.v1alpha1.MeshConfig.outbound_cluster_stat_name', index=44,
      number=45, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='certificates', full_name='istio.mesh.v1alpha1.MeshConfig.certificates', index=45,
      number=47, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MESHCONFIG_OUTBOUNDTRAFFICPOLICY, ],
  enum_types=[
    _MESHCONFIG_INGRESSCONTROLLERMODE,
    _MESHCONFIG_AUTHPOLICY,
    _MESHCONFIG_ACCESSLOGENCODING,
    _MESHCONFIG_H2UPGRADEPOLICY,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=187,
  serialized_end=2630,
)


_CONFIGSOURCE = _descriptor.Descriptor(
  name='ConfigSource',
  full_name='istio.mesh.v1alpha1.ConfigSource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='istio.mesh.v1alpha1.ConfigSource.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tls_settings', full_name='istio.mesh.v1alpha1.ConfigSource.tls_settings', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subscribed_resources', full_name='istio.mesh.v1alpha1.ConfigSource.subscribed_resources', index=2,
      number=3, type=14, cpp_type=8, label=3,
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
  serialized_start=2633,
  serialized_end=2787,
)


_CERTIFICATE = _descriptor.Descriptor(
  name='Certificate',
  full_name='istio.mesh.v1alpha1.Certificate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='secret_name', full_name='istio.mesh.v1alpha1.Certificate.secret_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dns_names', full_name='istio.mesh.v1alpha1.Certificate.dns_names', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=2789,
  serialized_end=2842,
)

_MESHCONFIG_OUTBOUNDTRAFFICPOLICY.fields_by_name['mode'].enum_type = _MESHCONFIG_OUTBOUNDTRAFFICPOLICY_MODE
_MESHCONFIG_OUTBOUNDTRAFFICPOLICY.containing_type = _MESHCONFIG
_MESHCONFIG_OUTBOUNDTRAFFICPOLICY_MODE.containing_type = _MESHCONFIG_OUTBOUNDTRAFFICPOLICY
_MESHCONFIG.fields_by_name['connect_timeout'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_MESHCONFIG.fields_by_name['protocol_detection_timeout'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_MESHCONFIG.fields_by_name['tcp_keepalive'].message_type = networking_dot_v1alpha3_dot_destination__rule__pb2._CONNECTIONPOOLSETTINGS_TCPSETTINGS_TCPKEEPALIVE
_MESHCONFIG.fields_by_name['ingress_controller_mode'].enum_type = _MESHCONFIG_INGRESSCONTROLLERMODE
_MESHCONFIG.fields_by_name['auth_policy'].enum_type = _MESHCONFIG_AUTHPOLICY
_MESHCONFIG.fields_by_name['rds_refresh_delay'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_MESHCONFIG.fields_by_name['access_log_encoding'].enum_type = _MESHCONFIG_ACCESSLOGENCODING
_MESHCONFIG.fields_by_name['default_config'].message_type = mesh_dot_v1alpha1_dot_proxy__pb2._PROXYCONFIG
_MESHCONFIG.fields_by_name['outbound_traffic_policy'].message_type = _MESHCONFIG_OUTBOUNDTRAFFICPOLICY
_MESHCONFIG.fields_by_name['sds_refresh_delay'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_MESHCONFIG.fields_by_name['config_sources'].message_type = _CONFIGSOURCE
_MESHCONFIG.fields_by_name['enable_auto_mtls'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_MESHCONFIG.fields_by_name['locality_lb_setting'].message_type = networking_dot_v1alpha3_dot_destination__rule__pb2._LOCALITYLOADBALANCERSETTING
_MESHCONFIG.fields_by_name['dns_refresh_rate'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_MESHCONFIG.fields_by_name['report_batch_max_time'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_MESHCONFIG.fields_by_name['h2_upgrade_policy'].enum_type = _MESHCONFIG_H2UPGRADEPOLICY
_MESHCONFIG.fields_by_name['certificates'].message_type = _CERTIFICATE
_MESHCONFIG_INGRESSCONTROLLERMODE.containing_type = _MESHCONFIG
_MESHCONFIG_AUTHPOLICY.containing_type = _MESHCONFIG
_MESHCONFIG_ACCESSLOGENCODING.containing_type = _MESHCONFIG
_MESHCONFIG_H2UPGRADEPOLICY.containing_type = _MESHCONFIG
_CONFIGSOURCE.fields_by_name['tls_settings'].message_type = networking_dot_v1alpha3_dot_destination__rule__pb2._TLSSETTINGS
_CONFIGSOURCE.fields_by_name['subscribed_resources'].enum_type = _RESOURCE
DESCRIPTOR.message_types_by_name['MeshConfig'] = _MESHCONFIG
DESCRIPTOR.message_types_by_name['ConfigSource'] = _CONFIGSOURCE
DESCRIPTOR.message_types_by_name['Certificate'] = _CERTIFICATE
DESCRIPTOR.enum_types_by_name['Resource'] = _RESOURCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MeshConfig = _reflection.GeneratedProtocolMessageType('MeshConfig', (_message.Message,), {

  'OutboundTrafficPolicy' : _reflection.GeneratedProtocolMessageType('OutboundTrafficPolicy', (_message.Message,), {
    'DESCRIPTOR' : _MESHCONFIG_OUTBOUNDTRAFFICPOLICY,
    '__module__' : 'mesh.v1alpha1.config_pb2'
    # @@protoc_insertion_point(class_scope:istio.mesh.v1alpha1.MeshConfig.OutboundTrafficPolicy)
    })
  ,
  'DESCRIPTOR' : _MESHCONFIG,
  '__module__' : 'mesh.v1alpha1.config_pb2'
  # @@protoc_insertion_point(class_scope:istio.mesh.v1alpha1.MeshConfig)
  })
_sym_db.RegisterMessage(MeshConfig)
_sym_db.RegisterMessage(MeshConfig.OutboundTrafficPolicy)

ConfigSource = _reflection.GeneratedProtocolMessageType('ConfigSource', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGSOURCE,
  '__module__' : 'mesh.v1alpha1.config_pb2'
  # @@protoc_insertion_point(class_scope:istio.mesh.v1alpha1.ConfigSource)
  })
_sym_db.RegisterMessage(ConfigSource)

Certificate = _reflection.GeneratedProtocolMessageType('Certificate', (_message.Message,), {
  'DESCRIPTOR' : _CERTIFICATE,
  '__module__' : 'mesh.v1alpha1.config_pb2'
  # @@protoc_insertion_point(class_scope:istio.mesh.v1alpha1.Certificate)
  })
_sym_db.RegisterMessage(Certificate)


DESCRIPTOR._options = None
_MESHCONFIG.fields_by_name['auth_policy']._options = None
_MESHCONFIG.fields_by_name['rds_refresh_delay']._options = None
_MESHCONFIG.fields_by_name['mixer_address']._options = None
_MESHCONFIG.fields_by_name['sds_refresh_delay']._options = None
# @@protoc_insertion_point(module_scope)
