

#Importing modules.
from socket import *
import time
from multiprocessing import shared_memory as smm
import multiprocessing as mp

myID = '1\r\n\r\n'	#Alloted Static Identification Number
leader = 0					#Initially leader is not defined

#This section defines Server Mode of Node.
def serverMode(name):
	global leader
	#Acessing common list
	peer_lead = smm.ShareableList(name=name)
	
	#Creating socket for server.
	serversocket = socket(AF_INET, SOCK_STREAM)
	try:
		#Binding server Socket on port=9001
		serversocket.bind(('127.0.0.1',9001))
		serversocket.listen(5)
		while(True):
			#Accecpting connections from other two peers.
			(clientsocket1,address) = serversocket.accept()
			(clientsocket2,address) = serversocket.accept()
			
			#Receiving Peer's Identification Number
			Peer1_ID = clientsocket1.recv(1024).decode()
			Peer2_ID = clientsocket2.recv(1024).decode()	
			
			#Appending ID's to common list in order to break extra p2p connection(s)
			peer_lead[1] = int(Peer1_ID[0])
			peer_lead[2] = int(Peer2_ID[0])		
			
			#Selection of leader with Min Identificaton Number.
			if int(myID[0]) < int(Peer1_ID[0]) and int(myID[0]) < int(Peer2_ID[0]) : 
				leader = int(myID[0])
			elif int(Peer1_ID[0]) < int(myID[0]) and int(Peer1_ID[0]) < int(Peer2_ID[0]) : 
				leader = int(Peer1_ID[0])
			else:
				leader = int(Peer2_ID[0])
			
			#Appending leader's ID in common list.
			peer_lead[0]=leader
			time.sleep(0.1)
			print('Leader : Node -',leader)
			
			time.sleep(0.2)
			#Logic for closing extra p2p Server connection channel as leader is elected.
			#Also logs of files along with peer details on p2p network is maintained here.
			if leader == int(myID[0]):
				#File with leader Node.
				path='/home/rahul/Desktop/CN/CN_ASSIGNMENT/59_ASSIGNMENT2/NODE1/'
				log=[(path,'Node1_file.txt\r\n\r\n',serversocket)]
				
				#Sending send cmd to peer in order to receive file logs of peer.
				clientsocket1.sendall('send\r\n\r\n'.encode())
				#Receiving peer's file log and appending it to leader's log database.
				str1 = clientsocket1.recv(512).decode()	
				with open(path+'Node2_file.txt','w') as f:
					while True:
						data = clientsocket1.recv(1024).decode()
						f.write(data)
						if len(data)<1024:
							break
				
				log.append((path,str1,clientsocket1))
				
				#Sending send cmd to peer in order to receive file logs of peer.
				clientsocket2.sendall('send\r\n\r\n'.encode())
				#Receiving peer's file log and appending it to leader's log database.	
				str2 = clientsocket2.recv(512).decode()
				with open(path+'Node3_file.txt','w') as f:
					while True:
						data = clientsocket1.recv(1024).decode()
						f.write(data)
						if len(data)<1024:
							break
				log.append((path,str2,clientsocket2))
				
				#displaying File logs in p2p netowrk.
				print('\n... Files on p2p network ...')
				for i in log:
					print(i)
					
			elif leader == peer_lead[1]:
				clientsocket2.shutdown(SHUT_WR)
				print('Connection between Node1 and Node3 is closed...')					
			elif leader == peer_lead[2]:
				clientsocket1.shutdown(SHUT_WR)		
				print('Connection between Node1 and Node2 is closed...')							
			
	except KeyboardInterrupt:
		print('\nShutting down...');
	except Exception as exc:
		print('Error:',exc)
		
	#closing Common list and server socket.
	peer_lead.shm.close()
	peer_lead.shm.unlink()
	serversocket.close()
	return
	
#This section defines client mode of a Node.
def clientMode(name):
	time.sleep(2)
	#Acessing Common list
	peer_lead = smm.ShareableList(name=name)
		
	#creating two sockets for Connecting with peers.
	peer2_sock = socket(AF_INET, SOCK_STREAM)
	peer3_sock = socket(AF_INET, SOCK_STREAM)

	#Connecting with other two peers.
	peer2_sock.connect(('127.0.0.1',9002))
	peer3_sock.connect(('127.0.0.1',9003))
	
	#Sharing ID with other two peers.
	print('Node-1 sending its ID=1 to both Peer...')
	peer2_sock.sendall(myID.encode())
	peer3_sock.sendall(myID.encode())
	
	time.sleep(3)
	#Logic for closing extra p2p client connection channel as leader is elected.
	#Sending Log data to leader as leader has to keep track of files in p2p n/w.
	
	if peer_lead[0] == int(myID[0]):	#If Node 1 is leader No need to break any connection.
		pass
	elif peer_lead[0] == peer_lead[1]: 
		#If peer2 is leader, breaking connection between node1 and peer3.
		peer3_sock.close()
		print('Connection between Node1 and Node3 is closed...')	
		
		#Waiting for send cmd from leader
		scrap=peer2_sock.recv(512)			
		#Sending log data to leader
		peer2_sock.sendall('Node1_file.txt\r\n\r\n'.encode())	
		path='/home/rahul/Desktop/CN/CN_ASSIGNMENT/59_ASSIGNMENT2/NODE1/'
		with open(path+'Node1_file.txt') as f:
			while True:
				try:
					data=f.read(1024)
					data = peer1_sock.sendall(data.encode())
					if len(data)<1024:
						break
				except:break
		time.sleep(0.1)
		print('Data shared with Leader Node...')	
	elif peer_lead[0] == peer_lead[2]:
		#If peer3 is leader, breaking connection between node1 and peer2.
		peer2_sock.close()  
		print('Connection between Node1 and Node2 is closed...')
		
		#Waiting for send cmd from leader
		scrap=peer3_sock.recv(512)			
		#Sending log data to leader
		peer3_sock.sendall('Node1_file.txt\r\n\r\n'.encode())	
		path='/home/rahul/Desktop/CN/CN_ASSIGNMENT/59_ASSIGNMENT2/NODE1/'
		with open(path+'Node1_file.txt') as f:
			while True:
				try:
					data=f.read(1024)
					data = peer1_sock.sendall(data.encode())
					if len(data)<1024:
						break
				except:break
		time.sleep(0.1)
		print('Data shared with Leader Node...')
		
	print('Shutting down Client Mode...')
	peer_lead.shm.close()
	peer_lead.shm.unlink()
	return


#Creating a common list acessible by both the mode of the Node.
sl = smm.ShareableList(range(3))
name = sl.shm.name

#To run Dual mode of the node in parallel, Node uses 2 thread representing each node.
#Thread of individual mode is created and executed.
sp = mp.Process(target=serverMode, args=(name,))
cp = mp.Process(target=clientMode, args=(name,))

sp.start()
cp.start()
sp.join()
cp.join()

#Common list is destroyed when Node is taken down
sl.shm.close()







	


