from collections import deque

n, k = map(int, input().split()) # n, k 입력
test_tube = [] # 시험관 정보 저장하는 리스트
virus_data = [] # 바이러스 정보 저장하는 리스트
# 시험관 정보 입력받기
for i in range(n):
    test_tube.append(list(map(int, input().split())))
    for j in range(n):
        # 입력받은 행 중에 바이러스가 있다면
        if test_tube[i][j] != 0:
            # 바이러스의 번호와 시간, 위치를 바이러스 정보에 추가
            virus_data.append((test_tube[i][j], 0, i, j))

# 바이러스 번호별로 오름차순 정렬 후 큐에 삽입
virus_data.sort()
queue = deque(virus_data)

# 타겟 변수 입력받기
target_s, target_x, target_y = map(int, input().split()) 

# 상하좌우 이동
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 큐가 빌때까지 반복
while queue:
    virus, s, x, y = queue.popleft()
    # s초가 지나면 중지
    if s == target_s:
        break
    # 현재 노드 기준으로 상하좌우 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 해당 위치로 이동할 수 있는 경우
        if 0 <= nx < n and 0 <= ny < n:
            # 바이러스가 없다면
            if test_tube[nx][ny] == 0:
                # 바이러스 전파
                test_tube[nx][ny] = virus
                # 전파된 바이러스 데이터 큐에 삽입
                queue.append((virus, s + 1, nx, ny))

print(test_tube[target_x - 1][target_y - 1])

# 풀이 : https://inistory.tistory.com/143