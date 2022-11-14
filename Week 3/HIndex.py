class Solution:
    def hIndex(self, citations: List[int]) -> int:
        hIndex = 0
        size = len(citations) 
        for i, count in enumerate(sorted(citations)):
            
            hIndex = max(hIndex, min(size - i, count)) 
        return hIndex