#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
		# code here
		ans=[]
		def calculate(indx,n,a,s,ans):
		    if indx>=n:
		        ans.append(s)
		        return
		    a.append(arr[indx])
		    s+=arr[indx]
		    calculate(indx+1,n,a,s,ans)
		    s-=arr[indx]
		    a.pop()
		    calculate(indx+1,n,a,s,ans)
		    
		calculate(0,N,[],0,ans)
		return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends