N = int(input())

cnt = 0

def dfs(n):
    global cnt

    if n == N:
        cnt += 1 

    if n > N:
        return
    
    for i in range(1, 5):
        dfs(n + i)
    
dfs(0)
print(cnt)