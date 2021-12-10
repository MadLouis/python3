import random
secret_num = random.randint(0,100)
limit_num = 3
guess_count=0

while guess_count < limit_num:
    guess_num = input('please put your guess nubmer: ')
    guess_count += 1
    if guess_num == secret_num:
        print('you won')
        break
    else:
        print(f'wrong. please guess again and you have remainder of {limit_num-guess_count}')

else:
    print("you're failed")
    print(f'secret number is {secret_num}')