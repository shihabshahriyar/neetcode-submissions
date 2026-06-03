class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexSet = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in indexSet:
                return [indexSet[complement], i]
            else:
                indexSet[num] = i