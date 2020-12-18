n = int(input())
arr = []
max = 0
for _ in range(n):
    temp = int(input())
    arr.append(temp)

arr.sort(reverse = True)
for i in range(n):
    k = i+1
    weight = k * arr[i]
    if max < weight:
        max = weight
print(max)
    
