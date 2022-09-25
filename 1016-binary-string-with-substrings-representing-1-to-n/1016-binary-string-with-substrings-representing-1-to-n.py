class Solution:
    def queryString(self, s: str, n: int) -> bool:
        q=deque(['1'])
        for x in range(n):
            el=q.popleft()
            if el in s:
                q.append(el+'0')
                q.append(el+'1')
            else:
                return False
        return True
        