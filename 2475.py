nums = [int(x) for x in input().split()]
squared_sum = 0
for i in nums:
    squared_sum += i**2

print(squared_sum%10)