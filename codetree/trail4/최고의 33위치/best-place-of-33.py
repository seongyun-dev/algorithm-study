n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = 0

for i in range(n-2):
    for j in range(n-2):
        total = 0

        for x in range(3):
            for y in range(3):
                if grid[i+x][j+y] == 1:
                    total += 1

        ans = max(ans, total)

print(ans) 