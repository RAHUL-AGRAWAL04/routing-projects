from multiprocessing import shared_memory as smm
import multiprocessing as mp

dt=0
buff = 5
ack=''
	
def a(t):
	global dt
	print('At time=',dt,'\nFrame is at router- a')
	name,p1 = t[1][0], t[1][1]
	b=smm.ShareableList(name=name)
	if b[0]<buff:
		if buff-b[0]<=p1:
			b[0] += buff-b[0]
		else:
			b[0] += p1 
		print('At time=',dt,'\nBuffer capacity of router-a',b[0])
	else:
		print('At time=',dt,'\nAt router-a BufferOverFlow..')
		t[1][1] = buff
	dt =dt + p1
	t[0].pop(0)
	print()
	if t[0][0]=='b' : ack=b(t)
	elif t[0][0] == 'c' : ack=c(t)
	elif t[0][0]=='d' : ack=d(t)
	elif t[0][0]=='e' : ack=e(t)
	elif t[0][0]=='r' : ack=r(t)
	b.shm.close()
	b.shm.unlink()
	return ack


def b(t):
	global dt
	print('At time=',dt,'\nFrame is at router- b')
	name,p1 = t[1][0], t[1][1]
	b=smm.ShareableList(name=name)
	if b[1]<buff:
		if buff-b[1]<=p1:
			b[1] += buff-b[1]
		else:
			b[1] += p1 
		print('At time=',dt,'\nBuffer capacity of router-b',b[1])
	else:
		print('At time=',dt,'\nAt router-b BufferOverFlow..')
		t[1][1] = buff
	dt = dt + p1
	t[0].pop(0)
	print()
	if t[0][0] == 'a' : ack=a(t)
	elif t[0][0] == 'c' : ack=c(t)
	elif t[0][0]=='d' : ack=d(t)
	elif t[0][0]=='e' : ack=e(t)
	elif t[0][0]=='r' : ack=r(t)
	b.shm.close()
	b.shm.unlink()
	return ack

def c(t):
	global dt
	print('At time=',dt,'\nFrame is at router- c')
	name,p1 = t[1][0], t[1][1]
	b=smm.ShareableList(name=name)
	if b[2]<buff:
		if buff-b[2]<=p1:
			b[2] += buff-b[2]
		else:
			b[2] += p1 
		print('At time=',dt,'\nBuffer capacity of router-c',b[2])
	else:
		print('At time=',dt,'\nAt router-c BufferOverFlow..')
		t[1][1] = buff
	dt = dt + p1
	t[0].pop(0)
	print()
	if t[0][0] == 'a' : ack=a(t)
	elif t[0][0]=='b' : ack=b(t)
	elif t[0][0]=='d' : ack=d(t)
	elif t[0][0]=='e' : ack=e(t)
	elif t[0][0]=='r' : ack=r(t)
	b.shm.close()
	b.shm.unlink()
	return ack

def d(t):
	global dt
	print('At time=',dt,'\nFrame is at router- d')
	name,p1 = t[1][0], t[1][1]
	b=smm.ShareableList(name=name)
	if b[3]<buff:
		if buff-b[3]<=p1:
			b[3] += buff-b[3]
		else:
			b[3] += p1 
		print('At time=',dt,'\nBuffer capacity of router-d',b[3])
	else:
		print('At time=',dt,'\nAt router-d BufferOverFlow..')
		t[1][1] = buff
	dt = dt+p1
	t[0].pop(0)
	print()
	if t[0][0] == 'a' : ack=a(t)
	elif t[0][0]=='b' : ack=b(t)
	elif t[0][0] == 'c' : ack=c(t)
	elif t[0][0]=='e' : ack=e(t)
	elif t[0][0]=='r' : ack=r(t)
	b.shm.close()
	b.shm.unlink()
	return ack

def e(t):
	global dt
	print('At time=',dt,'\nFrame is at router- e')
	name,p1 = t[1][0], t[1][1]
	b=smm.ShareableList(name=name)
	if b[4]<buff:
		if buff-b[4]<=p1:
			b[4] += buff-b[4]
		else:
			b[4] += p1 
		print('At time=',dt,'\nBuffer capacity of router-e',b[4])
	else:
		print('At time=',dt,'\nAt router-e BufferOverFlow..')
		t[1][1] = buff
	dt = dt+p1
	t[0].pop(0)
	print()
	if t[0][0] == 'a' : ack=a(t)
	elif t[0][0]=='b' : ack=b(t)
	elif t[0][0] == 'c' : ack=c(t)
	elif t[0][0]=='d' : ack=d(t)
	elif t[0][0]=='r' : ack=r(t)
	b.shm.close()
	b.shm.unlink()
	return ack

def r(t):
	global dt
	name,p1 = t[1][0], t[1][1]
	b=smm.ShareableList(name=name)
	xyz=['a','b','c','d','e']
	print('At time=',dt,'\nFrame is sent to receiver client\n')
	dt = dt+p1
	t[0].pop(0)
	sp1=str(p1)+'\r\n\r\n'
	clientsocket.sendall(sp1.encode())
	ack=''
	ack = clientsocket.recv(512)
	return ack.decode()

def transmit(frame):		
	paths=[
	['s','a','d','r'],
	['s','a','e','c','d','r'],
	['s','a','e','r'],
	['s','a','b','d','r'],
	['s','a','b','r'],
	['s','b','d','r'],
	['s','b','r'],
	['s','c','d','r']
	]
	import random
	import multiprocessing as mp
	select = random.randint(0,7)
	route = paths[select][:]
	t=(route,frame)
	t[0].pop(0)
	if t[0][0] == 'a' : a(t)
	elif t[0][0]=='b' : b(t)
	elif t[0][0] == 'c' : c(t)
	elif t[0][0]=='d' : d(t)
	elif t[0][0]=='e' : e(t)
	elif t[0][0]=='r' : r(t)
	print('asdfgfdsa')
	return ack	


import pyfiglet as p
result  = p.figlet_format('ROUTE')
print(result)	

sl = smm.ShareableList([0,0,0,0,0])
print(sl)
name = sl.shm.name

from socket import *
serversocket = socket(AF_INET, SOCK_STREAM)
try:
	serversocket.bind(('127.0.0.1',9000))
	serversocket.listen(5)
	while(True):
		(hostsocket,address) = serversocket.accept()
		(clientsocket,addr) = serversocket.accept()
		while True:
			cnt = hostsocket.recv(512).decode()
			print(cnt,'-packets received from host for transmission..')
			print('Routing and sending data to client...')
			array=[]
			for i in range(int(cnt[:2])):
				array.append([name,1])
				
			print('\nROUTE OF TRANSMISSION...\n')
			
			pool=mp.Pool()
			try:
				ack = pool.map(transmit,array)
				print(ack)
				pool.join()
				pool.close()
			except:pass
			for i in ack:
				if i=='':hostsocket.sendall('NONE\r\n\r\n'.encode())
				else : 
					print('Transmitting ACK to host...')
					hostsocket.sendall(str(i)+'\r\n\r\n'.encode())
			break
except KeyboardInterrupt:
	print('\nShutting down...');
except Exception as exc:
	print('Error:\n')
	print(exc)
serversocket.close()

sl.shm.close()

