numbers = [1,2,3,4,5]
fruits = ['apples', 'bananas','oranges']

print(fruits)
print(fruits[0])
print(len(fruits))

# returns last value
print(fruits[-1]) 

# update (add)
fruits.append('pears')
print(fruits)

# update (add to a specific point in the list)
fruits.insert(3, 'watermelons')
print(fruits)

# organizining a list - does not alter the original order of the list
print(sorted(fruits))

# sort method to permanently sort the list
fruits.sort()
print(fruits)

# reverse the order
fruits.reverse()
print(fruits)

# delete an element by index
del fruits[3]
print(fruits)