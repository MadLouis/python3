car_game = input('').lower()

while car_game == 'help':
    print(''' 
    start - to start the car
    stop - to stop the car
    exit - to exit
    ''')
    option = input('').lower()

    if option not in ['start','stop','exit']:
        print('i dont understand')
        break
    elif option == 'start':
        print('started....')
        break
    elif option == 'stop':
        print('stop...')
        break
    else:
        print('exit')
        break
