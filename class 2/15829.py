# 입력은 오직 영문 소문자
# 소문자 알파벳은 총 26자
# a=1, b=2, ... z=26으로 가정
# H = ai * r^i mod M (r = 31, M = 1234567891)

# 문자열 길이 L
L = int(input())

# 문자열
S = input()

total = 0
for i, char in enumerate(S):
    total += (ord(char) - ord('a') + 1) * 31**i

print(total % 1234567891)