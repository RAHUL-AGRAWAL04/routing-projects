  
def calcRedundantBits(m): 
  
    # Use the formula 2 ^ r >= m + r + 1 
    # to calculate the no of redundant bits. 
    # Iterate over 0 .. m and return the value 
    # that satisfies the equation 
  
    for i in range(m): 
        if(2**i >= m + i + 1): 
            return i 
  
  
def placeRedundantBits(data, r): 
  
    # Redundancy bits are placed at the positions 
    # which correspond to the power of 2.  
    data = list(data)
   
    for i in range(r): 
        data.insert((2**i)-1,'0')
            
    return ''.join(data)
  
  
def findHammingCode(data, r): 
    n = len(data) 
    data = list(data)
    # For finding rth parity bit, iterate over 
    # 0 to r - 1 
    for i in range(r): 
       temp = []
       for j in range((2**i)-1,len(data),(2**i)*2):
           temp += data[j:j + 2**i ]

       if temp.count('1') % 2 :
           data[(2**i)-1] = '1'
    return ''.join(data )
  
  
def detectError(data, nr): 
    n = len(data) 
    data = list(data)
    err_pos = 0
    
    # For finding rth parity bit, iterate over 
    # 0 to r - 1 
    
    for i in range(r): 
       temp = []
       for j in range((2**i)-1,len(data),(2**i)*2):
           temp += data[j:j + 2**i ]

       if temp.count('1') % 2 :
           err_pos += 2**i
    return err_pos
  
  
  
  
  
  
  
######   DRIVER CODE   ######

#Below 2 lines of code is just for decoration. 
#It doesn't affect any of the functionality.
#Comment below 2 lines if code shows unable to load module 'pyfiglet'.

import pyfiglet as p
print(p.figlet_format('B2 - 59  Hamming Code Demonstration...'))

#Do not comment from here..


# Enter the data to be transmitted 
data = input('Enter the bit string: ')
  
# Calculate the no of Redundant Bits Required 
r = calcRedundantBits(len(data)) 
print('No of parity Bits:',r)

# Determine the positions of Redundant Bits 
data = placeRedundantBits(data, r) 
print('Rough Hamming Code: ' + data)

# Determine the Hamming Code
data = findHammingCode(data, r) 
print('Hamming Code: ' + data)   

received_data = input('Bit String at reveiver side: ')
err_pos = detectError(received_data, r) 

if err_pos==0:
    print('No Error Detected...')
else:
    print('Error at: ' + str(err_pos)) 












