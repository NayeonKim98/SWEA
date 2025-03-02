# 종이 자르기

width, length = map(int, input().split())
cuts = int(input())
papper = [[0] * (width) for _ in range(length)]
cut_info = []

for _ in range(cuts):
    type, cut_num = map(int, input().split())
    cut_info.append([type, cut_num])

    if type == 0:  # 가로선이라면,
        for i in range(length):
            papper[cut_num][i].append()