class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j, val in reversed(list(enumerate(nums))):
                if nums[i] == val and i < j:
                    count += 1
        return count