class Solution {
    public int findJudge(int n, int[][] trust) {
        int[] trustCounts = new int[n+1];

        //Count the trust for each person
        for(int[] pair : trust){
            int trustingPerson= pair[0];
            int trustedPerson = pair[1];
            trustCounts[trustingPerson]--;
            trustCounts[trustedPerson]++;
        }
        //Check if there's a person trusted by everyone else 
        for(int i=1; i<=n; i++){
            if(trustCounts[i]== n-1){
                return i;
            }
        }
        return -1;
    }
}