from collections import deque

#bfs 메서드 정의
def bfs(graph, start, visited):
    queue = deque([start])
    #현재 노드 방문 처리
    visited[start] = True

    #큐가 빌 때(queue == False)까지 반복
    while queue:
        # 선입 선출 queue
        v = queue.popleft()
        print(v, end =' ')

        # 빠져 나온 노드를 기준으로 진행!
        for i in graph[v]:
            # 인접 노드 중 방문X인 노드 큐에 넣고, 모두 방문처리
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    #문제에 최적화 하기 위해 idx == 0에 해당하는 인접노드는 비워둔다.
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]


visited = [False] * 9  # idx ==0 을 포함한 (idx ==0 은 무조건 False)

bfs(graph,1,visited)