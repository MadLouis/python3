"""
Print out a conversion table of temperatures from Fahrenheit
to Celsius degrees, with the former ranging from 0 to 300 in 
step of 20
"""

"""""
min_temp = 0
max_temp = 300
step = 20
# \t: A tab
print('Fahrenheit\tCelsius')  # perfect space in between

for fahrenheit in range (min_temp,max_temp+step,step):
    celsius = 5*(fahrenheit-32)/9
    print(f'{fahrenheit:10}\t{celsius:7.1f}')

"""

# celsius to fahrenheit

min_temp = 0
max_temp = 100
step = 10
# \t: A tab

print('Celsius\tFahrenheit')  # perfect space in between

for celsius in range (min_temp,max_temp+step,step):
    fahrenheit = celsius * 9//5 + 32
    print(f'{celsius:7d}\t{fahrenheit:10d}')
    


