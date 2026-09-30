N, M, K = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
# 1번부터 M번까지 번호 순서대로 총 M개의 지점이 연결되어 있는 1차원 윷놀이 판
# M번에서는 더이상 갈 수 없다
ans = 0
cnt_room = [0] * K

def dfs(idx):
    global ans

    if idx == N:
        cnt = 0
        for i in range(K):
            if cnt_room[i] >= M-1:
                cnt += 1
        ans = max(ans, cnt)
        return
    
    a = nums[idx]

    for i in range(K):
        cnt_room[i] += a
        dfs(idx + 1)
        cnt_room[i] -= a

dfs(0)
print(ans)