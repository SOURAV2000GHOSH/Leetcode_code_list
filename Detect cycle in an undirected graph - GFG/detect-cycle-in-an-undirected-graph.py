from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		visited=[False]*V
		def solve(adj,par,cur,visited):
		    visited[cur]=True
		    for node in adj[cur]:
		        if node==par:
		            continue
		        if visited[node]:
		            return True
		        if(solve(adj,cur,node,visited)):
		            return True
		    return False
		for i in range(V):
		    if not visited[i] and solve(adj,-1,i,visited):
		        return True
		return False


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends