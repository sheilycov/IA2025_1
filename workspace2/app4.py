import numpy as np 


#arreglo de una dimension
a=np.array([1,2,3,4,5])

#shape significa formato
print(a.shape)
print('Element extracted of index 2: ', a[2])

#arreglo de dos dimensiones
b=np.array([[1,2,3],[11,22,33]])
print(b.shape)
print('Extracted element of row 1 and column 2:', b[1,2])

print(b)

print ("OK :)")

c=np.zeros((5,4))
print("The matrix x is: ")
print(c)


d=np.ones((3,4))
print("Matrix of values ones: ")
print(d)

e=np.full((3,4),8)
print("Matrix of a unique values")
print(e)
# type: ignore

f=np.random.randint(1,11,size=(5,5))
print(f)

print("___________________________________")


# print("Matrix G")
# g=np.random.random((5,5))
# print(g)
# filter1 & filter2
print("___________________________________")

print("Identifique matrix ")
h=np.eye(10)
print(h)


print("___________________________________")

print("SUBMATRIX")
f=np.random.randint(1,21,size=(3,4))
print(f)

m=f[:2,2:]
print(m)

print("___________________________________")

n=np.random.randint(1,101,size=(7,5))
print(n)
p=n[4:6,2:4]
print(p)


print("___________________________________")

o=n[2:5, 1:4]
print(o)


print("___________________________________")
k = n[[0, 0, -1, -1], [0, -1, 0, -1]]
print(k)

print("___________________________________")
# 0.0
# 6.0
# 6.4
# 0.4

h=n[[0,6,6,0],[0,0,4,4]]
print(h)
print(type)
print(h.shape)
print(h.ndim)


print("___________________________________")
p=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(p)
b=np.array([0,2,0,1])
a=np.arange(4)
#print(a)

print("___________________________________")
print(np.arange(4),b)
p[a,b]+=100
print(p)

print("___________________________________")
# Arrays de índices
b = np.array([0, 1, 2])  # Columnas de los elementos a modificar
a = np.array([0, 1, 2])  # Filas de los elementos a modificar

print("----")
print(np.arange(4), b)

# Alterar los valores 1, 5, 9 (en posiciones 0,0; 1,1; 2,2) sumando 200
p[a, b] += 200

print("\nMatriz después de agregar 200 a 1, 5 y 9:")
print(p)

filter=(p>5)
print(filter)
print (type(filter))
print(filter.ndim)
print(filter.shape)
z=p[filter]
print(type(z))
print(z.shape)
print(z.ndim)

print(z)

print("___________________________________")
filter=(p>5)
print(filter)
print(type(filter))
print(filter.ndim)
print(filter.shape)
z=p[filter]
print(type(z))
print(z.ndim)
print(z.shape)

print(z) 

print('FILTER VALUE FROM 40 TO 50')
f=np.random.randint(1,101,size=(15,15))
print(f)
print('*************')
filter1=(f>40)
filter2=(f<60)
f[filter1 & filter2]=0
print(f)
print(f.shape)
print (type(f))
print("___________________________________")
print("Matriz con valores entre 40 y 60 reemplazados por 0:")

f = np.random.randint(1, 101, size=(15, 15))  
print(f)

print("__________")

filter1=(f>40)
filter2=(f<60)
print('filter 1')
print (filter1)
print('filter 2')
print (filter2)
f[filter1 & filter2]=0
print(f)
print(f.shape)
print(type(f))

print("MATRIZ PARA REEMPLAZAR")
f = np.random.randint(1, 101, size=(7, 7))
print("Matriz original ")
print(f)

print('remplazo de numeros')
f[f % 10 == 0] = 200
print("matriz reemplazados por 200")
print(f)

print('IMPARES')
f = np.random.randint(1, 101, size=(3,3))
print(f)
p = f % 2 != 0
f[p] = f[p] ** 2
print(f)

print('MATRICES')
a = np.random.randint(1, 10, size=(2,2))
b = np.random.randint(1, 10, size=(2,2))
print('MATRIZ A')
print(a)
print('MATRIZ B')
print(b)

print('ADDING MATRICES')
adding_matrices=np.add(a,b)
print(adding_matrices)
print(a+b)
print(a-b)
print(a/b)
print(a*b)

aux1=np.subtract(a,b)
aux2=np.multiply(a,b)
aux3=np.divide(a,b)
aux4=np.sqrt(a)

print(aux3)

print('--------------------')
a = np.random.randint(1, 10, size=(3,3))
b = np.random.randint(1, 10, size=(3,3))
c=a.dot(b)
print(c)
print(c.shape)
print(c.ndim)


print('----------MATRICES----------')
a = np.random.randint(1, 10, size=(5,5))
b = np.random.randint(1, 10, size=(5,5))
h= np.dot(a,b)
print(h)

print('----------VECTORES----------')
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print(a)
print(b)

w=np.array([9,10])
v=np.array([11,12])

tmp1=np.dot(w,v)
tmp2=w.dot(v)

print(tmp1)
print(tmp2)
print(type(tmp1))
print(type(tmp2))
print(tmp2.shape)
print(tmp1.ndim)

print('----------producto de una matriz con vector----------')
tmp3=a.dot(v)
tmp4=np.dot(a,v)
print(type(tmp3))
print(tmp3.ndim)
print(tmp3.shape)

print('----------Matriz cuadrada de 2*2----------')
a = np.array([[1,2],[3,4]])
print(a)
result=np.sum(a)
print('the result of the sum the whole elements inside the matrix is: ',np.sum(a))

print('----------Matriz cuadrada de 15x15----------')

print('----------columnas----------')

g = np.random.randint(1, 21, size=(10,10))
print(g)
columns_sum=np.sum(g,axis=0)
print('The total elements of my column sum is:' ,columns_sum)
print(columns_sum.shape)
print('The total elements of my column sum is:' ,len(columns_sum))
print(columns_sum.ndim)
print('----------promedio de columnas----------')
print('promedio de columnas es' ,np.sum(f,axis=0)/len(np.sum(f,axis=0)))

print('promedio de columnas es' ,np.mean(f,axis=0))

print('promedio de columnas es' ,np.average(f,axis=0))

# print('----------filas----------')
# g = np.random.randint(1, 21, size=(15,15))
# print(g)
# filas_sum = np.sum(g, axis=1)
# print(filas_sum.shape)
# print('The total elements of my filas sum is:' ,len(filas_sum))
# print(filas_sum.ndim)
print('----------transpose matrix----------')
f = np.random.randint(1, 21, size=(4,4))
print(f)
print(f.T)

print('----------transpose matrix no cuadrada----------')
f = np.random.randint(1, 21, size=(4,9))
print(f)
print(f.T)

print('----------matriz 4x3----------')
x=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
v=np.array([1,0,1])
emptyMatrix=np.empty_like(x)

print(x)
print(v)
print(x.shape)
print('rows: ', x.shape[0])
# print('columns:', x.shape[1])

print('--------------------')
for i in range(x.shape[0]):
    emptyMatrix[i,:] = x[i,:] + v
print(emptyMatrix)

print('--------------------')
vv=np.tile(v,(4,1))
print(vv)
print(x+vv)

print('--------------------')
print(x+v)


print('--------------------')

# a=np.array([[1,3],[5,7],[9,11]])
# b=np.array([[2],[4],[6],[8]])
# c=np.hstack(a,b)
print("_____hstack y vstack_____")
#hstack (horizontal stack) y vstack (vertical stack)
x=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

# Vector columna (4 filas, 1 columna)
v_col = np.array([[100], [200], [300], [400]])
# Vector fila (1 fila, 3 columnas)
v_row = np.array([[10, 20, 30]])

result_hstack = np.hstack((x, v_col))
print("Resultado de hstack:")
print(result_hstack)

result_vstack = np.vstack((x, v_row))
print("Resultado de vstack:")
print(result_vstack)



