weight  = input('what is your weight? ')
unit = input('kg or lb').lower()

if unit == 'kg' or unit == 'lb':
    print (f'your weight is {weight} in {unit}')
else:
    print ('try again')
