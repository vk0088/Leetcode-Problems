import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int numFactoredBinaryTrees(int[] arr) {
        int mod = (int) Math.pow(10, 9) + 7; // Define a modulo value to prevent integer overflow.
        Arrays.sort(arr); // Sort the input array in ascending order.
        Map<Integer, Long> mp = new HashMap<>(); // Create a map to store the count of factored binary trees for each number.
        mp.put(arr[0], 1L); // Initialize the count for the first element in the array.

        // Loop through the input array starting from the second element.
        for (int i = 1; i < arr.length; i++) {
            long cnt = 1; // Initialize the count for the current element.

            // Iterate through the elements in the map.
            for (Map.Entry<Integer, Long> entry : mp.entrySet()) {
                int el = entry.getKey(); // Get an element from the map.

                // Check if the current element in the array is divisible by the map element
                // and if the resulting factor is also present in the map.
                if (arr[i] % el == 0 && mp.containsKey(arr[i] / el)) {
                    // Calculate the count for the current element by multiplying counts of factors.
                    cnt += entry.getValue() * mp.get(arr[i] / el);
                }
            }

            mp.put(arr[i], cnt); // Store the computed count in the map for the current element.
        }

        long ans = 0; // Initialize the answer variable.

        // Calculate the total number of factored binary trees by summing up the counts in the map.
        for (long value : mp.values()) {
            ans = (ans + value) % mod; // Use modulo to keep the result within bounds.
        }

        return (int) ans; // Return the total number of factored binary trees.
    }
}