import socket as s
import time as t
from threading import Thread
server = s.socket(s.AF_INET, s.SOCK_STREAM)
host = '192.168.0.141'
port = 33000
server.connect((host, port))
if __name__ == '__main__':
    print('connecting...')
    server.send(bytes('Sai', 'utf-8'))
    time.sleep(5)
    server.send(bytes('sem', 'utf-8'))
    while True:
        pass