#NAME : RAHUL AGRAWAL
# LEAKY BUCKET


import time
import random


storage=0; #initially bucket is empty
no_of_queries=int(input('Enter no of packet: '))
bucket_size=int(input('Enter bucket size: '))
#input_pkt_size=int(input('Enter input acket size: '))  
output_pkt_size=int(input('Enter bucket outgoing rate: '))  
for i in range(0,no_of_queries):
    print('\nPacket No ==> ',i+1,'\n')
    input_pkt_size = random.randint(bucket_size//2,bucket_size*1.5)
    print('Incomming Packet size = ', input_pkt_size)
    size_left=bucket_size-storage; #space left 
    if input_pkt_size <= size_left:          
        storage+=input_pkt_size 
        print("Buffer size is",storage," out of",bucket_size," bucket size")
    else:
        print("Packet loss :",(input_pkt_size-size_left)," out of",input_pkt_size)
        storage=bucket_size
        print('Buffer size is',storage,' out of',bucket_size,' bucket size')
    storage-=output_pkt_size
    print('After Outgoing : ',storage,' packets left out of',bucket_size)
    time.sleep(1)
    
