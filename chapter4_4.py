n, m = map(int, input().split())
x, y, d = map(int, input().split())
direction = [0, 1, 2, 3]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

matrix = [[0 for _ in range(m)] for _ in range(n)]

for i in matrix:
    for j in range(len(i)):
        # input 제한하기
        i[j] = map(int, input().split())
