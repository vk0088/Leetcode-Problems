class Solution {
    public int minOperations(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        // Making freq map of every elements.
        for (int i : nums) {
                map.put(i,map.getOrDefault(i,0)+1);
        }
        int operations = 0;
        // Iterating on the frequency of elements.
        for (int i:map.values()) {
            if (i == 1) {
                return -1;
            }          
                // we need add the divided value to operations.
                operations += (i+2) / 3;
            }
        return operations;
    }
}