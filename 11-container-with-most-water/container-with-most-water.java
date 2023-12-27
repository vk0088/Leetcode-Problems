class Solution {
   
    public int maxArea(int[] height) {
        int res = -1;
        int leftP = 0;
        int rightP = height.length - 1;

        while (leftP < rightP) {
            int curLeft = height[leftP];
            int curRight = height[rightP];
            
            int cur = Math.min(curLeft, curRight) * (rightP - leftP);

            if (cur > res) {
                res = cur;
            }
            if(curLeft >= curRight) {
                //move right p
                rightP--;

            }
            else {
                leftP++;
            }
        }
        return res;
    }
}