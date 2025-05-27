import pandas as pd

ser=pd.Series(data=[1,2,3,4,5], index=['tom','juan','kevin','sheily','winston'])

print(ser.index)
print('***************')
print('maria' in ser)

print('before')
print(ser)
print('after')
#print(ser*2)
#print(ser)
print('***************')
print(ser**2)

ser=pd.Series(data=[100,200,300,400,500], index=['tom','juan','kevin','sheily','winston'])
print(ser[[2,4]])

print(ser['kevin'])


print('******PANDAS DATAFRAME *********')
df={'one':pd.Series(data=[100,200,300], index=['apple','ball','clock']), 'two':pd.Series([111,222,333],
['apple','ball','cerill'])}
df1 =pd.DataFrame(df)
print(df1)

print("Index {}".format(df1.index))
print(df1.columns)

df1['three']=df1['one']*df1['two']
print(df1)
print('******FILTRO *********')
df1['flag']=df1['one']>100
print(df1)

aux=df1.pop('three')
print(df1)

del df1['one']
print (df1)

print('******COPIA DE FILA 2 *********')
df1.insert(2,'copy of two', df1['two'])
print(df1)

df1['two_upper_half']=df1['two'][:2]
print(df1)

df1['two_down_half']=df1['two'][2:]
print(df1)

