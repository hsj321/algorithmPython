n = int(input())
wine = []
answer = []
for _ in range(n):
    wine.append(int(input()))
if n > 0:
    answer.append(wine[0])
if n > 1:
    answer.append(wine[0]+wine[1])
if n > 2:
    answer.append(max(wine[0]+wine[2], wine[1]+wine[2], answer[1]))
if n > 3:
    for i in range(3, n):
        a = max(answer[i-2]+wine[i], wine[i]+answer[i-3]+wine[i-1], answer[i-1])
        answer.append(a)

print(answer[n-1])
