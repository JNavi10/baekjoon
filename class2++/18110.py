import sys
import math

input = sys.stdin.readline

n = int(input())

if n == 0:
    print(0)
else:
    li = []
    for _ in range(n):
        li.append(int(input()))

    li.sort()


    cut_num = math.floor((len(li) * 0.15) + 0.5)

    cut_li = li[cut_num:len(li)-cut_num]

    print(math.floor((sum(cut_li)/len(cut_li)) + 0.5))

# python uses banker's rounding. 
# Meaning .5 is rounded to nearest even number