"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""


def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    # Hash table solution to store and lookup complement number.
    # Time compexity: 0(N)
    # Space complexity: 0(N)

    complementTable = {}

    for i in range(0, len(nums)):
        complement = target - nums[i]

        if complement in complementTable:
            return [complementTable[complement], i]
        else:
            complementTable[nums[i]] = i

    return False
