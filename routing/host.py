import socket
import time,random

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.settimeout(10.0)
mysock.connect(('127.0.0.1',9000))

import pyfiglet as p
result  = p.figlet_format('HOST')
print(result)

print('Sending Data To client...\nData : Host Here!!\n')
time.sleep(1)

pkt_count = random.randint(15,30)
cnt = str(pkt_count) + '\r\n\r\n'
mysock.send(cnt.encode())
while True:
	try:
		data = mysock.recv(512)
	except socket.timeout:
		print('Timeout.. \nResending packet...')
		mysock.send(cnt.encode())
		continue
	except KeyboardInterrupt:break
	print('ACK Received From Client :',data.decode())


print('[+] ALL OK\n[*] Visit route.py output for viewing hops.')	
mysock.close()
