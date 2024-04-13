n = int(input())
move_list = input().split()
# L, R U, D
input_text = ["L", "R", "U", "D"]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
x = 1
y = 1

for move in move_list:
    if move in input_text:
        idx = input_text.index(move)
        nx = x + dx[idx]
        ny = y + dy[idx]
    if 1 <= nx and 1 <= ny <= n:
        x = nx
        y = ny

print(x, y)
