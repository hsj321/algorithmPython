n = int(input())
answer = 0

while True:
    if n < 5 and n != 3:
        break

    if n%5 == 0:
        answer+=1
        n-=5
        continue

    if n %3 == 0:
        answer+=1
        n-=3
        continue

    if n > 5:
        answer+=1
        n-=5
        continue


if n != 0:
    print(-1)
else:
    print(answer)
