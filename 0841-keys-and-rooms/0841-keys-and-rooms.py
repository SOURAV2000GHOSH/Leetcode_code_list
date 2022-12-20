class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        l=len(rooms)
        visited=[False]*l
        def solve(visited,source,rooms):
            visited[source]=True
            for node in rooms[source]:
                if not visited[node]:
                    solve(visited,node,rooms)
        solve(visited,0,rooms)
        return all(visited)