class Solution:
    def findMin(self, nums: List[int]) -> int:
        x = nums[0]
        for num in nums:
            x = min(x, num)
        return x