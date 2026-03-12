A = int(input())
B = int(input())
C = int(input())

mult = A*B*C
nums = [0] * 10

while mult:
    modulo = mult % 10
    nums[modulo] += 1
    mult = mult // 10

for num in nums:
    print(num)
