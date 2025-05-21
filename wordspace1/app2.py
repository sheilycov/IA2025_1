

# pairs key and the other value

myDictonary={'cat':'cute','dog':'friends','donkey':'hard-working'}

print(myDictonary['donkey'])

print('cat' in myDictonary)

myDictonary['fish']='wet'

for key in myDictonary:
    value=myDictonary[key]
    print ('The %s is %s'%(key,value))

print("Another way to print dictionaries")

for key, value in myDictonary.items():
    print ('the %s is %s '%(key,value))


# dictionary={'1':1, '2':4}

# myDictonary1={i:i**2 for i in range(20)}
# print(myDictonary1)

print('*****************************************')
dictionary = {str(i): i**2 for i in range(1, 21)}
for key, value in dictionary.items():
    print(f"The {key} is {value}")

print('*****************************************')

print ('SET CONTAINER')
animals={'cat','dog','chicken','hen','monkey'}
print('fish'in animals)
animals.add('fish')
print(animals)
animals.add('mouse')
print(animals)

print('*****************************************')
numberOfElements=len(animals)
print(numberOfElements)

print('*****************************************')

animals.remove('cat')
print(animals)
print(type(animals))
print(len(animals))

print('*****************************************')

print('TRUPLES')
tupleData=(5,5,5)
print(type(tupleData))

print('*****************************************')
tupleData = (3,6,9,12,15,18,21,24)
listData = list(tupleData)
listData.remove(15)  
tupleData = tuple(listData)
print(tupleData)

