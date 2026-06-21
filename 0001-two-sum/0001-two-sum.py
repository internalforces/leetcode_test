class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twosum = {}
        for i, num in enumerate(nums):

            complement = target - num

            if complement in twosum:

                return [twosum[complement], i]

            twosum[num] = i
        