import numpy as np

a=np.array([2,23,4], dtype=np.int)

b=np.array([[2,3,4],[4,5,6]])

c = np.zeros((3,4))
d = np.ones((3,4),dtype=np.int)
e = np.empty((3,4))
f = np.arange(10,20,2)
g = np.arange(12).reshape((3,4))
h = np.linspace(1,10,20)



print(a.dtype)
print(b.shape)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)

A = np.arange(14,2,-1).reshape(3,4)

print(A)
print(np.clip(A,5,9))#截断

##index

print(A[2])
print(A[1,1:3])
print(A.flatten())

##数组合并
A = np.array([1,1,1])
B = np.array([2,2,2])

print(np.vstack((A,B)))
print(np.hstack((A,B)))
print(A)
print(A[np.newaxis,:])
print(A[:,np.newaxis])
A = np.array([1,1,1])[:,np.newaxis]
B = np.array([2,2,2])[:,np.newaxis]
C = np.concatenate((A,B,B,A), axis=1)
print("con:")
print(A)
print(C)

##数组split

A= np.arange(12).reshape((3,4))

print(np.split(A,3,axis=0))
print(np.array_split(A,3,axis=1))

##copy

a = np.arange(4)

b=a
a[0]=11
b[1]=10
print(a)
print(b)

c=a.copy()
a[3]=11
print(a)
print(c)

