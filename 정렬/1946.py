import sys

t = int(input())
for _ in range(t):
    n = int(input())
    num = []
    for _ in range(n):
        num.append(list(map(int, sys.stdin.readline().strip().split())))
    temp = sorted(num, key = lambda x : x[0])

    count = 1

    min = temp[0][1]

    for j in range(1,n):
        if temp[j][1] < min:
            min = temp[j][1]
            count+=1
    
    print(count)
