class Solution:
    def minimumLength(self, s: str) -> int:
        i = 0
        j = len(s) - 1

        while i < j and s[i] == s[j]:
            tmp_var = s[i]

            while i <= j and s[i] == tmp_var:
                i += 1
            while i <= j and s[j] == tmp_var:
                j -= 1

        return (j - i + 1)