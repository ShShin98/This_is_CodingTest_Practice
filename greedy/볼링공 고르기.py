n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1~10 볼링공 무게별 개수를 저장하는 리스트
array = [0] * 11

# 각 무게에 해당하는 볼링공의 개수 카운트
for i in data:
    array[i] += 1

result = 0

# 1부터 m까지 각 무게에 대해서 반복
for i in range(1, m + 1):
    n -= array[i] # 전체 볼링공 개수에서 무게가 i인 볼링공 개수(A가 선택함) 제외 -> B가 선택할 볼링공 개수
    result += array[i] * n # A가 선택한 볼링공 개수와 B가 선택할 볼링공 개수 곱하기

print(result)