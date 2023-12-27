class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int ans = Integer.MAX_VALUE;
        for (int i=0;i<nums.length;i++) {
            int a = nums[i];
            if (i > 0 && a == nums[i-1])
                continue;
            int l = i+1;
            int r = nums.length - 1;
            while (l < r) {
                int threeSum = a + nums[l] + nums[r];
                if (threeSum > target) {
                    ans = (Math.abs(target-threeSum) < Math.abs(target-ans)) ? threeSum : ans;
                    r--;
                }
                else if (threeSum < target) {
                    ans = (Math.abs(target-threeSum) < Math.abs(target-ans)) ? threeSum : ans;
                    l++;
                } 
                else {
                    ans = (Math.abs(target-threeSum) < Math.abs(target-ans)) ? threeSum : ans;
                    l++;
                    while (nums[l] == nums[l-1] && l < r)
                        l++;
                }
            }
        }
        return ans;
    }
}