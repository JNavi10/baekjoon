T = int(input())

for i in range(T):
    R, S = input().split()
    for char in S:
        for j in range(int(R)):
            print(char, end='')
    print()