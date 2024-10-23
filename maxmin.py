"""maxmin"""
# L3 Challenge 3 Task 2

nums_1 = [2, 4, 1, 0, 2, -1]


def new_max(numbers):
    max = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] >= max:
            max = numbers[i]
            # print(max)
        else:
            # print("No change")
            max = max
            # print(max)
    return max


def new_min(numbers):
    min = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] <= min:
            min = numbers[i]
            # print(min)
        else:
            min = min
            # print("No change")
            # print(min)
    return min


"""print(new_max(nums_1))"""
"""print(new_min(nums_1))"""


def max_min(numbers):
    max_min_array = [new_min(numbers), new_max(numbers)]
    return max_min_array


print(max_min(nums_1))
