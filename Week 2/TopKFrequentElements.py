class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = Counter(nums) 
        # use heap to pop the smallest automatically
        import heapq
        container = []
        for element, freq in h.items():
            if len(container) < k:
                heapq.heappush(container, (freq, element))
            else:
                heapq.heappushpop(container, (freq, element)) 
        return [element for freq, element in container]