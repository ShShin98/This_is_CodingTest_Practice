s = input()
cnt = 0 # 변화 횟수 체크하는 변수

for i in range(len(s) - 1):
  # 현재 숫자와 다음 숫자가 다를 경우
  if s[i] != s[i] + 1:
    cnt += 1

# 규칙에 따르면 뒤집는 횟수는 변화 횟수 + 1을 2로 나눈 값이다
print((cnt + 1) // 2)
