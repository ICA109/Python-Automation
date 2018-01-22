myPets = ['Porky', 'Rover', 'Max', 'Alvin']

print('Enter a pet name:')
name = input()

if name in myPets:
    print(name + ' is my pet.')
else:
    print('I do not have a pet named ' + name)
