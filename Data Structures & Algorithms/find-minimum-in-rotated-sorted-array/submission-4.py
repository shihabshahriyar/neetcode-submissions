class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = 0
        R = len(nums) - 1
        result = nums[0]
        while L <= R:
            if nums[L] < nums[R]:
                result = min(result, nums[L])
                break

            M = (L + R) // 2
            result = min(result, nums[M])

            if nums[M] >= nums[L]:
                L = M + 1
            else:
                R = M - 1

        return result