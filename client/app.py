from flask import Flask, jsonify

app = Flask(__name__)

import grpc
import digimons_pb2
import digimons_pb2_grpc

def obj_to_dict(obj):return obj.__dict__

@app.route('/', methods=['GET'])
def index():
    return({'msg': 'Client works'})

@app.route('/<digimon>',methods=['GET'])
def search(digimon):
    print('Start service...')
    try:
        channel = grpc.insecure_channel('localhost:8080')
        stub = digimons_pb2_grpc.DiginfoStub(channel)
        digiquest = digimons_pb2.Digiquest(name=digimon)
        digisponse = stub.search(digiquest)

        return jsonify({
            "name": digisponse.name,
            "img": digisponse.img,
            "level": digisponse.level
        })
        
        channel.close()

    except Exception as e:
        print(e)
        return jsonify('Error while searching...')

if __name__ == '__main__':
    app.run()