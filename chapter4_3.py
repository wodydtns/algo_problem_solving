data = input()
column = ord(data[0]) - ord("a") + 1
row = data[1]
move_list = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, -2), (1, 2), (-1, -2), (-1, 2)]
count = 0

# x, y <= 8

for i in range(len(move_list)):
    next_row = int(row) + move_list[i][0]
    next_column = int(column) + move_list[i][1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        count += 1
print(count)
