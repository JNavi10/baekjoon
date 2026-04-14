import sys

sys.stdin.readline

num_stairs = int(input())

stairs = []
for _ in range(num_stairs):
    stairs.append(int(input()))

cur_index = 0
while cur_index < num_stairs:
    
    cur_index += 3

