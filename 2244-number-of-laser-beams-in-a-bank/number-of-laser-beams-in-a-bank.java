class Solution {
    public int numberOfBeams(String[] bank) {
        List<Integer> list = new ArrayList<>();
        
        int res = 0;
        for(String str : bank){
            int countOnes = 0;
            for(char c : str.toCharArray()) if(c=='1') countOnes++;
            if(countOnes>0) list.add(countOnes);
        }
        
        int ans = 0;
        int n = list.size()-1;
        for(int i=0;i<n;i++){
            int val = list.get(i)*list.get(i+1);
            ans+=val;
        }
        
        return ans;
    }
}