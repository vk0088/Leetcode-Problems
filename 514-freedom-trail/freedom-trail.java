class Solution {
    public int findRotateSteps(String ring, String key) {
        List<Integer>[] letterIds = new List[26];
        int n = ring.length(), k = key.length();
        int[][] memo = new int[n][k];

        for (int i = 0; i < n; i++) {
            char c = ring.charAt(i);
            if (letterIds[c - 'a'] == null) {
                letterIds[c - 'a'] = new ArrayList<Integer>();
            }
            letterIds[c - 'a'].add(i);
        }

        return dp(ring, key, letterIds, 0, 0, memo);
    }

    private int dp(String ring, String key, List<Integer>[] letterIds, int ringPtr, int keyPtr, int[][] memo) {
        int n = ring.length(), k = key.length();
        if (keyPtr == k) return 0; // base case
        if (memo[ringPtr][keyPtr] > 0) return memo[ringPtr][keyPtr];
        char target = key.charAt(keyPtr);
        int minMoves = Integer.MAX_VALUE;
        for (int targetIdx : letterIds[target - 'a']) {
            int currSteps = calcSteps(n, ringPtr, targetIdx);
            int furtherSteps = dp(ring, key, letterIds, targetIdx, keyPtr + 1, memo);
            minMoves = Math.min(minMoves, currSteps + furtherSteps);
        }
        memo[ringPtr][keyPtr] = minMoves;

        return memo[ringPtr][keyPtr];
    }

    private int calcSteps(int len, int i, int j) {
        int diff = Math.abs(i - j);
        int rotationSteps = Math.min(diff, len - diff);
        return rotationSteps + 1; // plus 1 more cost for spelling
    }
}