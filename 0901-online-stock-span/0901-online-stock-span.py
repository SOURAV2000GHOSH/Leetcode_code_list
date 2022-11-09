class StockSpanner:

    def __init__(self):
        self.store=[]
    def next(self, price: int) -> int:
        count=1
        while len(self.store)>0 and self.store[-1][0]<=price:
            count += self.store[-1][1]
            self.store.pop()
        self.store.append([price,count]) 
        return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)