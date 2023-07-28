class Solution {
    public int solve(int[][] dp,int []v,int i,int j,int k){
        if(i>j)return 0;
        if(dp[i][j]!=-1)return dp[i][j];
        int first=0,last=0,ans=0;
        if(k%2==0){// it's player 1's turn
            first=v[i]+solve(dp,v,i+1,j,k+1);
            last=v[j]+solve(dp,v,i,j-1,k+1);
            ans=Math.max(first,last);
        }
        else{// it's player 2's turn
            first=-v[i]+solve(dp,v,i+1,j,k+1);
            last=-v[j]+solve(dp,v,i,j-1,k+1);
            ans=Math.min(first,last);
        }
        return dp[i][j]=ans;
    }
    public boolean PredictTheWinner(int[] v) {
        int i,n=v.length;
        int[][] dp=new int[n][n];
        for(i=0;i<n;i++)Arrays.fill(dp[i],-1);
        return solve(dp,v,0,n-1,0)>=0;
    }
}
