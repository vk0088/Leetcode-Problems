class Solution {
    int min = Integer.MAX_VALUE;

    public int minimumOneBitOperations(int n) {
        // Base case: if n is 0 or 1, no further operations are needed
        if (n <= 1) {
            return n;
        }

        int count = 0;

        // Finding the position of the leftmost set bit in the binary representation of n
        while ((1 << count) <= n) {
            count++;
        }

        // Recursively calculate the minimum operations by clearing the leftmost set bit
        int recursiveResult = minimumOneBitOperations(n - (1 << (count - 1)));

        // Calculate the final result by subtracting the recursive result from (2^count - 1)
        return (1 << count) - 1 - recursiveResult;
    }
}