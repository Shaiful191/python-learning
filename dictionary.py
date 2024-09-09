# A dictionary is a collection 
# it same map in dart

person={
    'firstName':'Shaiful',
    'lastName':'Islam',
    'age':24
}

print(person)
print(person['firstName'])

person['phone']='01994393939'

# Get dictionary keys
print(person.keys())
# Get dictionary values
print(person.values())
# Get dictionary items
print(person.items())

print(len(person))

del(person['age'])
print(person)

person.clear()
print(person)

#List of dictionary:
people=[
    {'name':'Shaiful','age':24},
    {'name':'Sobuj','age':27},
    {'name':'Pervez','age':29},
]

print(people)
print(people[1]['name'])