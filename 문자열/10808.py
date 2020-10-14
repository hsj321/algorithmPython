s = input()
n = len(s)
answer = [0 for i in range(26)]
for i in range(n):
    answer[int(ord(s[i]))-97]+=1

for i in range(26):
    print(str(answer[i]), end=' ')
