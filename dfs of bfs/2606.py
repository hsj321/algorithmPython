def dfs(graph):
    answer = 0
    visited, need_visit = list(), list()
    need_visit.append(1)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
            answer += 1

    return answer
            


n = int(input())
m = int(input())
graph = dict()
for i in range(1, n+1):
    graph[i] = []
for i in range(m):
    temp = input().split()
    m = map(int,temp)
    a, b = m
    graph[a].append(b)
    graph[b].append(a)


    
print(dfs(graph)-1)
