class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        m = collections.defaultdict(int)
        for v in arr:
            m[v] += 1

        l = []
        for k in m:
            l.append(m[k])

        l.sort(reverse=True)
        cnt = int((len(arr)+1)/2)

        i = 0
        while i<len(l):
            cnt -= l[i]
            if cnt <= 0:
                break
            i += 1
        return i+1