import numpy as np

print(np.__version__)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a = np.array(matrix, dtype=np.int32)

print(a)
print(a.shape)
print(a.ndim)
print(a.dtype)
print(a.dtype.itemsize)
print(a.strides)
# a.astype(int)
print(a.reshape(1, 9))
print(a.flatten())
print(a.ravel())
print('transpose:')
print(a.T)  # print(a.transpose())
print(a[1, 1])  # good, bad - a[1][1]
print(a[[1, 2], :][:, [1, 2]])  # copy
print(a[np.ix_([1, 2], [1, 2])])  # view

print('\n --- 1 \n')

b = np.arange(5)
print(b)
print(b[np.newaxis, :])  # b.reshape(1, *b.shape)
print(np.expand_dims(b, axis=0))
print(b[:, np.newaxis])  # b.reshape(*b.shape, 1)
print(b[np.newaxis, np.newaxis].shape)

print('\n --- 2 \n')

print(np.zeros(shape=(2, 5)))
print(np.zeros_like(a))
print(np.ones(5))  # np.ones(shape=(5, ))
print(np.eye(4))  # diagonal arr
print(np.arange(1, 10, 2))  # odd int arr
print(np.linspace(1, 10, 4, endpoint=True))

print('\n --- 3 \n')

c = np.array([10, 20, 30, 40, 50])
print(c ** 2)  # np.power(c, 2)
print(c * 2)  # np.multiply(c, 2)
print(c + 2)  # np.add(c, 2)
print(np.sqrt(c))
print(np.exp(c))
print(np.log(1 + c))
print(np.log2(1 + c))
print(np.sin(c))
print(c > 0)  # np.greater(c, 0)

print(c.min())  # np.min(c)
print(c.max())
print(c.argmax())
print(c.sum())
print(c.prod())
print(c.mean())  # avg
print(c.any())
print(c.all())

print(a.sum(axis=0))  # action by column
print(a.sum(axis=1))  # action by row

print(np.fmax(b, c))
print(c > b)  # np.greater(c, b)
print(b + c)
print(np.isclose(b, c))

print('\n --- 4 \n')

bm = np.matrix([[1, 2], [3, 4]])
cm = np.matrix([[5, 6], [7, 8]])

print(np.matmul(bm, cm))
print(np.dot(bm, cm))
print(bm * cm)
print(bm + cm)

print('\n --- 5 \n')

c = np.array([[-2, -1, 0, 1, 2]])
print(c[c < 0])  # find all less 0, the same - c[np.where(c < 0)]
print(c[c % 2 == 0])
print(c[0, 0])

print('\n --- 6 \n')

print(np.random.rand(10))
print(np.random.randint(0, 10, 10))
print(np.random.permutation(10))
print(np.random.choice(10, size=10))

print('\n --- 6 \n')

d = np.random.choice(10, size=(4, 4))
print(np.sort(d.ravel()))  # copy
d.sort(axis=0)  # column sort, index sort - d.argsort(axis=0)
d.sort(axis=1)  # row sort, index sort - d.argsort(axis=1)
print(d)
print(np.unique(d))

print('\n --- 7 \n')

e = np.random.choice(100, size=(4, 4))
f = np.random.choice(100, size=(4, 4))
print(e)
print(f)
print(np.concatenate((e, f), axis=0))
print(np.concatenate((e, f), axis=1))
print(np.vstack((e, f)))
print(np.hstack((e, f)))
