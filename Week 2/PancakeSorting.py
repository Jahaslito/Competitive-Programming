class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(end):
            start = 0 
            while(start<end):
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        res = []
        for i in range(len(arr)-1, -1, -1):
            max_i = i 
            for j in range(i-1, -1, -1):
                if(arr[j]>arr[max_i]): max_i = j 
            if(max_i != i ):
                flip(max_i) 
                flip(i)
                res.append(max_i+1)
                res.append(i+1)
        return res
