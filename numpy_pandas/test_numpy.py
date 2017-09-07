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
