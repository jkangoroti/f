import math
from os import name
from unittest import result

name = input (" what is your name: ")
forc = input (f'hello {name},would you like f or c: ')  

#print (f"hello, {name} would you like f or c") # f string

temp = int(input ("what is the temperature: ")) 

#convertedf = result('the temperature in Celsius is:'),
#convertedc = result('the temperature in Fahrenheit is :'),

if forc == 'f':
    print ((temp) * 9/5 + 32)
elif forc == 'c':
   print((temp) -32 * 5/9)

else:
    print('not a f or c')
    