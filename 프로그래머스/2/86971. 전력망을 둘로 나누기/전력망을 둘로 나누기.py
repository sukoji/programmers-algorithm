def dfs(graph, start, visited):
    count = 1
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            count += dfs(graph, i, visited)
    return count

def solution(n, wires):
    
    graph = [[] for _ in range(n + 1)]
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    # 모든 전선을 기준으로 두 전력망의 차이를 계산
    min_difference = n
    for v1, v2 in wires:
        # 전선 제거
        graph[v1].remove(v2)
        graph[v2].remove(v1)
        
        # 두 전력망의 송전탑 개수 계산
        visited = [False] * (n + 1)
        count = dfs(graph, v1, visited)
        
        # 송전탑 개수 차이 계산
        difference = abs(count - (n - count))
        min_difference = min(min_difference, difference)
        
        # 전선 복구
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    return min_difference