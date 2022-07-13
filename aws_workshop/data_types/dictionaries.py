# mutable data type
user = {'first_name':'Ada'}
print(user)
print(user['first_name'])

# adding a value
user['family_name'] = 'Lovelace'
print(user)

# delete a value
del user['first_name']
print(user)