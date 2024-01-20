class Solution {
    public int sumSubarrayMins(int[] arr) {
        // idx of the first number the right that is lower than current
        int[] lessFromRight = new int[arr.length]; 
        lessFromRight[arr.length - 1] = arr.length;
        for (int i = arr.length - 2; i >= 0; i--) {
            int p = i + 1;

            while (p < arr.length && arr[p] >= arr[i]) {
                p = lessFromRight[p];
            }
            lessFromRight[i] = p;
        }

        int sum = 0;
        for (int i = 0; i < arr.length; i++) {
            // there are total of arr.length - i subarrays starting from i
            // divide them into batches by minimum element

            int cur = arr[i];
            int curPos = i;
            while (curPos < arr.length) {
                int nextPos = lessFromRight[curPos];

                // all subarrays starting at i and ending at nextPos - 1 will have cur as minimum
                sum += cur * (nextPos - curPos);
                sum %= 1000000007;

                curPos = nextPos;
                cur = curPos < arr.length ? arr[curPos] : -1;
            }
        }
        return sum;
    }
}