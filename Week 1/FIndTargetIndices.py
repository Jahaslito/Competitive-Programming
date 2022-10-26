class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sortedNums = sorted(nums)
        output = []
        for i in range(len(sortedNums)):
            if sortedNums[i] == target:
                output.append(i)
        return output