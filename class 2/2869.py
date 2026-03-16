# v=0에 달팽이
# v=V까지 올라간다
# 낮에 Am까지 올라간다
# 밤에 Bm 내려간다
# 정상에 도착하면 안 내려간다
# 정상 도착까지 며칠 걸리는가?
import math

A, B, V = map(int, input().split())

day_mv = A-B
target = V-B

print(math.ceil(target/day_mv))
