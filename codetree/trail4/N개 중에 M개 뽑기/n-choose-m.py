N, M = map(int, input().split())
answer = []
ans = set()

# Please write your code here.
# 1이상 N이하의 정수 중 M개의 정수를 골라 모든 조합
def dfs(start):
    if len(answer) == M:
        print(*answer)
        return
    
    for i in range(start, N + 1):
        answer.append(i)
        dfs(i + 1)
        answer.pop()

dfs(1)
