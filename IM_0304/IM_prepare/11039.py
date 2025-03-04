# 사각형 찾기(11039, sw)

import sys
sys.stdin = open(r"C:\Users\twony\Desktop\SWEA\IM_prepare\11039.input.txt", "r", encoding="utf-8")

def find_largest_rectangle(N, arr):
    max_area = 0  # 최대 직사각형 넓이 저장

    for i in range(N):  # 모든 행(i)
        for j in range(N):  # 모든 열(j)
            if arr[i][j] == 1:  # 1이 있는 곳에서 시작
                width = 0
                while j + width < N and arr[i][j + width] == 1:  # 가로 확장
                    width += 1

                    # 현재 width에 대해 최대 높이 찾기
                    height = 0
                    while i + height < N:  # 아래 방향으로 확장
                        valid = True  # 이 높이(height)가 유효한지 체크
                        for w in range(width):  # width 범위의 모든 칸이 1이어야 함
                            if arr[i + height][j + w] == 0:
                                valid = False
                                break
                        if not valid:
                            break
                        height += 1  # 높이 확장

                    max_area = max(max_area, width * height)  # 최대 넓이 갱신

    return max_area


# 입력 처리
T = int(input())  # 테스트케이스 개수
for tc in range(1, T + 1):
    N = int(input())  # 배열 크기
    arr = [list(map(int, input().split())) for _ in range(N)]  # 2D 배열 입력

    result = find_largest_rectangle(N, arr)
    print(f'#{tc} {result}')



# import sys
# sys.stdin = open("11039.input.txt", "r")

# def find_square(N, arr):
#     max_area = 0

#     for ci in range(N):
#         for cj in range(N):
#             if arr[ci][cj] == 1:
#                 width = 1
#                 height = 1
#                 ni, nj = ci, cj

#                 while nj + 1 < N and arr[ni][nj + 1] == 1:
#                     width += 1
#                     nj += 1
#                 while ni + 1 < N and arr[ni+1][nj] == 1:
#                     height += 1
#                     ni += 1

#                 max_area = max(width * height, max_area)

#     return max_area

# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]

#     result = find_square(N, arr)
#     print(f'#{tc} {result}')