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
print(alien)
del alien['points']
print(alien)
