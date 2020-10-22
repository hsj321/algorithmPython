n = int(input())
arr = list(map(int, input().split()))
answer = [0]*n
for i in range(1, n+1):
    idx = arr[i-1]
    count = 0
    for j in range(n):
        if count == idx and answer[j] == 0:
            answer[j] = i
            break
        elif answer[j] == 0:
            count+=1
print(*answer)
