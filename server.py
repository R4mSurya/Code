import socket

port = 53
ip = '192.168.43.131'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip, port))

#def createResponse(data):



while 1:
    data,addr = sock.recvfrom(512)
    print(data, addr)
    sock.sendto(b'hello', addr)