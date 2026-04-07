N = int(input())

li: list = [i for i in range(1, N+1)]
even_lives: bool = True

while True:
    if len(li) == 1:
        break
 
    if even_lives:  # 짝수면
        subset = li[1::2]  # 짝수만 산다
    else:
        subset = li[0::2]

    # even_lives 와 현재행의 홀수여부를 XOR하면 다음 even_lives의 값이 됨
    even_lives = even_lives ^ bool(len(li)%2)
    li = subset

print(li[0])