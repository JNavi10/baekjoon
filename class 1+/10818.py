N = int(input())

# map returns lazy iterator. if need to reused, convert it to list first
arr = list(map(int, input().split()))
print(min(arr), max(arr))