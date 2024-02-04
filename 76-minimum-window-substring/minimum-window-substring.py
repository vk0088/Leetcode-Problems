class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        # dictionary to track the characters from string t and their counts
        td = Counter(t)
        # our two pointers
        i, j = 0, 0
        # resi and resj are the result substring's starting and end positions and mnlen is to track the minimum length
        resi, resj, mnlen = 10**5 + 1, 10**5 + 1, 10**5 + 1
        while j < n:
            # we only hit this condition if we get the characters we care about (string t chars)
            if s[j] in td:
                # decreasing the count as we found (used) this character
                td[s[j]] -= 1
                # check if every character from t is found
                allpresent = all(v <= 0 for v in td.values())
                # while all are present repeat this block
                while allpresent:
                    # just update the mnlen and resultant pointers if all are present with smaller len
                    if j - i + 1 < mnlen:
                        mnlen = j - i + 1
                        resi, resj = i, j + 1
                    # important: try to increase the i pointer to shorten the substring and
                    # make sure that you are updating the count for that char in dictionary
                    # because we are unusing it (so it's available - hence count increased)
                    if s[i] in td:
                        td[s[i]] += 1
                    i += 1
                    # attendance of all characters same as previous one
                    allpresent = all(v <= 0 for v in td.values())
            j += 1
        return s[resi:resj]