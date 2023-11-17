class Solution {
    public int minPairSum(int[] nums) {
        Arrays.sort(nums);
        int max = 0;
        int start = 0, end = nums.length-1;

        while(start<end)
        {
            max = Math.max(max,nums[start++]+nums[end--]);
        }
        return max;
    }
}