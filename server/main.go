package main

import (
	"context"
	"encoding/json"
	"io/ioutil"
	"log"
	"net"
	"net/http"

	"github.com/aleksandarmilanovic/pygo-grpc/server/digimons"
	"google.golang.org/grpc"
)

//Server ...
type Server struct {
	digimons.UnimplementedDiginfoServer
}
//Search ...
func (Server) Search(ctx context.Context, request *digimons.Digiquest) (response *digimons.Digisponse, err error) {
	resp, err := http.Get("https://digimon-api.vercel.app/api/digimon/name/" + request.Name)

	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	jsonData, err := ioutil.ReadAll(resp.Body)

	if err != nil {
		return nil, err
	}
	var digimon []digimons.Digisponse
	if err := json.Unmarshal(jsonData, &digimon); err != nil {
		return nil,err
	}
	return &digimon[0], nil
}

func main() {

	grpcServer := grpc.NewServer()

	var server Server

	digimons.RegisterDiginfoServer(grpcServer, server)

	listen, err := net.Listen("tcp", "0.0.0.0:8080")
	if err != nil {
		log.Fatalf("Failed to listen to 0.0.0.0:8080 %v",err)
	}

	log.Println("Server starting")
	log.Fatal(grpcServer.Serve(listen))
}