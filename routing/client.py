import socket
import time

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('127.0.0.1',9000))

import pyfiglet as p
result  = p.figlet_format('CLIENT')
print(result)

while True : 
	try:
		data = mysock.recv(512)
		print('Data Received From Host :',data.decode(),end='')
		print('To Host : ACK')
		mysock.send('ACK\r\n\r\n'.encode())
	except:break
print('Closing Connection...\n')
mysock.close()
