#Notes - alter item, set new item at last by append, 
# and insert new item


# item = ["apple","banana","grave",'mango']
# print(item[-4].upper())

# #assignment
# print('my favourite frout is '+item[0].title())

## Adding item in a list
# item = ['honda','yamaha','suzuki']
# print(item)
# item[0] = 'ducati' # alter item
# print("added item:"+str(item))
# #remove
# item.append('toyota')
# print("new item at end:"+str(item))

# items = []
# items.append('apple')
# items.append('orange')
# items.append('mango')
# items.append('watermalon')
# print(items)
# #insert
# items.insert(3,'New Apple')
# print(items)
## removeig items
# del items[3]
# print(items)
# popped_items = items.pop()
# print(items)
# print(popped_items)
# popped_items = items.pop()
# print(items)
# print(popped_items)
# popped_items = items.pop()
# print(items)
# print(popped_items)

# items.remove('New Apple')
# print(items)

# ## Assisnment 3.4 and 3.5
print("Lis t of Invited 3 people for Dinner:")
names = []
names.append('ashik')
names.append('abir')
names.append('lamia')
invitation = 'You are Invited in my Dinner.'
print(names[0].title(),",\n",invitation)
print(names[1].title(),",\n",invitation)
print(names[2].title(),",\n",invitation)
popped = names.pop(1)
names.append('Emma')
print(popped.title(),',\n Is Unable to attend the party.')
print(names[2].title(),",\n",invitation)
print('Lists of all Members:',names)
names.insert(0,'Lola')
names.insert(2,'Chichi')
names.append('fife')
print(names)

# ## Removie By POP
# motorcycles = ['honda','yamaha','suzuki']
# print(motorcycles)

# last item
# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)

# remove specific item
# first_owned = motorcycles.pop(0)
# print('The first motorcycle I owned as a '+ first_owned.title() +'.') 