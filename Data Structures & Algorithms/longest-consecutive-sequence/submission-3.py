class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        print(nums)
        if len(nums) == 0:
            return 0

        count = 1
        longest = 1
        for i, num in enumerate(nums):
            if i == 0:
                continue

            if num == nums[i - 1] + 1:
                count += 1
            else:
                count = 1

            if count >= longest:
                longest = count

        return longest
