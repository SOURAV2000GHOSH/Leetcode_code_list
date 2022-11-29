class RandomizedSet:

    def __init__(self):
        self.store=dict()
        self.arr=[]
        

    def insert(self, val: int) -> bool:
        if val not in self.store:
            l=len(self.arr)
            self.store[val]=l
            self.arr.append(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.store:
            indx=self.store[val]
            value=self.arr[-1]
            self.store[value]=indx
            self.arr[indx]=value
            self.store.pop(val)
            self.arr.pop()
            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()