n = int(input())
answer = 0
arr = [n]

def cal(n):
    temp = []
    for i in n:
        temp.append(i-1)
        if i%3 == 0:
            temp.append(i/3)
        if i%2 == 0:
            temp.append(i/2)
    return temp

while True:
    if n==1:
        print(0)
        break
    temp = arr[:]
    arr = []
    arr = cal(temp)
    answer+=1
    if min(arr) == 1:
        print(answer)
        break
