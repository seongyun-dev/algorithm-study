K, N = map(int, input().split())
answer = []

def dfs(n):
    if n == N:
        print(*answer)
        return

    for i in range(1, K + 1):
        answer.append(i)

        dfs(n + 1)

        answer.pop()

dfs(0)