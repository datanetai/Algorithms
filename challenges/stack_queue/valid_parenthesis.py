# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

def isValid(s: str) -> bool:
    stack = []
    for i in s:
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack or stack.pop() != '(':
                return False
        elif i == '}':
            if not stack or stack.pop() != '{':
                return False
        elif i == ']':
            if not stack or stack.pop() != '[':
                return False
    return not stack

# 2nd solution:
def isValid2(s: str) -> bool:
    if len(s) % 2 != 0:
            return False
    opening = set('([{')
    matches = set([('(', ')'), ('[', ']'), ('{', '}')])
    stack = []
    for paren in s:
        if paren in opening:
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False
            last_open = stack.pop()
            if (last_open, paren) not in matches:
                return False

    return stack == []

# 3rd solution: faster than 2nd solution
def isValid3(s: str) -> bool:
    d = {'(':')','{':'}','[':']'}
    stack = []
    for paran in s:
        if paran in d:
            stack.append(paran)
        elif len(stack) == 0 or d[stack.pop()]!=paran:
            return False
    return stack == []
    
# 4th solution: pythonic way
def isValid4(s: str) -> bool:
    d = ['()','{}','[]']
    while '()' in s or '{}' in s or '[]' in s:
        s = s.replace('()','').replace('{}','').replace('[]','')
    return s == ''