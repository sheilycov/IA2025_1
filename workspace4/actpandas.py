import pandas as pd # type: ignore

ser=pd.Series(data=[1,2,3,4,5],index=['tom','bob','juan','lucha','jackson'])

print(ser.index)
print('dayana' in ser)
print('before')
print(ser)
print('after')
print(ser*2)
print(ser)

ser=pd.Series(data=[100,200,300,400,500],index=['tom','bob','juan','lucha','jackson'])
print(ser[[2,4]])

print(ser['juan'])

print('PANDAS DATAFRAME')

df = {
    'one': pd.Series(data=[100, 200, 300], index=['apple', 'ball', 'clock']),
    'two': pd.Series([111, 222, 333], index=['apple', 'ball', 'cerill'])
}

df1 = pd.DataFrame(df)
print(df1)

print("Index: {}".format(df1.index))
print("Columns:", df1.columns)
print('---------------------------------------')

df1['there']=df1['one']*df1['two']
print(df1)
print('---------------------------------------')

df1['flag']=df1['one']>100
print(df1)

print('---------------------------------------')

aux=df1.pop('there')
print(df1)

print('---------------------------------------')

del df1['one']
print(df1)   

print('---------------------------------------')
#una copia de la columna 2 q va a pasar ser la 3
df1.insert(2, 'copy of two', df1['two'])
print(df1)
print('---------------------------------------')

df1['two_upper_half']=df1['two'][:2]
print(df1)

print('---------------------------------------')

df1['two_down_half']=df1['two'][2:4]
print(df1)



print('---------------------------------------')
print('    ')
print('CASE STRUDY: MOVIES DATA ANAYSIS')
print('     ')

import pandas as pd 
print('MOVIES')
movies=pd.read_csv('movies.csv')
print(movies.head(2))
print(movies.columns)
print(movies.index)
print(movies.shape)


print('     ')
print('TAGS')
tags=pd.read_csv('tags.csv')
print(tags.head(2))
print(tags.columns)
print(tags.index)
print(tags.shape)


print('     ')
print('RATINGS')
ratings=pd.read_csv('ratings.csv')
print(ratings.head(2))
print(ratings.columns)
print(ratings.index)
print(ratings.shape)


print('ok')


print('---------------------------------------')
print('     ')
print("TIMESTAMP VARIABlE WAS DELETED")
print('     ')

del ratings['timestamp']
del tags['timestamp']
print(ratings.head(2))
print(tags.head(2))

print('     ')
print('---------------------------------------')

print(tags.iloc[[0,11,200]])

print(ratings.head())
print(ratings.tail())

statistics=ratings['rating'].describe()
print(statistics)
print(ratings['rating'].mean())
print(ratings['rating'].min())
print(ratings['rating'].max())
print(ratings['rating'].median()) 
print(ratings['rating'].mode())

print("filtro")
filter=ratings['rating']>5
print(filter.any())

filter=ratings['rating']>0
print(filter.any())


print('---------------------------------------')
print("MOVIES")
print(movies.shape)
print(movies.isnull().any())

print('---------------------------------------')
print("RATINGS")
print(ratings.shape)
print(ratings.isnull().any())

print('---------------------------------------')
print("tags")
print(tags.shape)
print(tags.isnull().any())

# print('---------------------------------------')
# print("tags funcion para eliminar")
# tags=tags.dropna()

print('---------------------------------------')
print("DATA VISUALIZACION MATPLOTLIB")
import matplotlib.pyplot as plt
ratings.hist(column='rating',figsize=(15,10))
# plt.show()
print(ratings.head(10))
print(ratings.shape)
plt.show()