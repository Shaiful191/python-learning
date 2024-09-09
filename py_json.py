import json

userJson='{"first_name":"Shaiful","last_name":"Islam","age":30}'

# Parse json to dictionary:
user=json.loads(userJson)
print(user)
print(user['first_name'])

car = {'make':'Ford','model':'Mustang','year':1970}
# Parse dictionary to json:
carJson = json.dumps(car)
print(carJson)