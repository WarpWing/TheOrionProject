import os
import io
import socket
import sys
import requests  
from apfunc import *
#Deploys the webserver on port 8888
HOST, PORT = '', 8888
# Cut this beauty out from docs. Probably going to rewrite it soon enough
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
# Reports Port Listening and Message
print(f'Serving the Admin Panel on port {PORT} ')
while True:
    client_connection, client_address = listen_socket.accept()
    request_data = client_connection.recv(1024)
    print(request_data.decode('utf-8'))

    http_response = b"""\
HTTP/1.1 200 OK

Hello!
"""
    client_connection.sendall(http_response)
    client_connection.close()

#systemsupport()