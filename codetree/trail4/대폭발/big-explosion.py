n, m, r, c = map(int, input().split())

# 0-index로 변경
r -= 1
c -= 1

# 현재 존재하는 폭탄들의 위치
bombs = {(r, c)}

# 상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for t in range(1, m + 1):

    # t초일 때 이동 거리: 2^(t-1)
    dist = 2 ** (t - 1)

    # 기존 폭탄은 그대로 남아있음
    new_bombs = set(bombs)

    # 현재 시점에 이미 있던 폭탄들만 폭발
    for y, x in bombs:

        for d in range(4):
            ny = y + dy[d] * dist
            nx = x + dx[d] * dist

            # 격자 안이라면 폭탄 생성
            if 0 <= ny < n and 0 <= nx < n:
                new_bombs.add((ny, nx))

    bombs = new_bombs

print(len(bombs))