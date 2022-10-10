# https://www.acmicpc.net/problem/18352
from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())
# 도시마다 연결된 다른 도시를 저장하는 리스트
graph = [[] for _ in range(n+1)]

# 모든 도로 정보 입력받기
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시애 대한 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0

# 너비 우선 탐색(BFS) 수행
queue = deque([x])

while queue:
    now = queue.popleft()
    
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            queue.append(next_node)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)

# 만약 최단 거리가 K인 도시가 없다면, -1 출력
if k not in distance:
    print(-1)
