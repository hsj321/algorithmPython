n = int(input())
arr = [0 for i in range(301)]
answer = [0 for i in range(301)]
for i in range(n):
    arr[i] = int(input())

answer[0]=arr[0]
answer[1]=arr[1]+arr[0]
answer[2]=max(arr[0]+arr[2], arr[1]+arr[2])

for i in range(3, n):
    answer[i] = max(answer[i-2]+arr[i], arr[i]+answer[i-3]+arr[i-1])

print(answer[n-1])
