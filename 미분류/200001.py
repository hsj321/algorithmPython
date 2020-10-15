problem = 0
while(True):
    temp = input()
    if temp == "문제":
        problem+=1
        continue
    if temp == "고무오리":
        if problem == 0:
            problem+=2
        else:
            problem-=1
        continue
    if temp == "고무오리 디버깅 끝":
        break
if problem == 0:
    print("고무오리야 사랑해")
else:
    print("힝구")
