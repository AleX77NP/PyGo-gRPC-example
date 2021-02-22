// Code generated by protoc-gen-go-grpc. DO NOT EDIT.

package digimons

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

// DiginfoClient is the client API for Diginfo service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type DiginfoClient interface {
	Search(ctx context.Context, in *Digiquest, opts ...grpc.CallOption) (*Digisponse, error)
}

type diginfoClient struct {
	cc grpc.ClientConnInterface
}

func NewDiginfoClient(cc grpc.ClientConnInterface) DiginfoClient {
	return &diginfoClient{cc}
}

func (c *diginfoClient) Search(ctx context.Context, in *Digiquest, opts ...grpc.CallOption) (*Digisponse, error) {
	out := new(Digisponse)
	err := c.cc.Invoke(ctx, "/digimons.Diginfo/search", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// DiginfoServer is the server API for Diginfo service.
// All implementations must embed UnimplementedDiginfoServer
// for forward compatibility
type DiginfoServer interface {
	Search(context.Context, *Digiquest) (*Digisponse, error)
	mustEmbedUnimplementedDiginfoServer()
}

// UnimplementedDiginfoServer must be embedded to have forward compatible implementations.
type UnimplementedDiginfoServer struct {
}

func (UnimplementedDiginfoServer) Search(context.Context, *Digiquest) (*Digisponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Search not implemented")
}
func (UnimplementedDiginfoServer) mustEmbedUnimplementedDiginfoServer() {}

// UnsafeDiginfoServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to DiginfoServer will
// result in compilation errors.
type UnsafeDiginfoServer interface {
	mustEmbedUnimplementedDiginfoServer()
}

func RegisterDiginfoServer(s grpc.ServiceRegistrar, srv DiginfoServer) {
	s.RegisterService(&Diginfo_ServiceDesc, srv)
}

func _Diginfo_Search_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(Digiquest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(DiginfoServer).Search(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/digimons.Diginfo/search",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(DiginfoServer).Search(ctx, req.(*Digiquest))
	}
	return interceptor(ctx, in, info, handler)
}

// Diginfo_ServiceDesc is the grpc.ServiceDesc for Diginfo service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var Diginfo_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "digimons.Diginfo",
	HandlerType: (*DiginfoServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "search",
			Handler:    _Diginfo_Search_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "digimons.proto",
}