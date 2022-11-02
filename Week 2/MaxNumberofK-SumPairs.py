class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hash = defaultdict(int)
        operations = 0 
        
        for num in nums:
            target = k - num
            
            if hash[target] > 0:
                hash[target] -= 1
                operations += 1
            else:
                hash[num] += 1
                        
        return operations