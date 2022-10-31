class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        results = []

        l, r = 0, len(nums) - 1

        while len(results) != len(nums):
            results.append(nums[l])
            l += 1

            if l <= r:
                results.append(nums[r])
                r -= 1
        return results