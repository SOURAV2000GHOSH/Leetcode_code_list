#User function template for Python

class Solution:	
    #Function to reverse every sub-array group of size k.
	def reverseInGroups(self, arr, N, k):
		# code here
		start=0
		end=k-1
		while end<N:
		    tempStart=start
		    tempEnd=end
		    while tempStart<tempEnd:
		        arr[tempStart],arr[tempEnd]=arr[tempEnd],arr[tempStart]
		        tempEnd-=1
		        tempStart+=1
		    start=end+1
		    end+=k
    	if start<N:
    	    end=N-1
    	    while start<end:
    		     arr[start],arr[end]=arr[end],arr[start]
    		     start+=1
    		     end-=1

#{ 
 # Driver Code Starts
#Initial template for Python

import math
def main():
    T=int(input())
    while(T>0):
        nk=[int(x) for x in input().strip().split()]
        N=nk[0]
        K=nk[1]
        arr=[int(x) for x in input().strip().split()]
        
        ob = Solution()
        ob.reverseInGroups(arr,N,K)
        for i in arr:
            print(i,end=" ")
        print()
        T-=1

if __name__=="__main__":
    main()




# } Driver Code Ends