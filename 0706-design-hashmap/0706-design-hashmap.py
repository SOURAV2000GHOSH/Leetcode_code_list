class MyHashMap:

    def __init__(self):
        self.MyHashMap=dict()
        

    def put(self, key: int, value: int) -> None:
        self.MyHashMap[key]=value
        

    def get(self, key: int) -> int:
        return self.MyHashMap[key] if key in self.MyHashMap else -1
        

    def remove(self, key: int) -> None:
        if key in self.MyHashMap:
            self.MyHashMap.pop(key)
            


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)