class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans=address.split(".")
        return "[.]".join(ans)