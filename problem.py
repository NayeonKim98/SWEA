# def KFC(num):
#     if num == 5:
#         return
#     print(num)
#     KFC(num + 1)
#     print(num)
#
# KFC(0)
# print("끝")

path = []
# cnt = 재귀호출마다 누적되어 전달되어야 하는 값.
def recur(cnt):  # 보통 매개변수는 누적되는 것!!!!!!!!
    # 카드를 2 개 뽑으면 종료
    if cnt == 2:
        # 종료시에 해야할 로직 여기 작성
        print(*path)
        return

    # 1개의 카드를 뽑는다.
    path.append(0)
    # 다음 재귀호출 (뽑은 카드 1개가 추가)
    recur(cnt + 1)
    # 지나간 경로는 다시 안감.
    path.pop()

    path.append(1)
    recur(cnt + 1)
    path.pop()

    path.append(2)
    recur(cnt + 1)
    path.pop()

# 제일 처음 호출할 때 시점이므로, 초기값을 전달하면서 시작
recur(0)