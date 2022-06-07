from multiprocessing import shared_memory as smm
import multiprocessing as mp

def a(xyz):
	name,t= xyz[0],xyz[1]
	arr=smm.ShareableList(name=name)
	if arr[1]==11:
		arr[1]=t
	else:arr[1]=11
	print(arr)
	arr.shm.close()
	arr.shm.unlink()

sl = smm.ShareableList(range(4))
print(sl)
name = sl.shm.name

xyz=[[name,11],[name,12]]
pool=mp.Pool()
try:
	pool.map(a,xyz)
except:pass
print(sl)
sl.shm.close()

