def c(z):
	print(z)

def b(y):
	print(y)
	c(y)
	return y

def a(x):
	print('a')
	b(x)
	return x


from multiprocessing import Pool
p=Pool()
x=p.map(a,[1,2])
print(x)
