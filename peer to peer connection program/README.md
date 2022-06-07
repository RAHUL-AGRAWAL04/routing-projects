# peer to peer connection program

## PROBLEM STATEMENT:
    The goal of your programming assignment is to build a very simple peer-to-peer system involving three nodes using sockets. You need to write
    programs that run on three nodes and achieve the following task.
        ● Elect a node among the three as the leader. The leader node is a peer but keeps track of the files available on the p2p network
          together with the IP addresses and port numbers from where they could be obtained.
        
        Leader Election: Assign identification numbers to each node, setup TCP connections among the three nodes, exchange the identification numbers
        and choose the node with the lowest identity as the leader. The other two peers should now remove any connections they have between
        themselves. In setting up the TCP connections you might have to order the server and client functionality across the three nodes.

## SPECIFICATIONS :
1. Each node contains two mode i.e. a)Server Mode and b)Client Mode
2. Both modes are executed in parallel using threads.
3. Generally, Server Mode is used to receive data from peers and Client Mode is used to send data to peers
4. Once leader is elected p2p connection between other peers is taken down
5. All peers send their data to the leader as leader should have all the data of p2p network.
6. Leader store files in its folder named .../NODE1/
7. Leader maintains the log of data in the form of array.

## STEPS TO FOLLOW :
1. Clone the folder in your desired location
2. Open program, edit path variable and set it to the path according to your system.
3. Open 3 terminals and set path to the directory where you have cloned the folder
4. Run the following cmd
    1. Python3 Node1.py
    2. Python3 node2.py
    3. Python3 node3.py
5. After the execution of program press CTRL+C or CTRL+D in each terminal to terminate the execution of program 

## OUTPUT :
1. All Node show the Identification Number of the leader.
2. Leader Node will print file logs that include path,file_name and name of peer in the console.
3. A folder is dedicated to each Node. Name of folder is as follows:
    1. For Node-1 Folder name is NODE1
    2. For Node-2 Folder name is NODE2
    3. For Node-x Folder name is NODEx
4. You can visit to the leader’s folder to verify the execution of program.