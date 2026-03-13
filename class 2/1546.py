# 시험 과목 수
N = int(input())

li = list(map(int, input().split()))

max_score = max(li)
total = sum([score/max_score*100 for score in li])

print(total/N)

## no need to create list in sum
## just do sum(score / max_score * 100 for score in li)