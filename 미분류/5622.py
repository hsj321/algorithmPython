word = input()
number = 0

for i in word:
    num = ord(i)
    if num >= 65 and num <= 67:
        number += 3
    elif num >= 68 and num <= 70:
        number+=4
    elif num >= 71 and num <= 73:
        number+=5
    elif num >= 74 and num <= 76:
        number+=6
    elif num >= 77 and num <= 79:
        number+=7
    elif num >= 80 and num <= 83:
        number+=8
    elif num >= 84 and num <= 86:
        number+=9
    elif num >= 87 and num <= 90:
        number+=10



print(number)
