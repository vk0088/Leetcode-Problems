class Solution {
    class Tuple {
        int start;
        int end ;
        int profit;
        Tuple(int a,int b,int c){
            start =a;
            end =b;
            profit =c;
        }
    }
    public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {
        List<Tuple> list = new ArrayList<>();
        for(int i=0;i<profit.length;i++){
            list.add(new Tuple(startTime[i],endTime[i],profit[i]));   
        }
      Collections.sort(list, (a,b) -> a.start - b.start);
      int[] dp = new int[list.size()];
      Arrays.fill(dp,-1);
      return dfs(0,list,dp);
    } 
    private int dfs(int i,List<Tuple> list,int[] dp){
        if(i==list.size())return 0;
        if(dp[i]!=-1)return dp[i];
        int start = i+1;
        int end = list.size()-1;
        int ind =list.size();
        while(start<=end){
            int mid =start+(end-start)/2;
            if(list.get(mid).start>=list.get(i).end){
                ind =mid;
                end =mid-1;
            }
            else{
                start =mid+1;
            }
        }
        return dp[i] = Math.max(dfs(i+1,list,dp), list.get(i).profit+dfs(ind,list,dp));
    }
 }




  