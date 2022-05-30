import re
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = re.sub('\s+', ' ', s)
        
        li = s.split()
        return " ".join(li[::-1])
        