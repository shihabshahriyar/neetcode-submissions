class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_array = []
        postfix_array = []
        output = []

        for i, num in enumerate(nums):
            if i == 0:
                prefix_array.append(1)
            else:
                prefix_array.append(nums[i-1] * prefix_array[i-1])

        reversed_nums = list(reversed(nums))
        print(reversed_nums)
        for i, num in enumerate(reversed_nums):
            if i == 0:
                postfix_array.append(1)
            else:
                postfix_array.append(reversed_nums[i-1] * postfix_array[i-1])

        postfix_array = list(reversed(postfix_array))

        for i, num in enumerate(nums):
            output.append(prefix_array[i] * postfix_array[i])

        return output