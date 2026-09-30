K, N = map(int, input().split())

answer = []

def dfs(n):
    global cnt

    if n == N:
        print(*answer)
        return

    for i in range(1, K + 1):

        # 같은 숫자가 3번 연속 나오면 제외
        if len(answer) >= 2 and answer[-1] == i and answer[-2] == i:
            continue

        answer.append(i)
        dfs(n + 1)
        answer.pop()

dfs(0)
