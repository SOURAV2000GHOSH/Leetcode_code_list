import heapq as h

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp=[]
        for el in nums:
            if len(hp)<k:
                h.heappush(hp,el)
            else:
                if hp[0]<el:
                    h.heappop(hp)
                    h.heappush(hp,el)
        return hp[0]
        