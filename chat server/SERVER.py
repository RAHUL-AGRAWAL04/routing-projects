
#This is Server program...

import socket        
from PIL import Image  #using this module to display Image.        

port = 12345                    
sock = socket.socket()             
host = socket.gethostname()     
sock.bind((host, port))            
sock.listen(5)                     

print('Server Waiting for client....')

while True:
    try:
        connection, addr = sock.accept()     
    except:
        print('\nShutting Down server...')
        break
    print('Got connection from', addr)
    
    print('Client Requesting...')
    with open('ClientRequest', 'wb') as f:
        print('file opened')
        while True:
            data = connection.recv(1024)
            f.write(data)
            if len(data)<1024:
	              break
    f.close()
    print('\nA connection created between server and client\n')
    
    print('\n...Image received by client...\n')
    Image.open('ClientRequest').show()
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    print('Responding to Client...')
    filename='/home/rahul/Desktop/CN_LAB/EXPT04/respond.png'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       connection.send(l)
       l = f.read(1024)
    f.close()

    print('Responded to Client')
    connection.send('Thank you for connecting'.encode())
    connection.close()

