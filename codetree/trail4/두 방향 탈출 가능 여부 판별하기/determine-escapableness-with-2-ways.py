N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
# N x M 크기의 이차원 영역의 좌측 상단에서 춟달
# 우측 하단까지 뱀에게 물리지 않고 탈출
dy = [0, 1]
dx = [1, 0]
answer = False
used = [[False] * M for _ in range(N)]
used[0][0] = True

def dfs(y, x):
    global answer

    if answer:
        return
    
    if (y, x) == (N - 1, M - 1):
        answer = True
        return

    for d in range(2):
        ny = y + dy[d]
        nx = x + dx[d]
        if not (0 <= ny < N and 0 <= nx < M):
            continue
        
        if graph[ny][nx] == 0:
            continue
        
        if used[ny][nx] == True:
            continue
        
        used[ny][nx] = True
        dfs(ny, nx)

dfs(0, 0)

if answer == True:
    print(1)
else:
    print(0)