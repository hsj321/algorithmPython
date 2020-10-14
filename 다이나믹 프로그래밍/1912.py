n = int(input())

arr = list(map(int, input().split()))
answer = []
answer.append(arr[0])
for i in range(1, n):
    answer.append(max(answer[i-1]+arr[i], arr[i]))
print(max(answer))
