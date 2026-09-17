n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# r, c : 시작 위치
# m1 ~ m4 : 1~4번 방향으로 이동할 거리
# direction : 0 = 반시계, 1 = 시계
r, c, m1, m2, m3, m4, direction = map(int, input().split())

# 파이썬 배열은 0-index
r -= 1
c -= 1

# 1번 ↗, 2번 ↖, 3번 ↙, 4번 ↘
dy = [-1, -1, 1, 1]
dx = [1, -1, -1, 1]

move_num = [m1, m2, m3, m4]

# 직사각형 테두리 좌표 저장
path = []

y, x = r, c

for d in range(4):
    for _ in range(move_num[d]):
        path.append((y, x))

        y += dy[d]
        x += dx[d]

# 기존 값들을 따로 저장
values = []

for y, x in path:
    values.append(grid[y][x])

length = len(path)

if direction == 0:
    # 반시계 방향
    # 현재 값이 다음 위치로 이동
    for i in range(length):
        ny, nx = path[(i + 1) % length]
        grid[ny][nx] = values[i]

else:
    # 시계 방향
    # 현재 값이 이전 위치로 이동
    for i in range(length):
        ny, nx = path[(i - 1) % length]
        grid[ny][nx] = values[i]

for row in grid:
    print(*row)