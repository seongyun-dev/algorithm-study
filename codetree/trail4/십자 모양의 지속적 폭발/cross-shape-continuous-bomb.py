n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bomb(col):
    # 1. 해당 열에서 가장 위에 있는 폭탄 찾기
    row = -1

    for i in range(n):
        if grid[i][col] != 0:
            row = i
            break

    # 해당 열에 폭탄이 없으면 아무 일도 일어나지 않음
    if row == -1:
        return

    # 폭탄의 크기
    power = grid[row][col]

    # 2. 십자 모양으로 폭발
    # 중심 제거
    grid[row][col] = 0

    # 상하좌우로 power - 1칸씩 제거
    for d in range(4):
        for dist in range(1, power):
            ny = row + dy[d] * dist
            nx = col + dx[d] * dist

            # 격자 밖이면 그 방향은 더 볼 필요 없음
            if not (0 <= ny < n and 0 <= nx < n):
                break

            grid[ny][nx] = 0

    # 3. 중력 적용
    apply_gravity()


def apply_gravity():
    new_grid = [[0] * n for _ in range(n)]

    # 각 열별로 아래에서부터 채운다
    for j in range(n):
        bottom = n - 1

        # 기존 격자도 아래에서부터 확인
        for i in range(n - 1, -1, -1):
            if grid[i][j] != 0:
                new_grid[bottom][j] = grid[i][j]
                bottom -= 1

    # 원래 grid 갱신
    for i in range(n):
        for j in range(n):
            grid[i][j] = new_grid[i][j]


# 총 m번 폭탄 터뜨리기
for _ in range(m):
    col = int(input()) - 1  # 입력은 1번 열부터 시작
    bomb(col)


# 결과 출력
for row in grid:
    print(*row)