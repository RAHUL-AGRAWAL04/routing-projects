

'''
--> ALL FUNCTION DEFINED IS A ROUTER WITHIN ITSELF. ROUTER-S IS A PACKET SENDER ROUTER
--> ROUTER-R IS THE PACKET RECEIVER ROUTER

-->INSIDE ROUTER(FUNCTION)..
    ->multi-threading is used to flood neighbour router
    ->DEF ROUTER(TASK):
        connected=['a','b','c']     #TRACK OF NEIGHBOUR ROUTER.
        frame[-1]-=1    #DECREMENTING COUNTER OF PACKET BY 1
        IF COND:        #FOR EXECUTNG PART-1
        
            IF:         #CHECKING WETHER COUNTER IS > ZERO
            
            #FLOODING CODE.
            
            ELSE:       #IF COUNTER=0 DISCARDING PACKET
            
        ELIF COND:         #FOR EXECUTING PART-2
        
        ELIF COND:          #FOR EXECUTING PART-3
        .
        .
        .


'''

import multiprocessing as mp
from random import randint 

def s(task):
    connected=['a','b','c']
    part,sender,frame = task[0],task[1],task[2]
    print('[*] Mode=',part,'; Packet:',frame[0],'; Generates at router-S')
    frame[-1]-=1    
    if part==1:
        if frame[-1]>0:
            print('[+] Packet:',frame[0],'; Flooded to:',connected)
            p1=mp.Process(target=a, args=([part,'s',frame],))
            p2=mp.Process(target=b, args=([part,'s',frame],))
            p3=mp.Process(target=c, args=([part,'s',frame],))
            
            p1.start()
            p2.start()
            p3.start()
            p1.join()
            p2.join()
            p3.join()
        else:print('[-] Packet:',frame[0],'; Discarded(counter=0) at Router-S')
            
    elif part==2:
        if frame[-1]>0:
            print('[+] Packet:',frame[0],'; Flooded to:',connected,' Except Router:',sender)
            p1=mp.Process(target=a, args=([part,'s',frame],))
            p2=mp.Process(target=b, args=([part,'s',frame],))
            p3=mp.Process(target=c, args=([part,'s',frame],))
            
            p1.start()
            p2.start()
            p3.start()
            p1.join()
            p2.join()
            p3.join()
        else:print('[-] Packet:',frame[0],'; Discarded(counter=0) at Router-S')
    
    elif part==3:
        if frame[-1]>0:
            print('[+] Packet:',frame[0],'; Flooded to: [b,c]')
            p2=mp.Process(target=b, args=([part,'s',frame],))
            p3=mp.Process(target=c, args=([part,'s',frame],))
            p2.start()
            p3.start()
            p2.join()
            p3.join()
        else:print('[-] Packet:',frame[0],'; Discarded(counter=0) at Router-S')
    
    
    
def a(task):
    connected=['s','b','e','d']
    part,sender,frame = task[0],task[1],task[2]
    print('[*] Mode=',part,'; Packet:',frame[0],'; Arrived at router-A')
    frame[-1]-=1    
    if part==1:
        if frame[-1]>0:
            print('[+] Packet:',frame[0],'; Flooded to:',connected)
            p1=mp.Process(target=s, args=([part,'a',frame],))
            p2=mp.Process(target=b, args=([part,'a',frame],))
            p3=mp.Process(target=e, args=([part,'a',frame],))
            p4=mp.Process(target=d, args=([part,'a',frame],))
            p1.start()
            p2.start()
            p3.start()
            p4.start()
            p1.join()
            p2.join()
            p3.join()
            p4.join()
        else:print('[-] Packet:',frame[0],'; Discarded(counter=0) at Router-A')
            
    elif part==2:
        if frame[-1]>0:
            print('[+] Packet:',frame[0],'; Flooded to:',connected,' Except Router:',sender)
            p=[]
            for i in connected:
                if i==sender:continue
                elif i=='s':
                    x=mp.Process(target=s, args=([part,'a',frame],))
                    p.append(x)
                    x.start()
                elif i=='b':
                    y=mp.Process(target=b, args=([part,'a',frame],))
                    p.append(y)
                    y.start()
                elif i=='e':
                    z=mp.Process(target=e, args=([part,'a',frame],))
                    p.append(z)
                    z.start()
                elif i=='d':
                    w=mp.Process(target=d, args=([part,'a',frame],))
                    p.append(w)
                    w.start()
            p[0].join()
            p[1].join()
            p[2].join()               
        else:print('[-] Packet:',frame[0],'; Discarded(counter=0) at Router-A')
    
    elif part==3:
        if frame[-1]>0:
            print('[+] Packet:',frame[0],'; Flooded to: [e,d]')
            p2=mp.Process(target=e, args=[part,'a',frame])
            p3=mp.Process(target=d, args=[part,'a',frame])
            p2.start()
            p3.start()
            p2.join()
            p3.join()
        else:print('[-] Packet:',frame[0],'; Discarded(counter=0) at Router-A')
    


def b(task):
    connected=['s','a','d','r']
    part,sender,frame = task[0],task[1],task[2]
    print('[*] Mode=',part,'; Packet:',frame[0],'; Arrived at router-B')
    frame[-1]-=1    
    if part==1:
        if frame[-1]>0:
            print('[+] Packet:',frame[0],'; Flooded to:',connected)
            p1=mp.Process(target=s, args=([part,'b',frame],))
            p2=mp.Process(target=a, args=([part,'b',frame],))
            p3=mp.Process(target=r, args=([part,'b',frame],))
            p4=mp.Process(target=d, args=([part,'b',frame],))
            p1.start()
            p2.start()
            p3.start()
            p4.start()
            p1.join()
            p2.join()
            p3.join()
            p4.join()
        else:print('[-] Packet:',frame[0],'; Discarded(counter=0) at Router-B')
            
    elif part==2:
        if frame[-1]>0:
            print('[+] Packet:',frame[0],'; Flooded to:',connected,' Except router:',sender)
            p=[]
            for i in connected:
                if i==sender:continue
                elif i=='s':
                    x=mp.Process(target=s, args=([part,'b',frame],))
                    p.append(x)
                    x.start()
                elif i=='a':
                    y=mp.Process(target=a, args=([part,'b',frame],))
                    p.append(y)
                    y.start()
                elif i=='r':
                    z=mp.Process(target=r, args=([part,'b',frame],))
                    p.append(z)
                    z.start()
                elif i=='d':
                    w=mp.Process(target=d, args=([part,'b',frame],))
                    p.append(w)
                    w.start()
            p[0].join()
            p[1].join()
            p[2].join()               
        else:print('[-] Packet:',frame[0],'; Discarded(counter=0) at Router-B')
    
    elif part==3:
        if frame[-1]>0:
            print('[+] Packet:',frame[0],'; Flooded to: [r]')
            r([part,'b',frame])
        else:print('[-] Packet:',frame[0],'; Discarded(counter=0) at Router-B')


def c(task):
    connected=['s','e','d']
    part,sender,frame = task[0],task[1],task[2]
    print('[*] Mode=',part,'; Packet:',frame[0],'; Arrived at router-C')
    frame[-1]-=1    
    if part==1:
        if frame[-1]>0:
            print('[+] Packet:',frame[0],'; Flooded to:',connected)
            p1=mp.Process(target=s, args=([part,'c',frame],))
            p2=mp.Process(target=e, args=([part,'c',frame],))
            p4=mp.Process(target=d, args=([part,'c',frame],))
            p1.start()
            p2.start()
            p4.start()
            p1.join()
            p2.join()
            p4.join()
        else:print('[-] Packet:',frame[0],'; Discarded(counter=0) at Router-C')
            
    elif part==2:
        if frame[-1]>0:
            print('[+] Packet:',frame[0],'; Flooded to:',connected,' Except router:',sender)
            p=[]
            for i in connected:
                if i==sender:continue
                elif i=='s':
                    x=mp.Process(target=s, args=([part,'c',frame],))
                    p.append(x)
                    x.start()
                elif i=='e':
                    y=mp.Process(target=e, args=([part,'c',frame],))
                    p.append(y)
                    y.start()
                elif i=='d':
                    z=mp.Process(target=d, args=([part,'c',frame],))
                    p.append(z)
                    z.start()
            p[0].join()
            p[1].join()            
        else:print('[-] Packet:',frame[0],'; Discarded(counter=0) at Router-C')
    
    elif part==3:
        if frame[-1]>0:
            print('[+] Packet:',frame[0],'; Flooded to: [d]')
            d([part,'c',frame])
        else:print('[-] Packet:',frame[0],'; Discarded(counter=0) at Router-C')


#pending...
def d(task):
    connected=['a','b','c','r']
    part,sender,frame = task[0],task[1],task[2]
    print('[*] Mode=',part,'; Packet:',frame[0],'; Arrived at router-D')
    frame[-1]-=1    
    if part==1:
        if frame[-1]>0:
            print('[+] Packet:',frame[0],'; Flooded to:',connected)
            p1=mp.Process(target=a, args=([part,'d',frame],))
            p2=mp.Process(target=b, args=([part,'d',frame],))
            p3=mp.Process(target=c, args=([part,'d',frame],))
            p4=mp.Process(target=r, args=([part,'d',frame],))
            p1.start()
            p2.start()
            p3.start()
            p4.start()
            p1.join()
            p2.join()
            p3.join()
            p4.join()
        else:print('[-] Packet:',frame[0],'; Discarded(counter=0) at Router-D')
            
    elif part==2:
        if frame[-1]>0:
            print('[+] Packet:',frame[0],'; Flooded to:',connected,' Except router:',sender)
            p=[]
            for i in connected:
                if i==sender:continue
                elif i=='a':
                    x=mp.Process(target=a, args=([part,'d',frame],))
                    p.append(x)
                    x.start()
                elif i=='b':
                    y=mp.Process(target=b, args=([part,'d',frame],))
                    p.append(y)
                    y.start()
                elif i=='c':
                    z=mp.Process(target=c, args=([part,'d',frame],))
                    p.append(z)
                    z.start()
                elif i=='r':
                    w=mp.Process(target=r, args=([part,'d',frame],))
                    p.append(w)
                    w.start()
            p[0].join()
            p[1].join()  
            p[2].join()          
        else:print('[-] Packet:',frame[0],'; Discarded(counter=0) at Router-D')
    
    elif part==3:
        if frame[-1]>0:
            print('[+] Packet:',frame[0],'; Flooded to: [r]')
            r([part,'d',frame])
        else:print('[-] Packet:',frame[0],'; Discarded(counter=0) at Router-D')


def e(task):
    connected=['a','c','r']
    part,sender,frame = task[0],task[1],task[2]
    print('[*] Mode=',part,'; Packet:',frame[0],'; Arrived at router-E')
    frame[-1]-=1    
    if part==1:
        if frame[-1]>0:
            print('[+] Packet:',frame[0],'; Flooded to:',connected)
            p1=mp.Process(target=a, args=([part,'e',frame],))
            p3=mp.Process(target=c, args=([part,'e',frame],))
            p4=mp.Process(target=r, args=([part,'e',frame],))
            p1.start()
            p3.start()
            p4.start()
            p1.join()
            p3.join()
            p4.join()
        else:print('[-] Packet:',frame[0],'; Discarded(counter=0) at Router-E')
            
    elif part==2:
        if frame[-1]>0:
            print('[+] Packet:',frame[0],'; Flooded to:',connected,' Except router:',sender)
            p=[]
            for i in connected:
                if i==sender:continue
                elif i=='a':
                    x=mp.Process(target=a, args=([part,'e',frame],))
                    p.append(x)
                    x.start()
                elif i=='c':
                    z=mp.Process(target=c, args=([part,'e',frame],))
                    p.append(z)
                    z.start()
                elif i=='r':
                    w=mp.Process(target=r, args=([part,'e',frame],))
                    p.append(w)
                    w.start()
            p[0].join()
            p[1].join()            
        else:print('[-] Packet:',frame[0],'; Discarded(counter=0) at Router-E')
    
    elif part==3:
        if frame[-1]>0:
            print('[+] Packet:',frame[0],'; Flooded to: [r]')
            r([part,'e',frame])
        else:print('[-] Packet:',frame[0],'; Discarded(counter=0) at Router-E')


def r(task):
    part,sender,frame = task[0],task[1],task[2]
    frame[-1] -= 1
    print('[++] Received Packet:',frame[0],end='')
    print('; Prev Router:',sender,end='')
    print('; Counter:',frame[-1])
    

n=1
print('[#] This program will demonstrate the flooding algorithm in routing.')
print('[#] For the routing graph kindly read README.pdf file.')
print('[#] Program uses total 1 packet for the demonstration purpose.')
print('[#] Program automatically assigns the counter(0-5) to the packet(s).')
print('[#] You are supposed to enter the mode from the provided menu. ')
print('[#] Routing Logs will be displayed on the screen. You can study it to understand flood routing\n')
mode=-1
while mode!=0:
    print('\nEnter Mode from below...\n[0] Exit\n[1] All lines flooded')
    print('[2] All lines except input line are flooded\n[3] Only Best K-lines are flooded.')
    mode=int(input('>>>'))
    if mode==0:break
    tasks=[mode,'',[1,randint(2,5)]]
    s(tasks)











