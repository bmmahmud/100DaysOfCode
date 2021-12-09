# Dictionary
alien = {'color': 'green','points':5}
new_points = alien['points']
# print("You just eanrd "+str(new_points)+" points!")

alien['x_position'] = 2
alien['y_position'] = 25
# print(alien)

#modify dic
alien['color'] = 'yellow'
# print("Alien is now "+alien['color'])

#Alien Game
alien_0 = {'x_position': 0, 'y_position':25, 'speed':'medium'}
# print("Orriginal X-position: "+str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

# print("New x-position: " + str(alien_0['x_position']))

## Remove item from Dic
# print(alien)
# del alien['points']
# print(alien)

# Assignment 6.1
person = {'name':'Ashik','age':28,'location':'Mirpur','zipcode':1216}
# for info in person:
    # print('Name: '+str(person['name']).title()+'\n'
    # 'Age: '+str(person['age'])+'\n'
    # 'Location: '+str(person['location'].title())+'\n'
    # 'Zipcode:'+str(person['zipcode'])+'.'
    # )

# Ass 6.2 with new loops
birthDate = {'Abir':11,'Lamia':8,'Ashik':8,'Rasel':24,'Shila':16,'Mim':17}
# for name,bdate in birthDate.items():
    # print(name.title()+"'s Birthday in June "+str(bdate)) 

## Only accress Key
# for name in birthDate.keys():
    # print(name)
## sorted key
# for name in sorted(birthDate.keys()):
#     print(name+" Hi their.")  

## print only values
# for age in birthDate.values():
#     print(age)
## WithOut repeatation 
# for age in set(birthDate.values()):
#     print(age)


### Nested Dic

aliens = []
# make 15 green aliens
for alien_number in range(0,5):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
# for alien in aliens[0:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['points'] = 10
#         alien['speed'] = 'medium'
# for alien in aliens[6:10]:        
#     if  alien['color'] == 'green':
#         alien['color'] = 'red'
#         alien['points'] = 15
#         alien['speed'] = 'Fast'    
# show the firs         
for alien in aliens[0:5]:
    print(aliens)
print('........')

# upto page 111