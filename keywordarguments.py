def greet_user(name,age):  # argument is the value that we supply to function
    print(f'Hi louis {name},i am {age}')


print('start')
greet_user('Louis', age = '19') # keyword argument should be used after positional argument

greet_user(age =18, name = 'vicky')
print('finish')