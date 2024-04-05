class Solution:
    def makeGood(self, s: str) -> str:
        while (m:=re.search(r'(.)(?!\1)(?i:\1)',s)):
            s = s.replace(m.group(0),'')
        return s