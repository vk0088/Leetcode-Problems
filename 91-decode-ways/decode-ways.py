from functools import lru_cache

class Solution:
    @lru_cache() # cache the result
    def numDecodings(self, s: str) -> int:
        # edge cases: `0`-start string can never form a valid combination
        if s.startswith('0'):
            return 0
        # last char
        elif len(s) <= 1:
            return 1
        num = 0
        # we can take two chars at a time for string starts with *1* like *11*, *13*.
        if s.startswith('1'):
            num += self.numDecodings(s[2:])
        # we can also take two chars for string starts with *2* as long as the next char is still valid.
        elif s.startswith('2') and s[1] in ['0', '1', '2', '3', '4', '5', '6']:
            num += self.numDecodings(s[2:])
        # select one char by default
        return num + self.numDecodings(s[1:])