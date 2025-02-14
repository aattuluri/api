// Code generated by protoc-gen-gogo. DO NOT EDIT.
// source: envoy/config/filter/http/authn/v2alpha1/config.proto

package v2alpha1

import (
	fmt "fmt"
	proto "github.com/gogo/protobuf/proto"
	io "io"
	v1alpha1 "istio.io/api/authentication/v1alpha1"
	math "math"
	math_bits "math/bits"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.GoGoProtoPackageIsVersion3 // please upgrade the proto package

// FilterConfig is the config for Istio-specific filter that is used to enforce
// authentication policy on Envoy.
type FilterConfig struct {
	// Policy is the original copy of the policy.
	Policy *v1alpha1.Policy `protobuf:"bytes,1,opt,name=policy,proto3" json:"policy,omitempty"`
	// Map from issuer to location of the payload that is emitted by Jwt filter.
	// This information is added by pilot when construct and add Jwt and
	// authN filters.
	JwtOutputPayloadLocations map[string]string `protobuf:"bytes,2,rep,name=jwt_output_payload_locations,json=jwtOutputPayloadLocations,proto3" json:"jwt_output_payload_locations,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"bytes,2,opt,name=value,proto3"`
	// Skips validating the peer's trust domain.
	// By default, the istio authn filter will reject the request if the peer and
	// the local service is not in the same trust domain.
	// Set this field to true to skip the validation and allows peers from any
	// trust domains.
	// Note, the istio authn filter only validates the trust domain when mTLS is
	// used, In other words, this field has no effect for plaintext traffic.
	SkipValidateTrustDomain bool     `protobuf:"varint,3,opt,name=skip_validate_trust_domain,json=skipValidateTrustDomain,proto3" json:"skip_validate_trust_domain,omitempty"`
	XXX_NoUnkeyedLiteral    struct{} `json:"-"`
	XXX_unrecognized        []byte   `json:"-"`
	XXX_sizecache           int32    `json:"-"`
}

func (m *FilterConfig) Reset()         { *m = FilterConfig{} }
func (m *FilterConfig) String() string { return proto.CompactTextString(m) }
func (*FilterConfig) ProtoMessage()    {}
func (*FilterConfig) Descriptor() ([]byte, []int) {
	return fileDescriptor_b4b13c85ef974588, []int{0}
}
func (m *FilterConfig) XXX_Unmarshal(b []byte) error {
	return m.Unmarshal(b)
}
func (m *FilterConfig) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	if deterministic {
		return xxx_messageInfo_FilterConfig.Marshal(b, m, deterministic)
	} else {
		b = b[:cap(b)]
		n, err := m.MarshalToSizedBuffer(b)
		if err != nil {
			return nil, err
		}
		return b[:n], nil
	}
}
func (m *FilterConfig) XXX_Merge(src proto.Message) {
	xxx_messageInfo_FilterConfig.Merge(m, src)
}
func (m *FilterConfig) XXX_Size() int {
	return m.Size()
}
func (m *FilterConfig) XXX_DiscardUnknown() {
	xxx_messageInfo_FilterConfig.DiscardUnknown(m)
}

var xxx_messageInfo_FilterConfig proto.InternalMessageInfo

func (m *FilterConfig) GetPolicy() *v1alpha1.Policy {
	if m != nil {
		return m.Policy
	}
	return nil
}

func (m *FilterConfig) GetJwtOutputPayloadLocations() map[string]string {
	if m != nil {
		return m.JwtOutputPayloadLocations
	}
	return nil
}

func (m *FilterConfig) GetSkipValidateTrustDomain() bool {
	if m != nil {
		return m.SkipValidateTrustDomain
	}
	return false
}

func init() {
	proto.RegisterType((*FilterConfig)(nil), "istio.envoy.config.filter.http.authn.v2alpha1.FilterConfig")
	proto.RegisterMapType((map[string]string)(nil), "istio.envoy.config.filter.http.authn.v2alpha1.FilterConfig.JwtOutputPayloadLocationsEntry")
}

func init() {
	proto.RegisterFile("envoy/config/filter/http/authn/v2alpha1/config.proto", fileDescriptor_b4b13c85ef974588)
}

var fileDescriptor_b4b13c85ef974588 = []byte{
	// 345 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x94, 0x92, 0xcf, 0x4a, 0x33, 0x31,
	0x14, 0xc5, 0xc9, 0x94, 0xaf, 0x7c, 0xa6, 0x2e, 0x64, 0x10, 0x1c, 0x8b, 0x0c, 0x45, 0x14, 0xba,
	0x31, 0xa1, 0xb5, 0x0b, 0x51, 0xdc, 0xd4, 0x3f, 0x0b, 0x29, 0x58, 0x06, 0x71, 0xd1, 0xcd, 0x10,
	0xdb, 0xd4, 0xa6, 0x8d, 0x49, 0x98, 0xb9, 0x33, 0x65, 0x9e, 0xc5, 0x17, 0x72, 0xe9, 0x23, 0x48,
	0x1f, 0xc2, 0xb5, 0x4c, 0x32, 0x05, 0x5d, 0x28, 0xba, 0xcb, 0xcd, 0x39, 0xe7, 0x77, 0x93, 0x9b,
	0xe0, 0x1e, 0x57, 0xb9, 0x2e, 0xe8, 0x58, 0xab, 0xa9, 0x78, 0xa4, 0x53, 0x21, 0x81, 0x27, 0x74,
	0x06, 0x60, 0x28, 0xcb, 0x60, 0xa6, 0x68, 0xde, 0x65, 0xd2, 0xcc, 0x58, 0xa7, 0x72, 0x10, 0x93,
	0x68, 0xd0, 0xfe, 0x91, 0x48, 0x41, 0x68, 0x62, 0xb3, 0xa4, 0x52, 0x5c, 0x96, 0x94, 0x59, 0x62,
	0xb3, 0x64, 0x9d, 0x6d, 0x1e, 0x94, 0x35, 0x57, 0x20, 0xc6, 0x0c, 0x84, 0x56, 0x34, 0xef, 0x54,
	0x50, 0xa3, 0xa5, 0x18, 0x17, 0x0e, 0xba, 0xff, 0xee, 0xe1, 0xcd, 0x6b, 0x0b, 0xb9, 0xb0, 0x44,
	0xff, 0x1c, 0xd7, 0x9d, 0x21, 0x40, 0x2d, 0xd4, 0x6e, 0x74, 0x0f, 0x89, 0x6b, 0xfb, 0x95, 0x46,
	0xd6, 0x34, 0x32, 0xb4, 0xe6, 0xa8, 0x0a, 0xf9, 0xcf, 0x08, 0xef, 0xcd, 0x97, 0x10, 0xeb, 0x0c,
	0x4c, 0x06, 0xb1, 0x61, 0x85, 0xd4, 0x6c, 0x12, 0x4b, 0xed, 0x72, 0x69, 0xe0, 0xb5, 0x6a, 0xed,
	0x46, 0x77, 0x44, 0xfe, 0x74, 0x19, 0xf2, 0xf9, 0x88, 0xe4, 0x66, 0x09, 0xb7, 0x16, 0x3f, 0x74,
	0xf4, 0xc1, 0x1a, 0x7e, 0xa5, 0x20, 0x29, 0xa2, 0xdd, 0xf9, 0x77, 0xba, 0x7f, 0x86, 0x9b, 0xe9,
	0x42, 0x98, 0x38, 0x67, 0x52, 0x4c, 0x18, 0xf0, 0x18, 0x92, 0x2c, 0x85, 0x78, 0xa2, 0x9f, 0x98,
	0x50, 0x41, 0xad, 0x85, 0xda, 0xff, 0xa3, 0x9d, 0xd2, 0x71, 0x5f, 0x19, 0xee, 0x4a, 0xfd, 0xd2,
	0xca, 0xcd, 0x01, 0x0e, 0x7f, 0xee, 0xec, 0x6f, 0xe1, 0xda, 0x82, 0xbb, 0xc1, 0x6d, 0x44, 0xe5,
	0xd2, 0xdf, 0xc6, 0xff, 0x72, 0x26, 0x33, 0x1e, 0x78, 0x76, 0xcf, 0x15, 0xa7, 0xde, 0x09, 0xea,
	0xf7, 0x5f, 0x56, 0x21, 0x7a, 0x5d, 0x85, 0xe8, 0x6d, 0x15, 0xa2, 0x51, 0xcf, 0x8d, 0x43, 0x68,
	0xca, 0x8c, 0xa0, 0xbf, 0xfc, 0x1e, 0x0f, 0x75, 0xfb, 0x86, 0xc7, 0x1f, 0x01, 0x00, 0x00, 0xff,
	0xff, 0x54, 0x7b, 0x57, 0x19, 0x50, 0x02, 0x00, 0x00,
}

func (m *FilterConfig) Marshal() (dAtA []byte, err error) {
	size := m.Size()
	dAtA = make([]byte, size)
	n, err := m.MarshalToSizedBuffer(dAtA[:size])
	if err != nil {
		return nil, err
	}
	return dAtA[:n], nil
}

func (m *FilterConfig) MarshalTo(dAtA []byte) (int, error) {
	size := m.Size()
	return m.MarshalToSizedBuffer(dAtA[:size])
}

func (m *FilterConfig) MarshalToSizedBuffer(dAtA []byte) (int, error) {
	i := len(dAtA)
	_ = i
	var l int
	_ = l
	if m.XXX_unrecognized != nil {
		i -= len(m.XXX_unrecognized)
		copy(dAtA[i:], m.XXX_unrecognized)
	}
	if m.SkipValidateTrustDomain {
		i--
		if m.SkipValidateTrustDomain {
			dAtA[i] = 1
		} else {
			dAtA[i] = 0
		}
		i--
		dAtA[i] = 0x18
	}
	if len(m.JwtOutputPayloadLocations) > 0 {
		for k := range m.JwtOutputPayloadLocations {
			v := m.JwtOutputPayloadLocations[k]
			baseI := i
			i -= len(v)
			copy(dAtA[i:], v)
			i = encodeVarintConfig(dAtA, i, uint64(len(v)))
			i--
			dAtA[i] = 0x12
			i -= len(k)
			copy(dAtA[i:], k)
			i = encodeVarintConfig(dAtA, i, uint64(len(k)))
			i--
			dAtA[i] = 0xa
			i = encodeVarintConfig(dAtA, i, uint64(baseI-i))
			i--
			dAtA[i] = 0x12
		}
	}
	if m.Policy != nil {
		{
			size, err := m.Policy.MarshalToSizedBuffer(dAtA[:i])
			if err != nil {
				return 0, err
			}
			i -= size
			i = encodeVarintConfig(dAtA, i, uint64(size))
		}
		i--
		dAtA[i] = 0xa
	}
	return len(dAtA) - i, nil
}

func encodeVarintConfig(dAtA []byte, offset int, v uint64) int {
	offset -= sovConfig(v)
	base := offset
	for v >= 1<<7 {
		dAtA[offset] = uint8(v&0x7f | 0x80)
		v >>= 7
		offset++
	}
	dAtA[offset] = uint8(v)
	return base
}
func (m *FilterConfig) Size() (n int) {
	if m == nil {
		return 0
	}
	var l int
	_ = l
	if m.Policy != nil {
		l = m.Policy.Size()
		n += 1 + l + sovConfig(uint64(l))
	}
	if len(m.JwtOutputPayloadLocations) > 0 {
		for k, v := range m.JwtOutputPayloadLocations {
			_ = k
			_ = v
			mapEntrySize := 1 + len(k) + sovConfig(uint64(len(k))) + 1 + len(v) + sovConfig(uint64(len(v)))
			n += mapEntrySize + 1 + sovConfig(uint64(mapEntrySize))
		}
	}
	if m.SkipValidateTrustDomain {
		n += 2
	}
	if m.XXX_unrecognized != nil {
		n += len(m.XXX_unrecognized)
	}
	return n
}

func sovConfig(x uint64) (n int) {
	return (math_bits.Len64(x|1) + 6) / 7
}
func sozConfig(x uint64) (n int) {
	return sovConfig(uint64((x << 1) ^ uint64((int64(x) >> 63))))
}
func (m *FilterConfig) Unmarshal(dAtA []byte) error {
	l := len(dAtA)
	iNdEx := 0
	for iNdEx < l {
		preIndex := iNdEx
		var wire uint64
		for shift := uint(0); ; shift += 7 {
			if shift >= 64 {
				return ErrIntOverflowConfig
			}
			if iNdEx >= l {
				return io.ErrUnexpectedEOF
			}
			b := dAtA[iNdEx]
			iNdEx++
			wire |= uint64(b&0x7F) << shift
			if b < 0x80 {
				break
			}
		}
		fieldNum := int32(wire >> 3)
		wireType := int(wire & 0x7)
		if wireType == 4 {
			return fmt.Errorf("proto: FilterConfig: wiretype end group for non-group")
		}
		if fieldNum <= 0 {
			return fmt.Errorf("proto: FilterConfig: illegal tag %d (wire type %d)", fieldNum, wire)
		}
		switch fieldNum {
		case 1:
			if wireType != 2 {
				return fmt.Errorf("proto: wrong wireType = %d for field Policy", wireType)
			}
			var msglen int
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return ErrIntOverflowConfig
				}
				if iNdEx >= l {
					return io.ErrUnexpectedEOF
				}
				b := dAtA[iNdEx]
				iNdEx++
				msglen |= int(b&0x7F) << shift
				if b < 0x80 {
					break
				}
			}
			if msglen < 0 {
				return ErrInvalidLengthConfig
			}
			postIndex := iNdEx + msglen
			if postIndex < 0 {
				return ErrInvalidLengthConfig
			}
			if postIndex > l {
				return io.ErrUnexpectedEOF
			}
			if m.Policy == nil {
				m.Policy = &v1alpha1.Policy{}
			}
			if err := m.Policy.Unmarshal(dAtA[iNdEx:postIndex]); err != nil {
				return err
			}
			iNdEx = postIndex
		case 2:
			if wireType != 2 {
				return fmt.Errorf("proto: wrong wireType = %d for field JwtOutputPayloadLocations", wireType)
			}
			var msglen int
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return ErrIntOverflowConfig
				}
				if iNdEx >= l {
					return io.ErrUnexpectedEOF
				}
				b := dAtA[iNdEx]
				iNdEx++
				msglen |= int(b&0x7F) << shift
				if b < 0x80 {
					break
				}
			}
			if msglen < 0 {
				return ErrInvalidLengthConfig
			}
			postIndex := iNdEx + msglen
			if postIndex < 0 {
				return ErrInvalidLengthConfig
			}
			if postIndex > l {
				return io.ErrUnexpectedEOF
			}
			if m.JwtOutputPayloadLocations == nil {
				m.JwtOutputPayloadLocations = make(map[string]string)
			}
			var mapkey string
			var mapvalue string
			for iNdEx < postIndex {
				entryPreIndex := iNdEx
				var wire uint64
				for shift := uint(0); ; shift += 7 {
					if shift >= 64 {
						return ErrIntOverflowConfig
					}
					if iNdEx >= l {
						return io.ErrUnexpectedEOF
					}
					b := dAtA[iNdEx]
					iNdEx++
					wire |= uint64(b&0x7F) << shift
					if b < 0x80 {
						break
					}
				}
				fieldNum := int32(wire >> 3)
				if fieldNum == 1 {
					var stringLenmapkey uint64
					for shift := uint(0); ; shift += 7 {
						if shift >= 64 {
							return ErrIntOverflowConfig
						}
						if iNdEx >= l {
							return io.ErrUnexpectedEOF
						}
						b := dAtA[iNdEx]
						iNdEx++
						stringLenmapkey |= uint64(b&0x7F) << shift
						if b < 0x80 {
							break
						}
					}
					intStringLenmapkey := int(stringLenmapkey)
					if intStringLenmapkey < 0 {
						return ErrInvalidLengthConfig
					}
					postStringIndexmapkey := iNdEx + intStringLenmapkey
					if postStringIndexmapkey < 0 {
						return ErrInvalidLengthConfig
					}
					if postStringIndexmapkey > l {
						return io.ErrUnexpectedEOF
					}
					mapkey = string(dAtA[iNdEx:postStringIndexmapkey])
					iNdEx = postStringIndexmapkey
				} else if fieldNum == 2 {
					var stringLenmapvalue uint64
					for shift := uint(0); ; shift += 7 {
						if shift >= 64 {
							return ErrIntOverflowConfig
						}
						if iNdEx >= l {
							return io.ErrUnexpectedEOF
						}
						b := dAtA[iNdEx]
						iNdEx++
						stringLenmapvalue |= uint64(b&0x7F) << shift
						if b < 0x80 {
							break
						}
					}
					intStringLenmapvalue := int(stringLenmapvalue)
					if intStringLenmapvalue < 0 {
						return ErrInvalidLengthConfig
					}
					postStringIndexmapvalue := iNdEx + intStringLenmapvalue
					if postStringIndexmapvalue < 0 {
						return ErrInvalidLengthConfig
					}
					if postStringIndexmapvalue > l {
						return io.ErrUnexpectedEOF
					}
					mapvalue = string(dAtA[iNdEx:postStringIndexmapvalue])
					iNdEx = postStringIndexmapvalue
				} else {
					iNdEx = entryPreIndex
					skippy, err := skipConfig(dAtA[iNdEx:])
					if err != nil {
						return err
					}
					if skippy < 0 {
						return ErrInvalidLengthConfig
					}
					if (iNdEx + skippy) > postIndex {
						return io.ErrUnexpectedEOF
					}
					iNdEx += skippy
				}
			}
			m.JwtOutputPayloadLocations[mapkey] = mapvalue
			iNdEx = postIndex
		case 3:
			if wireType != 0 {
				return fmt.Errorf("proto: wrong wireType = %d for field SkipValidateTrustDomain", wireType)
			}
			var v int
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return ErrIntOverflowConfig
				}
				if iNdEx >= l {
					return io.ErrUnexpectedEOF
				}
				b := dAtA[iNdEx]
				iNdEx++
				v |= int(b&0x7F) << shift
				if b < 0x80 {
					break
				}
			}
			m.SkipValidateTrustDomain = bool(v != 0)
		default:
			iNdEx = preIndex
			skippy, err := skipConfig(dAtA[iNdEx:])
			if err != nil {
				return err
			}
			if skippy < 0 {
				return ErrInvalidLengthConfig
			}
			if (iNdEx + skippy) < 0 {
				return ErrInvalidLengthConfig
			}
			if (iNdEx + skippy) > l {
				return io.ErrUnexpectedEOF
			}
			m.XXX_unrecognized = append(m.XXX_unrecognized, dAtA[iNdEx:iNdEx+skippy]...)
			iNdEx += skippy
		}
	}

	if iNdEx > l {
		return io.ErrUnexpectedEOF
	}
	return nil
}
func skipConfig(dAtA []byte) (n int, err error) {
	l := len(dAtA)
	iNdEx := 0
	for iNdEx < l {
		var wire uint64
		for shift := uint(0); ; shift += 7 {
			if shift >= 64 {
				return 0, ErrIntOverflowConfig
			}
			if iNdEx >= l {
				return 0, io.ErrUnexpectedEOF
			}
			b := dAtA[iNdEx]
			iNdEx++
			wire |= (uint64(b) & 0x7F) << shift
			if b < 0x80 {
				break
			}
		}
		wireType := int(wire & 0x7)
		switch wireType {
		case 0:
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return 0, ErrIntOverflowConfig
				}
				if iNdEx >= l {
					return 0, io.ErrUnexpectedEOF
				}
				iNdEx++
				if dAtA[iNdEx-1] < 0x80 {
					break
				}
			}
			return iNdEx, nil
		case 1:
			iNdEx += 8
			return iNdEx, nil
		case 2:
			var length int
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return 0, ErrIntOverflowConfig
				}
				if iNdEx >= l {
					return 0, io.ErrUnexpectedEOF
				}
				b := dAtA[iNdEx]
				iNdEx++
				length |= (int(b) & 0x7F) << shift
				if b < 0x80 {
					break
				}
			}
			if length < 0 {
				return 0, ErrInvalidLengthConfig
			}
			iNdEx += length
			if iNdEx < 0 {
				return 0, ErrInvalidLengthConfig
			}
			return iNdEx, nil
		case 3:
			for {
				var innerWire uint64
				var start int = iNdEx
				for shift := uint(0); ; shift += 7 {
					if shift >= 64 {
						return 0, ErrIntOverflowConfig
					}
					if iNdEx >= l {
						return 0, io.ErrUnexpectedEOF
					}
					b := dAtA[iNdEx]
					iNdEx++
					innerWire |= (uint64(b) & 0x7F) << shift
					if b < 0x80 {
						break
					}
				}
				innerWireType := int(innerWire & 0x7)
				if innerWireType == 4 {
					break
				}
				next, err := skipConfig(dAtA[start:])
				if err != nil {
					return 0, err
				}
				iNdEx = start + next
				if iNdEx < 0 {
					return 0, ErrInvalidLengthConfig
				}
			}
			return iNdEx, nil
		case 4:
			return iNdEx, nil
		case 5:
			iNdEx += 4
			return iNdEx, nil
		default:
			return 0, fmt.Errorf("proto: illegal wireType %d", wireType)
		}
	}
	panic("unreachable")
}

var (
	ErrInvalidLengthConfig = fmt.Errorf("proto: negative length found during unmarshaling")
	ErrIntOverflowConfig   = fmt.Errorf("proto: integer overflow")
)
