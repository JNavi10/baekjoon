int_N = int(input())

result = 0

ans = 0
while ans < int_N:
    # 분해합
    bhh = ans
    str_ans = str(ans)
    for numchar in str_ans:
        bhh += int(numchar)

    if bhh == int_N:
        result = ans
        break
    ans += 1

print(result)