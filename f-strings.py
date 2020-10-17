## example 1 variable
firts_name = 'James'
last_name = 'Li'

# format method
sentence = 'My name is {} {}'.format(firts_name, last_name)
print(sentence)

# f string
sentence = f'My name is {firts_name} {last_name}'
print(sentence)

# f string with functions
sentence = f'My name is {firts_name.upper()} {last_name.upper()}'
print(sentence)

## example 2 dictionary
person = {'name': 'James', 'age': 29}

# format method
sentence = 'My name is {} and I am {} years old'.format(person['name'], person['age'])
print(sentence)

# f string method
sentence = f'My name is {person["name"]} and I am {person["age"]} years old'
print(sentence)

# f string with calculation 
calculation = f'17 times 59 is equal to {17*59}'
print(calculation)

# f string with loop and zero padded with 4 digits
for i in range(1,21):
	index = f'the index value is {i:04}'
	print(index)

# f string with float formating
import math
sentence = f'Pi is equal to {math.pi:.6f}'
print(sentence)

# f string with dates
from datetime import datetime

birthday = datetime(1991,1,1)

sentence = f'James has a birthday on {birthday:%B %d, %Y}'
print(sentence)





















