import sys
input = sys.stdin.readline

N, M = map(int, input().split())

name_to_dex = {}
dex_to_name = {}

def insert(name, dex_no):
    name_to_dex[name] = dex_no
    dex_to_name[dex_no] = name

def lookup(x):
    if x in name_to_dex: 
        return name_to_dex[x]
    if x in dex_to_name: 
        return dex_to_name[x]


for i in range(N):
    name = input().strip()
    insert(name, str(i+1))

for _ in range(M):
    print(lookup(input().strip()))
