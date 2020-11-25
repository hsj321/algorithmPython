while(True):
    
    n, a, b = map(int, input().split())
    if n == 0 and a == 0 and b == 0:
        break
    time = 0
    arr = [[0]*4 for _ in range(n)]

    for i in arr:
        i[0], i[1], i[2] = map(int, input().split())
        i[3] = abs(i[1]-i[2])
    arr = sorted(arr, key = lambda x : (abs(x[3])), reverse = True)
    print(arr)
    for i in arr:
        count = i[0]
        aL = i[1]
        bL = i[2]
        if aL < bL:
            if a-i[0] >= 0:
                a-=i[0]
                time+=aL*i[0]
                i[0] = 0
            else:
                i[0]-=a
                time+=aL*a
                a = 0
        else:
            if b-i[0] >= 0:
                b-=i[0]
                time+=bL*i[0]
                i[0] = 0
            else:
                i[0]-=b
                time+=bL*b


                
                b = 0
    for i in arr:
        count = i[0]
        aL = i[1]
        bL = i[2]
        print(count)
        if count == 0:
            continue
        if aL < bL:
            b-=count
            time+=bL*count
                
        else:
            a-=count
            time+=aL*count
                
    print(time)
