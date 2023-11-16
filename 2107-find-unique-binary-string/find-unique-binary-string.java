class Solution {
    public String findDifferentBinaryString(String[] nums) {
        String s = "";
        for(int i=0;i<nums.length;i++){
            char ch = nums[i].charAt(i);
            if(ch == '0'){
                s+='1';
            }else{
                s+='0';
            }
        }
        return s;
    }
}