class Solution {
    public int getLastMoment(int n, int[] left, int[] right) {
           int res = 0;
        for (int j : left) {
            res = Math.max(res, j);
        }
        for (int j : right) {
            res = Math.max(res, n - j);
        }
        return res;
    }
}