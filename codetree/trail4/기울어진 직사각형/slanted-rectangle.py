n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 우상 → 좌상 → 좌하 → 우하
dy = [-1, -1, 1, 1]
dx = [1, -1, -1, 1]

ans = 0

# 시작 위치
for i in range(n):
    for j in range(n):

        # 두 종류의 변 길이
        for a in range(1, n):
            for b in range(1, n):

                move_num = [a, b, a, b]

                y = i
                x = j
                total = 0
                valid = True

                # 4개의 변
                for d in range(4):

                    # 해당 변 길이만큼 이동
                    for _ in range(move_num[d]):

                        # 현재 칸을 합에 추가
                        total += grid[y][x]

                        ny = y + dy[d]
                        nx = x + dx[d]

                        # 격자를 벗어나면 이 직사각형은 불가능
                        if not (0 <= ny < n and 0 <= nx < n):
                            valid = False
                            break

                        y = ny
                        x = nx

                    if not valid:
                        break

                if valid:
                    ans = max(ans, total)

print(ans)