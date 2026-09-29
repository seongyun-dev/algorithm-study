n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
booms = []
destroyed_map = [[0] * n for _ in range(n)]

for y in range(n):
    for x in range(n):
        if grid[y][x] == 1:
            booms.append((y, x))

boom_cnt = len(booms)
ans = 0

booms_type = [
    [
        (-2, 0),
        (-1, 0),
        (0, 0),
        (1, 0),
        (2, 0)
    ],
    [
        (-1, 0),
        (0, 0),
        (0, 1),
        (0, -1),
        (1, 0)
    ],
    [
        (-1, 1),
        (-1, -1),
        (0, 0),
        (1, 1),
        (1, -1)
    ]
]

def destroyed(y, x, i, value):
    for j in range(5):
        dy, dx = booms_type[i][j]
        ny = y + dy
        nx = x + dx
        if not(0 <= ny < n and 0 <= nx < n):
            continue
        destroyed_map[ny][nx] += value
    

def destroyed_cnt():
    cnt = 0

    for y in range(n):
        for x in range(n):
            if destroyed_map[y][x] > 0:
                cnt += 1

    return cnt

def dfs(idx):
    global ans

    if idx == boom_cnt:
        ans = max(ans, destroyed_cnt())
        return

    y, x = booms[idx]

    for i in range(3):
        destroyed(y, x, i, 1)
        dfs(idx + 1)
        destroyed(y, x, i, -1)
    
dfs(0)
print(ans)
        