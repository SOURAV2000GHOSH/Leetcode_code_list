class MedianFinder:

    def __init__(self):
        self.store=[]
        

    def addNum(self, num: int) -> None:
        self.store.append(num)
        

    def findMedian(self) -> float:
        self.store.sort()
        l=len(self.store)
        if l%2==1:
            return float(self.store[l//2])
        mean=(self.store[l//2]+self.store[(l//2)-1])/2
        return float(mean)
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()