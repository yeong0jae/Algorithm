# 2667 단지번호붙이기 - 격자그래프, dfs에서 깊이값 출력하기

n = int(input())

graph = []

for _ in range(n):
	graph.append(list(map(int, input())))
	# 간선 정보가 필요없는 그래프는 graph가 visited의 역할도 함. ex ㄴ격자그래프
num = []

def dfs(x, y): # 격자그래프의 dfs는 좌표 받음
	if x <= -1 or x >= n or y <= -1 or y >= n: # 종료조건
		return False
	if graph[x][y] == 1: # 시작 노드의 방문 여부로 dfs. 방문했으면 0으로 바꿔주기
		global count
		count += 1 # 스택이 다시 비었을때, count값이 유지되도록 해야함 그리고 다시 0으로 돌려주기
		graph[x][y] = 0 # 방문한 노드는 0으로 바꿔주기
		dfs(x - 1, y) # 상하좌우 노드에 대해 dfs
		dfs(x, y - 1)
		dfs(x + 1, y)
		dfs(x, y + 1)
		return True # 단지가 끝나면 True 반환
	return False

count = 0
result = 0
for i in range(n):
	for j in range(n): # 모든 노드를 확인하며 단지를 확인함. 아파트가 하나 발견되면 바로 단지를 정복하게됨.
		if dfs(i, j) == True: # dfs가 True를 반환하면, 단지가 끝난 것이므로, 단지의 아파트 수를 num에 추가하고, count를 0으로 돌려주기
			num.append(count)
			count = 0 # (i, j) 에 대해 바로 count를 유지하면서 더해주며 단지를 정복하므로, 단지가 끝나면 dfs(i, j)가 종료되는데, 종료되면 count = 0으로 돌려주면 됨.
			result += 1
			
num.sort()
print(result)
for i in range(len(num)):
    print(num[i])


