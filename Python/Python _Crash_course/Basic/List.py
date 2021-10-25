#Notes - alter item, set new item at last by append, 
# and insert new item


# item = ["apple","banana","grave",'mango']
# # print(item[-2].upper())

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

## Assisnment 3.4
print("Invite 3 people for Dinner.\n Enter name:")
names = []
names.append('Ashik')
names.append('Abir')
names.append('Lamia')
invitation = 'You are Invited in my Dinner.'
print(names[0],",\n",invitation)
print(names[1],",\n",invitation)
print(names[2],",\n",invitation)
print(names[1],',\n Is Unable to attend the party.')
names[1]='Emma'
print(names[1],",\n",invitation)
print('Lists of all Members:',names)