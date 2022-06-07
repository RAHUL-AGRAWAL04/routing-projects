
#This is client program...

import socket                   
import time
from PIL import Image #using this module to display Image.

s = socket.socket()             
host = socket.gethostname()     
port = 12345                    

s.connect((host, port))  #connection to server

print('Requesting...')
filename='/home/rahul/Desktop/CN_LAB/EXPT04/request.png'
f = open(filename,'rb')
l = f.read(1024)
while (l):
   s.send(l)
   l = f.read(1024)
f.close()

time.sleep(1)

print('\nA connection created between client and server\n')
print('Receiving data from server...')
with open('ServerResponse', 'wb') as f:
    while True:
        data = s.recv(1024)
        if not data:
            break
        f.write(data)
f.close()

print('Successfully received response image from server..')
s.close()
print('connection closed')

print('\n...Image received from server...\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
Image.open('ServerResponse').show()
