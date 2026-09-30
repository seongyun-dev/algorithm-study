n = int(input())
num = list(map(int, input().split()))

# Please write your code here.
# 각 위치로부터 최대 점프 가능 거리를 의미한 N개의 정수
# 최소 점프 횟수 구하기
ans = float('inf')

def dfs(idx, cnt):
    global ans

    if idx > n - 1:
        return

    if idx == n - 1:
        ans = min(cnt, ans)
        return
    
    d = num[idx]

    for i in range(1, d + 1):
        dfs(idx + i, cnt + 1)
    
dfs(0, 0)

if ans == float('inf'):
    ans = -1

print(ans)