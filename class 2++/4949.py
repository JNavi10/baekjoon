import sys

input = sys.stdin.readline

while True:
    input_str = input()[:-1]

    # If . break
    if input_str == '.':
        break

    # Remove all unnecessary characters
    cleaned_str = ''
    for c in input_str:
        if c in ['[', ']','(',')','.']:
            cleaned_str += c
    #print(cleaned_str)

    # Check validity
    stack = []
    no_flag = False
    for c in cleaned_str:
        match c:
            case '(':
                stack.append(c)
            case '[':
                stack.append(c)
            case ')':
                if not stack or stack[-1] != '(':
                    no_flag = True
                    break
                else:
                    stack.pop()
            case ']':
                if not stack or stack[-1] != '[':
                    no_flag = True
                    break
                else:
                    stack.pop()
            case '.':
                if stack:
                    no_flag = True
                    break
    
    if no_flag:
        print('no')
    else:
        print('yes')

