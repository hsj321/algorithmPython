n = int(input())

answer = [0,0,0]

while True:
    if n != 0 and n >= 10:
        if n >= 300:
            n-=300
            answer[0]+=1
        elif n <300 and n >= 60:
            n-=60
            answer[1]+=1
        elif n < 60:
            n-=10
            answer[2]+=1
    else:
        break
if n != 0:
    print(-1)
else:
    print('{0} {1} {2}'.format(answer[0], answer[1], answer[2]))
