import numpy as np
print(np.__version__)
np.show_config()
Z = np.zeros(10)
print(Z)
Z = np.zeros((10,10))
print("%d bytes" % (Z.size * Z.itemsize))
print(Z.itemsize)
Q = np.ones(10)
print(Q)
ll = 3
A = np.full(13,ll)
print(A)
Z1 = np.arange(10,50)
print(Z1)
Z2 = np.zeros(13)
Z2[4] = 4
print(Z2)
Z4 = np.arange(10)
print(Z4)
Z4 = Z4[::-1]
print(Z4)
Z5 = np.arange(27).reshape(3,3,3)
print(Z5)
nz = np.nonzero([1,2,0,0,4,0])
print(nz)
Z34 = np.ones_like(Z5)
print(Z34)
Z12 = np.full_like(Z5,9)
print(Z12)
Z33 = np.eye(3)
print(Z33)
Z66 = np.random.random((3,3,3))
print(Z66)
Z223 = np.random.random((10,10))
print(Z223)
Zmin, Zmax = Z223.min(), Z223.max()
print(Zmin, Zmax)
Z2232 = np.random.random(30)
print(Z2232)
m = Z2232.mean()
print(m)
