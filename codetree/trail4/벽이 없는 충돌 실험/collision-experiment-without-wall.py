import sys
input = sys.stdin.readline

COORD_SIZE = 4000
BLANK = -1

# U, D, L, R
dir_num = {
    'U': 0,
    'D': 1,
    'L': 2,
    'R': 3
}

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 매 테스트마다 새로 만들면 매우 느리므로 딱 한 번만 생성
next_marble_index = [
    [BLANK] * (COORD_SIZE + 1)
    for _ in range(COORD_SIZE + 1)
]

T = int(input())

for _ in range(T):
    n = int(input())

    marbles = []

    for number in range(1, n + 1):
        x, y, weight, direction = input().split()

        x = int(x)
        y = int(y)
        weight = int(weight)

        # 좌표를 2배해서 0.5 위치의 충돌까지 정수 좌표로 처리
        # 범위를 0 ~ 4000으로 이동
        row = -y * 2 + 2000
        col = x * 2 + 2000

        marbles.append(
            (number, row, col, weight, dir_num[direction])
        )

    answer = -1

    # 최대 4000초까지만 보면 됨
    for time in range(1, 4001):

        # 더 이상 충돌 자체가 불가능
        if len(marbles) <= 1:
            break

        next_marbles = []

        for number, y, x, weight, direction in marbles:

            ny = y + dy[direction]
            nx = x + dx[direction]

            # 이 범위를 벗어난 구슬은
            # 앞으로 다른 구슬과 충돌할 수 없으므로 제거
            if not (
                0 <= ny <= COORD_SIZE
                and 0 <= nx <= COORD_SIZE
            ):
                continue

            # 해당 위치에 아직 아무 구슬도 없음
            if next_marble_index[ny][nx] == BLANK:

                next_marbles.append(
                    (number, ny, nx, weight, direction)
                )

                next_marble_index[ny][nx] = len(next_marbles) - 1

            # 이미 구슬이 있음 -> 충돌
            else:
                answer = time

                idx = next_marble_index[ny][nx]

                old_number, _, _, old_weight, _ = next_marbles[idx]

                # 새 구슬의 영향력이 더 크면 교체
                if (
                    weight > old_weight
                    or
                    (weight == old_weight and number > old_number)
                ):
                    next_marbles[idx] = (
                        number,
                        ny,
                        nx,
                        weight,
                        direction
                    )

        marbles = next_marbles

        # 우리가 사용했던 칸만 다시 BLANK로 초기화
        for number, y, x, weight, direction in marbles:
            next_marble_index[y][x] = BLANK

    print(answer)