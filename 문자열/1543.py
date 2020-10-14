n = input()
m = input()
start = 0
end = len(m)
count = 0
while True:
    if n[start:end] != m:
        start+=1
        end+=1
        if end > len(n):
            break
        continue
    else:
        count+=1
        start+=len(m)
        end+=len(m)
        if end > len(n):
            break

print(count)
