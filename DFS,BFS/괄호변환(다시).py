def isCorrect(s):
    stack = []
    
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                return False
            stack.pop()
        
    return True
        
def divide(s):
    open_p = 0
    close_p = 0
    
    for i in range(len(s)):
        if s[i] == '(':
            open_p += 1
        else:
            close_p += 1
        if open_p == close_p:
            return s[:i + 1], s[i + 1:]
        
def solution(p):
    # 과정 1
    if not p:
        return p
    
    # 과정 2
    u, v = divide(p)
    
    # 과정 3
    if isCorrect(u):
        # 과정 3-1
        return u + solution(v)
    # 과정 4
    else:
        # 과정 4-1
        answer = '('
        # 과정 4-2
        answer += solution(v)
        # 과정 4-3
        answer += ')'
        # 과정 4-4
        for c in u[1:len(u) - 1]:
            if c == '(':
                answer += ')'
            else:
                answer += '('
        # 과정 4-5
        return answer