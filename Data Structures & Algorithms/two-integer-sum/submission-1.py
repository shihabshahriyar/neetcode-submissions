class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = { num: i for i, num in enumerate(nums) }
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict and i != num_dict[complement]:
                return [i, num_dict[complement]]
        return []