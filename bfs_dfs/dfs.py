def dfs(graph, v, visited):
    #방문 시 True 처리
    visited[v] = True
    #방문지 출력
    print(v,end = ' ')

    # v 번째 노드의 인접 노드 탐색
    for i in graph[v]:
        # 해당 노드의 인접 노드 들이 False면, True처리 후 다시 출력 & 다시 실행 (재귀함수)
        if not visited[i]:
            dfs(graph,i,visited)

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

visited = [False] * 9 # idx ==0 을 포함한 (idx ==0 은 무조건 False)

dfs(graph, 1, visited)