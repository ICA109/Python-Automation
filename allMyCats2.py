myCats = []

i = 0
while True:
    print('Enter the name of cat ' + str(i) + ' (Or enter nothing to stop.)')
    name = input()

    if name == '':
        break
    else:
        myCats = myCats + [name]
        i = i+1

print('The cat names are:')
for aCat in myCats:
    print(' ' + aCat)
