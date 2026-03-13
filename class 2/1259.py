
while True:
    str_input = input()

    if str_input == '0':
        break
    
    done = False
    for i in range(len(str_input)//2):
        if str_input[i] != str_input[-(i+1)]:
            print('no')
            done = True
            break
    if not done:
        print('yes')
