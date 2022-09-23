s = input()
# 첫번째 문자를 숫자로 변경함 (s는 문자열이기 때문)
result = int(s[0])

for i in range(1, len(s)):
  # 위와 같은 방법으로 문자를 숫자로 변환 (비교하기 위해)
  num = int(s[i])
  # 두 수 중에서 하나라도 0, 1 인 경우, 곱하기보다는 더하기가 낫다
  if num <= 1 or result <= 1:
    result += num
  else:
    result *= num

print(result)