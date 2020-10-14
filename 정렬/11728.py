a, b = map(int, input().split())
aList = list(map(int, input().split()))
bList = list(map(int, input().split()))
answer = []

ac = 0
bc = 0

for i in range(a+b):
	if ac == len(aList):
		answer.append(bList[bc])
		print("{} ".format(bList[bc]), end='')
		bc+=1
		continue
	elif bc == len(bList):
		answer.append(aList[ac])
		print("{} ".format(aList[ac]), end='')
		ac+=1
		continue
	if aList[ac] < bList[bc]:
		answer.append(aList[ac])
		print("{} ".format(aList[ac]), end='')
		ac+=1
		continue
	else:
		answer.append(bList[bc])
		print("{} ".format(bList[bc]), end='')
		bc+=1
		continue
