class Solution:
  def maxScore(self, s: str) -> int:
    ans = -math.inf
    zeros = 0
    ones = 0
    
    #loop till s[-2]
    for i in range(len(s) - 1):
      if s[i] == '0':
        zeros += 1
      else:
        ones += 1
      ans = max(ans, zeros - ones)

    #check if last character is 1
    if s[-1]=='1':
        ones +=1

    return ans + ones