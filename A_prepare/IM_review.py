def max_sublist_within_difference(nums):
    nums.sort()  # 정렬하여 연속적인 숫자들끼리 비교하기 쉽게 만든다.
    max_length = 0
    best_subset = []

    for i in range(len(nums)):
        subset = [nums[i]]

        for j in range(i + 1, len(nums)):
            if nums[j] - subset[0] <= 2:  # 차이가 2 이하인지 확인
                subset.append(nums[j])
            else:
                break  # 초과하면 중단

        if len(subset) > max_length:
            max_length = len(subset)
            best_subset = subset[:]

    return best_subset


# 예제 리스트
numbers = [3, 5, 1, 2, 6, 8, 10, 7, 4, 12, 15, 17, 14, 13, 9, 11, 16, 18, 19, 20]
result = max_sublist_within_difference(numbers)
print(result)