class Solution {
    public int garbageCollection(String[] garbage, int[] travel) {
        int ans = 0, a = 0, pm = 0, pg = 0, pp =0;
        for (int i = garbage.length -1; i > 0; i--){
            if(pm == 0 && garbage[i].contains("M")){
                a++;
                pm = 1;
            }
            if(pg == 0 && garbage[i].contains("G")){
                a++;
                pg = 1;
            }
            if(pp == 0 && garbage[i].contains("P") ){
                a++;
                pp = 1;
            }
            
          ans = ans + garbage[i].length()+ (a*travel[i-1]);

        }
        ans = ans + garbage[0].length();
    return ans;
    }
}