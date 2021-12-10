print(''' 
hello,
1. Put whatever number you like 
2. Sum these nubmers
3. Exit
''')

while True:
    option = input('please enter your option: ')
    if option == '1':
        num = float(input('give a number: '))
        i = 1
        res = []
        for i in range(1,13):
            res.append(num *i)
            i +=1
        print(res)

    elif option == '2':
        num1 = float(input('give a first number: '))
        num2 = float(input('give a second number: '))
        sum = num1 + num2
        print(sum)
    
    elif option == '3':
        print('goodbye')
        break
    
    else:
        print('Invalid choice')





