import socket
import os
import sys
import json

from dotenv import load_dotenv

from methodValidator import MethodValidator
from inputProcessor import InputProcessor


class RPC:
    def __init__(self):
        load_dotenv()
        self.client_address = os.environ['CLIENT_ADDRESS']
        self.server_address = os.environ['SERVER_ADDRESS'] 
        self.id_count = 1


    def create_socket(self):
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)


    def connect_server(self):
        try:
            self.sock.connect(self.server_address)
        except socket.error as err:
            print(err)
            sys.exit(1) 
            

    def create_request(self):
        method = ""
        params = []
        param_types = []

        while not MethodValidator.is_valid_comb(method, params, param_types):
            method, params, param_types = InputProcessor.get_inputs()
        
        request = {
            "method": method,
            "params": params,
            "param_types": param_types,
            "id": self.id_count
        }

        self.id_count += 1

        return request


    def write_into_server(self):
        self.sock.sendall((json.dumps(self.create_request())).encode())
    

    def grab_server_response(self):
        try:
            while True:
                data = self.sock.recv(4096)

                if data:
                    print('Server Responce: ' + str(data))
                else:
                    break
        finally:
            print('Closing socket')
            self.sock.close()


    def run(self):
        self.create_socket()
        print('Success to create socket.')
        self.connect_server()
        print('Establish connection with server.')
        self.write_into_server()
        print('Waiting for server response...')
        self.grab_server_response()


if __name__ == '__main__':
    rpc = RPC()
    rpc.run()

