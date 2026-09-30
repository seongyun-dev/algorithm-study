N, M = map(int, input().split())

# Please write your code here.
# 1번 정점에서 시작하여 주어진 간선을 따라 이동했을 때 도달할 수 있는 
# 서로 다른 정점의 개수
cnt = 0
graph = [[] for _ in range(N + 1)]
used = [False] * (N + 1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

used[1] = True

def dfs(cur):
    global cnt

    used[cur] = True

    for nxt in graph[cur]:
        if used[nxt]:
            continue
        
        used[nxt] = True
        cnt += 1
        dfs(nxt)

dfs(1)

print(cnt)