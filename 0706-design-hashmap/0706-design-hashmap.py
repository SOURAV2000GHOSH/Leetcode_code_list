class MyHashMap:

    def __init__(self):
        self.MyHashMap=[-1]*(10**6+1)
        self.cheak=set()
        

    def put(self, key: int, value: int) -> None:
        self.MyHashMap[key]=value
        self.cheak.add(key)
        

    def get(self, key: int) -> int:
        return self.MyHashMap[key]
        

    def remove(self, key: int) -> None:
        if key in self.cheak:
            self.MyHashMap[key]=-1
            self.cheak.remove(key)
            


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)