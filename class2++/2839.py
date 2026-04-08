N = int(input())

num = N

count_3 = 0
while num%5!=0 and not num < 0:
    num -= 3
    count_3 += 1

if num<0:
    print(-1)
else:
    print(count_3 + num//5)

exit(0)
# 이 아래는 테스트 코드

def func_2839(N):

    #N = int(input())

    num = N

    count_3 = 0
    while num%5!=0 and not num < 0:
        num -= 3
        count_3 += 1
        print('    ', num)
    
    if num<0:
        print(-1)
    else:
        print(count_3 + num//5)

for i in [18,4,6,9,11]:
    func_2839(i)