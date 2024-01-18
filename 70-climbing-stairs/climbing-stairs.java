class Solution {
    public int climbStairs(int n) {
      if(n < 4)
      return n;
      int f = 2, s = 3, t = 0;
      for(int i = 3; i < n; i++){
          t = f + s;
          f = s;
          s = t;
      }
        return t;
    }
}