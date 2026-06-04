class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = { num: i for i, num in enumerate(nums)}
        output = []
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict and num_dict[complement] != i:
                output.append([complement, num])
        return output

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print(nums)
        output = []
        output_set = set()

        for i, num in enumerate(nums):
            twoSum = self.twoSum(nums[i+1:], num * -1)

            if len(twoSum) == 0:
                continue
            
            for doublet in twoSum:
                num2, num3 = doublet
                triplet = sorted([num, num2, num3])

                if tuple(triplet) in output_set:
                    continue

                output_set.add(tuple(triplet))
                output.append(triplet)

        return output