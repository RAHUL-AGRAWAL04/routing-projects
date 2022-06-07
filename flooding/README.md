# Flooding

IMG--

S : SENDER
R : RECEIVER
A,B,C,D,E : ROUTERS

## QUESTION :
Write a program to simulate routing using flooding. Each packet should contain a counter
that is decremented on each hop. When the counter gets to zero, the packet is discarded.
Time is discrete, with each line handling one packet per time interval.
a) Write a program for all lines are flooded.
b) Write a program for all lines except the input line are flooded
c) Write a program for only the (statically chosen) best k lines are flooded


## EXPLANATION:
1. This program will demonstrate the flooding algorithm in routing.
2. Program uses total 1 packet for the demonstration purpose.
3. Program automatically assigns the counter(0-5) to the packet(s).
4. You are supposed to enter the mode from the provided menu.
5. Multi-threading is used to flood neighbour router.
6. Routing Logs will be displayed on the screen.
7. You can study it to understand flood routing


## OVERVIEW:
For the demonstration purpose, I have pre-set few things,
1. Number of packets = 1
2. Transmission time = 1 unit
This project is command-line based and demonstrates computer network routing for discrete
time interval.


## STEPS TO FOLLOW:
1. Download/Place route.py, host.py and client.py file in the same folder
2. Run the file in the following order: route.py-> host.py -> client.py
3. If you are using Linux based system then -
    1. Open your terminal (3-terminal)
    2. Set your current working directory to the folder where you have stored the program
    3. Type this command
    4. Python3 flooding.py (In terminal 1)
4. User must give input as asked while executing the program
5. To exit the program press CTRL+D or CTRL+C or you can enter 0 once the cmd prompt is asking for input
6. If you are using Windows based system then -
    1. Open any python IDE based on python3 and run the program.