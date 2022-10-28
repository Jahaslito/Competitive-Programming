class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        length = len(intervals)

        if length == 0 or length == 1:
           return intervals        

        intervals.sort(key=lambda x:x[0])
        output = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] <= output[-1][1]:
                output[-1][1] = max(output[-1][1], interval[1])
            else:
                output.append(interval)
            
        return output