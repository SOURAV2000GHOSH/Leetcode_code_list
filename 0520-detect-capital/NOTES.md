using map
​
```
class Solution:
def detectCapitalUse(self, word: str) -> bool:
cheakcapital=set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
cheaksmall=set("abcdefghijklmnopqrstuvwxyz")
if word[0] in cheakcapital:
issmall=False
for x in range(1,len(word)):
if word[x] not in cheakcapital:
if word[x] in cheaksmall:
issmall=True
continue
elif issmall:
return False
iscap=False
for x in range(1,len(word)):
if word[x] not in cheaksmall:
if word[x] in cheakcapital:
iscap=True
continue
elif iscap:
return False
else:
for x in range(1,len(word)):
if word[x] in cheakcapital:
return False
return True
```