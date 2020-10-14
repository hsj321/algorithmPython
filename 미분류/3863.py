while(True):
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    call = []
    police = []

    for _ in range(n):
        source, dest, start, duration = map(int, input().split())
        call.append((start, start+duration))

    for _ in range(m):
        start, duration = map(int, input().split())
        police.append((start, start+duration))

    for i in range(m):
        answer = 0
        for j in range(n):
            if police[i][0] >= call[j][1] or police[i][1] <= call[j][0]:
                continue
            else:
                answer+=1
        print(answer)
