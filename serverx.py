import socket as s
from threading import Thread
'''
setting up the server
buiding dictionaries
'''
class persons:
    def __init__(self,name,pas):
        self.name = name 
        self.pas = pas
        print(f'{self.name} has joined the chat, password: {self.pas}')
    def send(self):
        pass
    def recieve(self):
        pass
clients = {}
addr = []
server = s.socket(s.AF_INET, s.SOCK_STREAM)
host = '192.168.0.141'
port = 33000
server.bind((host, port))
#----------------defining functions----------------------------------------------------------
def accept():
    while True:
        client,clientaddr= server.accept()
        a = Thread(target=handle, args=(client,))
        a.start()
def handle(client):
    name = client.recv(1024).decode('utf-8')
    clients[client] = name
    addr.append(name)
    xml = client.recv(1024).decode('utf-8')
    client = persons(name,xml)
    client.send(bytes(addr, 'utf-8'))
    while True:
        m = client.recv(1024)
        if m == bytes('quit', 'utf-8'):
            client.send(bytes('Logged out', 'utf-8'))
            client.close()
            del clients[client]
            addr.remove(name)
        else:
            broadcast(m, prefix=name+':')
            print(name, ':', m.decode('utf-8'))
def broadcast(msg, prefix=''):
    for i in clients:
        i.send(bytes(prefix, 'utf-8') + msg)
'''
running the server
calling functions
'''
if __name__ == '__main__':
    server.listen(5)
    print('waiting for connection...')
    t = Thread(target=accept)
    t.start()
    t.join()
server.close()