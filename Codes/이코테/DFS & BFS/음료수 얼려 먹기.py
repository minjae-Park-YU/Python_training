n, m = map(int, input().split())

ice_cnt = 0
ice_tray = []
for _ in range(n):
    ice_tray.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(graph, x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x < 0 or x > n-1 or y < 0 or y > m-1:
        return False
    # 현재 노드를 아직 방문하지 않은 경우
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(ice_tray, i, j) == True:
            ice_cnt += 1

print(ice_cnt)


