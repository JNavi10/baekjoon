import sys
input = sys.stdin.readline

N, M = map(int, input().split())

site_set = dict()
for _ in range(N):
    site_str, pw = input().split()
    site_set[site_str] = pw

for _ in range(M):
    site_str = input().strip()
    print(site_set[site_str])
