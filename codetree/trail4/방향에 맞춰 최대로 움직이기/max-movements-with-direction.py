n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
move_dir = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.
# N x N 크기의 격자
# 수는 중복없이 단 한번씩만 주어짐
# 방향은 아래 그림에서 왼쪽에 적혀있는대로 여덟 방향 중 하나
# 특정 위치에서 시작하여 적혀있는 방향에 있는 수 중 현재 수보다
# 더 큰수가 적혀있는 곳으로 이동 최대한 반복
direction = [
    [0, 0],
    [-1, 0],
    [-1, 1],
    [0, 1],
    [1, 1],
    [1, 0],
    [1, -1],
    [0, -1],
    [-1, -1]
]
ans = 0

def dfs(y, x, cnt):
    global ans

    ans = max(ans, cnt)

    d = move_dir[y][x]
    dy, dx = direction[d]

    dist = 1
    while True: 
        ny = y + dist * dy
        nx = x + dist * dx
        if not (0 <= ny < n and 0 <= nx < n):
            break
        
        if num[ny][nx] > num[y][x]:
            dfs(ny, nx, cnt + 1)

        dist += 1

dfs(r - 1, c - 1, 0)
print(ans)