numbers = [3,6,2,8,4,10,90]
max = numbers[0]  # assume the max num in [0]

for number in numbers:
    if max< number:
        max = number

print(f'max_num: {max}')    