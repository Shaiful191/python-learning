# Core module
import datetime
from datetime import date 
from time import time

#pip module
from camelcase import CamelCase 

# Custom module
import validator
from validator import validate_email

# today=datetime.date.today()
today=date.today()
print(today)

timestamp=time()
print(timestamp)


"""
Run in command:
pip3 install camelcase
for use 3rd parti module

"""
c = CamelCase()
print(c.hump('hello there world'))

email='test@gmail.com'
if validate_email(email):
    print('Email is valid')
else:
    print('Email is bad')

