# def twoSum(nums, target):
#     d = {num: i for i, num in enumerate(nums)}
#     for num, ind in d.items():
#         complement = target - num
#         if complement in d and d[complement] != ind:
#             return [ind, d[complement]]
#     return None


def twoSum(nums, target):
    for ind1, num1 in enumerate(nums):
        for ind2, num2 in enumerate(nums):
            if ind1 != ind2 and num1 + num2 == target:
                return [ind1, ind2]
    return None

    # d = {}
    # for i, num in enumerate(nums):
    #     if num in d:
    #         d[num].append(i)
    #     else:
    #         d[num] = [i]
    #
    # for num, inds in d.items():
    #     complement = target - num
    #     if complement in d and d[complement] != inds:
    #         return [inds[0], d[complement][0]]
    # return None

nums = [3,3]
target = 6
print(twoSum(nums, target))