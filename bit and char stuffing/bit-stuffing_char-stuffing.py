

###   CHARACTER STUFFING FUNCTIONS DEFINATIONS   ####
def stuffChar(flag, message):	##This defination is used to stuff esc characters where ever needed
	result = ''
	result += flag
	for msg in message:
		if msg == flag:
			result =result + flag + msg
		else:
			result += msg
	result += flag
	return result						##return the msg with stuffed char
	
def destuffChar(flag, message):		##This defination is used to de-stuff the stuffed characters
	msg = list(message)
	result = ''
	track = 0			##track variable is used to track of esc character
	if msg[0] == flag and msg[-1] == flag:
		for i in range(1,len(msg)-1):
			if  msg[i] == flag and track==0:
				msg[i]=''		##de-stuffing stuffed char
				track=1
			else: track = 0			
	else:
		print('Broken Frame...')	
	return (''.join(msg[1:len(msg)-1]))	#returns the original msg
	
	
###   BIT STUFFING FUNCTIONS DEFINATIONS   ###
def createBitString(message):		##This defination is used to create bit sequence from a string
	bit_string = ''
	for c in message:
		'''
		Ascii value is represented as 7-bit binary sequence.
		format() function returns 6-bit binary sequence if ascii value is less than 64.
		In order to balance the sequence of 7 , '0' bit is added if ascii value < 64 
		'''
		if ord(c) < 64:			
			bit_string += '0'
		bit_string += ''.join(format(ord(c),'b'))
	return bit_string
	
def createAsciiString(bit_string):	##This defination is used to create string from a bit sequence
	result = ''
	for i in range(0,len(bit_string),7):
		c = chr(int(bit_string[i:i+7], 2))
		result += c
	#print(result)
	return result
	
def stuffBit(message):		#This function is used to stuff bit as an esc bit where ever needed
	msg = list(message)
	count = 0
	i = 0
	while i != len(msg):
		if msg[i] == '1':
			count += 1
		else : count = 0
		if count == 5:
			msg.insert(i+1,'0')
			count = 0
		i += 1
		
	return (''.join(msg))

def destuffBit(message):	#This function is used to destuff the stuffed bits
	msg = list(message)
	count = 0
	i = 0
	while i != len(msg):
		if msg[i] == '1':
			count += 1
		else : count = 0
		if count == 5:
			msg.pop(i+1)
			count = 0
		i += 1
		
	return (''.join(msg))


###   DRIVER CODE   ###
choice = -1

while True :
	choice = int(input('\nSelect From Below...\n[0] EXIT\n[1] CHARACTER STUFFING\n[2] BIT STUFFING\n>>>'))
	if choice == 0:break
	elif choice == 1:
		message = input('Input Data to send: ')
		flag = input('Flag character: ')
		print()
		stuffed_message = stuffChar(flag, message)
		print('Data after character stuffing: '+ stuffed_message)
		destuffed_message = destuffChar(flag, stuffed_message)
		print('Data after character de-stuffing: '+ destuffed_message)
	elif choice == 2:
		message = input('Input Data to send: ')
		bit_string = createBitString(message)
		print('Bit String: '+bit_string+'\n')
		stuffed_bit_msg = stuffBit(bit_string)
		print('Bit String after Bit Stuffing: '+stuffed_bit_msg+'\n')
		print('Data after Bit Stuffng:',createAsciiString(stuffed_bit_msg))
		destuffed_bit_msg = destuffBit(stuffed_bit_msg)
		print('Bit String after Bit destuffing: '+destuffed_bit_msg+'\n')
		print('Data after De-stuffing:',createAsciiString(destuffed_bit_msg))
	else:
		print(r'Select from the options provided...')



				######   END OF CODE   ######


