class Solution:
    def capitalizeTitle(self, title: str) -> str:
        if len(title)<3:
            return title.lower()
        i=0
        isfirst=True
        ans=[]
        while i<len(title):
            temp=[]
            if isfirst:
                while i<len(title):
                    if title[i]==" ":
                        i+=1
                        break                    
                    if isfirst:
                        temp.append(title[i].upper())
                        isfirst=False
                        i+=1
                    else:
                        temp.append(title[i].lower())
                        i+=1
            if len(temp)<3:
                temp[0]=temp[0].lower()
            ans.append("".join(temp))
            isfirst=True
        return " ".join(ans)
                    
                
                
        