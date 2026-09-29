N = int(input())
line_lst = []

for _ in range(N):
    a, b = map(int, input().split())
    line_lst.append((a, b))

line_lst.sort()
# Please write your code here.
# 수직선상에 N개의 선분이 주어졌을 떄
# 서로 겹치지 않고 고를 수 있는 가장 많은 선분의 수
# 끝점을 공유하는 것 역시 겹친 것
# 순서대로 정렬 후 작업하면 쉬울 것 같다.
# 정렬 후 하나씩 선택, 전 선분의 사이에 있으면 선택안함
ans = 0

def dfs(n, last_r, cnt):
    global ans
    
    if n == N:
        ans = max(ans, cnt)
        return
    
    if last_r >= line_lst[n][0]:
        dfs(n + 1, last_r, cnt)
        return

    dfs(n + 1, line_lst[n][1], cnt + 1)
    dfs(n + 1, last_r, cnt)
    
dfs(0, 0, 0)
print(ans)

    