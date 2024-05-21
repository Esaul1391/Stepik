#  Скобки

def check(string: str):
    stack = []
    for i, char in enumerate(string, 1):
        if char in '([{':
            stack.append((char, i))
        elif char in ')]}':
            if len(stack) == 0:
                return i
            if char == ')' and stack[-1][0] == '(':
                stack.pop()
            elif char == ']' and stack[-1][0] == '[':
                stack.pop()
            elif char == '}' and stack[-1][0] == '{':
                stack.pop()
            else:
                stack.append((char, i))
    print(stack)
    return stack[-1][1] if len(stack) > 0 else 'Successful'



def check_brackets(s):
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}'}
    for i, char in enumerate(s, 1):
        if char in brackets.keys():
            stack.append((char, i))
        elif char in brackets.values():
            if not stack:
                return i
            last_open_bracket, index = stack.pop()
            if brackets[last_open_bracket] != char:
                return i
    return stack[0][1] if stack else 'Success'
print(check_brackets(input()))



print(check('{{{[][][]'))
assert check("()[]}") == 5
assert check("{{[()]]") == 7
assert check("{{{[][][]") == 3
assert check("{*{{}") == 3
assert check("[[*") == 2
assert check("{{") == 2
assert check("}") == 1
assert check("{{{**[][][]") == 3


# print(staples('([](){([dfdf])})'))