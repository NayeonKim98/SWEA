# 최대값(2566,bj)

arr = [list(map(int, input().split())) for _ in range(10)]
max_value = 0

for i in range(9):
    for j in range(9):
        cur_max = arr[i][j]
        max_value = max(cur_max, max_value)
        if max_value == cur_max:
            max_i, max_j = i, j

print(max_value)
print(f'{max_i + 1} {max_j + 1}')
