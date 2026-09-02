class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        j = 0
        max_count = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                j += 1
                max_count = max(max_count, j)
            else:
                j = 0

        return max_count