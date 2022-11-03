class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        #check is use for storing the number of sequence and cheaking
        check=dict()
        #iteration_cheak is use for not
        iteration_cheak=set()
        ans=0
        mid=0
        for x in words:
            check[x]=1 if x not in check else check[x]+1
            
        for key in check.keys():
            if key in iteration_cheak:
                continue
            temp_key=key[::-1]
            if key==temp_key and temp_key in check:
                if check[key]%2==1:
                    mid=2
                if check[key]>1:
                    if check[key]%2==0:
                        ans+=check[key]*2
                    else:
                        ans+=(check[key]-1)*2
                
            elif temp_key in check:
                ans+=min(check[key],check[temp_key])*4
            iteration_cheak.add(temp_key)
        return ans+mid
                
            
            
            
        