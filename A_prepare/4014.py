# 활주로 건설

import sys
sys.stdin = open("4014.input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    impossible_count = 0

    # 가로 탐색
    for i in range(N):
        str_j = 0
        end_j = 0
        for j in range(N-1):
            if arr[i][j] - arr[i][j + 1] == 1:  # 옆 원소가 더 낮을 때
                str_j = j + 1
                for k in range(j + 2, N):
                    if arr[i][str_j] - arr[i][k] != 0 or k == N - 1:  # 높이가 달라지는 순간이거나 끝까지 갔을 때
                        end_j = k - 1

                if end_j - str_j + 1 < X:  # 그 구간의 길이가 주어진 활주로 길이보다 짧다면,
                    impossible_count += 1
                    break

            elif arr[i][j] - arr[i][j + 1] == -1:  # 옆 원소가 더 높을 때
                if arr[i][j] == arr[i][0]:  # 첫 번째 원소와 값이 같다면,
                    str_j = 0
                    end_j = j
                else:  # 첫 번째 원소와 값이 다르면
                    str_j = end_j + 1

                if end_j - str_j + 1 < X:  # 그 구간의 길이가 주어진 활주로 길이보다 짧다면,
                    impossible_count += 1
                    break

    # 세로 탐색
    for j in range(N):
        str_i = 0
        end_i = 0
        for i in range(N-1):
            if arr[i][j] - arr[i + 1][j] == 1:  # 옆 원소가 더 낮을 때
                str_i = i + 1
                for k in range(i + 2, N):
                    if arr[str_i][j] - arr[k][j] != 0 or k == N - 1:  # 높이가 달라지는 순간이거나 끝까지 갔을 때
                        end_i = k - 1

                if end_i - str_i + 1 < X:  # 그 구간의 길이가 주어진 활주로 길이보다 짧다면,
                    impossible_count += 1
                    break

            elif arr[i + 1][j] - arr[i][j] == -1:  # 옆 원소가 더 높을 때
                if arr[i][j] == arr[0][j]:  # 첫 번째 원소와 값이 같다면,
                    str_i = 0
                    end_i = i
                else:  # 첫 번째 원소와 값이 다르면
                    str_i = end_i + 1

                if end_i - str_i + 1 < X:  # 그 구간의 길이가 주어진 활주로 길이보다 짧다면,
                    impossible_count += 1
                    break

    result = 2 * N - impossible_count
    print(f'#{tc} {result}')