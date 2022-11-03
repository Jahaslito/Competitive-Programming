class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sums = []
        leftPointer, rightPointer = 0, len(nums) - 1 
        
        while leftPointer < rightPointer:
            sums.append(nums[leftPointer] + nums[rightPointer])
            leftPointer += 1
            rightPointer -= 1
        return max(sums)