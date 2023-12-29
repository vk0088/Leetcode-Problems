class Solution {

    int[][][] dp;
    int n;
    public int minDifficulty(int[] jobDifficulty, int d) {
        n = jobDifficulty.length;
        if(n < d){
            return -1;
        }

        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += jobDifficulty[i];
        }
        if (sum == 0) {
            return 0;
        }

        dp = new int[n + 1][d + 1][1001];
        int count = minDiff(jobDifficulty, d, 0, 0);


        return count >= 10001 ? -1 : count;
    }

    public int minDiff(int[] jobDifficulty, int d, int i, int currMax){


        if(i == n && d == 0){
            return 0;
        }

        if(i == n && d != 0){
            return 10001;
        }

        if(d == 0 && i != n){
            return 10001;
        }

        if(dp[i][d][currMax] != 0){
            return dp[i][d][currMax];
        }
        
        currMax = Math.max(currMax, jobDifficulty[i]);

        int count = Math.min(
        minDiff(jobDifficulty, d, i + 1, currMax),
        currMax + minDiff(jobDifficulty, d - 1, i + 1, 0));

        dp[i][d][currMax] = count;

        return count;
    }
}