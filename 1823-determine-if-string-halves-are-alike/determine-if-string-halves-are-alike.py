class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def count(s):
            c = 0
            check = ('a', 'e', 'i', 'o', 'u')
            for i in s:
                if i.lower() in check:
                    c+=1
            return c


        n = len(s)
        s1 = count(s[:n//2])
        s2= count(s[n//2:])
        return s1==s2