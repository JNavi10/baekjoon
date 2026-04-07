import sys

input = sys.stdin.readline

N, M = map(int,input().split())

board = []
for _ in range(N):
    row_str: str = input().strip()
    row_int = []
    for char in row_str:
        if char == 'B':
            row_int.append(0)
        elif char == 'W':
            row_int.append(1)
        else:
            raise ValueError()
    board.append(row_int)

# 1 is white
# 0 is black
chess_white = [1, 0, 1, 0, 1, 0, 1, 0]
chess_black = [0, 1, 0, 1, 0, 1, 0, 1]

col = 0
row = 0
min = 64

for col in range(0, M-7):
    for row in range(0, N-7):
        temp_min = 0

        for i in range(col, col+8):
            if i%2==0:
                check_row = chess_white
            else:
                check_row = chess_black
            for j in range(row, row+8):
                if board[j][i] != check_row[j-row]:
                    temp_min += 1


        if temp_min > 32:
            temp_min = 64 - temp_min

        if min > temp_min:
            min = temp_min

print(min)