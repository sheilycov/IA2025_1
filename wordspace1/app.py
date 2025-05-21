#!/usr/bin/env python3
#Hello my friends 
# THis is the way to create comments


print("Este es mi primer mensaje my friends")



variable1=120
variable2=15.6
variable3= True
variable4= 'Sheily Coveña'

print(variable1)
print(variable2)
print(variable3)
print(variable4)

#lista

print ('#Lista')
lista1=[1,2,3,4,6,7,'Sheily Coveña', True]
print(lista1[5])
print(lista1[6])

# diccionario
print ('#Diccionario')
dict1={'student1': 'Sheily Coveña', 'student2':'Kevin Prado'}
print(dict1['student2'])


stingVariable='3'
print (type(stingVariable))
numericalVariable=int(stingVariable) 
print (type(numericalVariable))

print ('-----------------------')


print("CONTROL FLOW")

age=30
message1='you are younger'
message2='you are old'

if age>=25:
    print(message2)
else:
    print(message1)
print ('-----------------------')   

if age>30:
    print(message2)
elif age<30:
    print(message1)
elif age==30:
    print('you have th right age, congratulations')

print ('-----------------------')   
for i in lista1:
    print('Elements inside the list', i)


print ('-----------------------')  

print ('how to iterate diccionay')
for key in dict1:
    print(dict1[key])

print ('-----------------------')  

print ('FUNCIONES')  

def message():
    print('Hello from the function message')

message()

for i in range(5):
    message()



# name=input ('Enter your name:')
# age=int (input ('Enter your age:'))


# def message1 (age,name):
#     print("You are young !!!")
#     print(f'Your name is {name} and your age is {age}')

# def message2 (age,name):
#     print("You are old !!!")
#     print(f'Your name is {name} and your age is {age}')

# def message2(age,name)
# else:
#     message3(age,name)age3 (age,name):
#     print("You are young !!!")
#     print("You are old !!!")
#     print(f'Your name is {name} and your age is {age}')

# if age<30:
#     message1(age,name)
# elif age>50:
#     mess

# while True:
#     name = input('Enter your name: ')
#     age = int(input('Enter your age: '))

#     def message1(age, name):
#         print("You are young !!!")
#         print(f'Your name is {name} and your age is {age}')

#     def message2(age, name):
#         print("You are old !!!")
#         print(f'Your name is {name} and your age is {age}')

#     def message3(age, name):
#         print("You are young !!!")
#         print("You are old !!!")
#         print(f'Your name is {name} and your age is {age}')

#     if age < 30:
#         message1(age, name)
#     elif age > 50:
#         message2(age, name)
#     else:
#         message3(age, name)


lista1=[1,2,3,4,5]
listsquared=[]

for item in lista1:
    listsquared.append(item**2)

for item in listsquared:
    print(item)

import math

listsquarenumbers=[]

for item in lista1:
    listsquarenumbers.append(math.sqrt(item))

print ('SQUARE ROOT FROM MY IST')
for i in listsquarenumbers:
    print (i)


