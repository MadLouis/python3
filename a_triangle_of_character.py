#ord("z") #  to convert character to ASCII
#chr(90)  #  to convert ASCII to character

while True:
    try:
        height  = int(input("Enter a int positive  number: "))
        if height <=0:
            raise ValueError
        break
    except ValueError:
        print("Incorrect input, try again")


A_code = ord("A")         # 90
c = A_code
for i in range(1,height+1):
    print(" "*(height-i),end = '')
    line = ""
    for j in range(0,i):
        j = j%26
        line += chr(c+j)
    line += line[:-1][::-1]
    print(line)
        
        
        
        





    