phone = input('phone: ')
#             '1234'
digits_mapping={
    '1': 'One',
    '2': 'TWo',
    '3': 'Three',
    '4': 'Four'
}
output = ''
for ch in phone:
    output += digits_mapping.get(ch, "n/a") + " " # get(..,'n/a') 
print(output)