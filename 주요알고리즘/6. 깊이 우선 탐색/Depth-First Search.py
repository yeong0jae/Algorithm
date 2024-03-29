# 깊이 우선 탐색(DFS): 가중치가 1인 그래프에서, 탐색하지 않은 인접 노드를 우선으로 최대한 깊숙이 탐색하여 노드를 방문한 후, 다시 돌아가 다른 경로로 탐색하는 방법이다.
# 후입선출 구조

# DFS의 구현 방법

# 1. 탐색 시작 노드를 매개변수로 받아 방문 처리를 한다.
# 2. 인접 노드를 차례로 돌며 탐색하지 않은 경우(인접 노드의 탐색 여부가 재귀 조건) 재귀 호출을 하고, 모두 탐색한 경우 함수를 종료한다.
# (+ 인접 노드의 탐색 여부를 종료 조건으로 해서 재귀 호출을 하므로 탐색하지 않은 인접 노드에 대해서만 재귀 호출을 하기 때문에 호출량이 적다.)


# DFS

graph = [ # 인접 리스트 방식.
  [], # 0번 노드는 없으므로 비워둔다.
  [2, 3, 8], # 1번 노드와 연결된 노드들
  [1, 7], # 2번 노드와 연결된 노드들
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7] # 8번 노드와 연결된 노드들
]
visited = [False] * 9 # 노드의 방문 여부 테이블

def dfs(graph, v, visited): # 탐색 그래프, 시작노드, 방문 여부 테이블
	visited[v] = True
	for i in graph[v]:
		if not visited[i]: # 인접 노드의 방문 여부가 재귀 조건: 방문 안한 인접 노드면 호출, 방문 한 인접노드면 호출X
			''' if 조건 추가 가능. 바로 return 하던지 등 '''
			dfs(graph, i, visited)




# 1. 탐색 시작 노드를 매개변수로 받아
# 2. 탐색하지 않은 경우(현재 노드의 탐색 여부가 재귀 조건) 방문 처리 후 인접 노드를 차례로 돌며 재귀 호출을 하고, 탐색한 경우 함수를 종료한다.
# (+ 현재 노드의 탐색 여부를 종료 조건으로 해서 재귀 호출을 하기 때문에, 매번 모든 인접 노드에 대하여 재귀 호출을 해야해서 호출량이 많아진다.)


'''
def dfs(graph, v, visited):
	if not visited[v]: # 현재 노드의 방문 여부가 재귀 조건: 호출 시 방문 안한 노드면 방문처리, 방문 했으면 탈출
		visited[v] = True
		for i in graph[v]:
			dfs(graph, i, visited)

'''

