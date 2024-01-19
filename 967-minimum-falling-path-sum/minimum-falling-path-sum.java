class Solution {
    Map<String, Integer> memo = new HashMap<>();
    public int minFallingPathSum(int[][] matrix) {
        int minSum = Integer.MAX_VALUE;
        for (int j=0; j< matrix.length;j++)
            minSum = Math.min(minSum, process(matrix, 0,j));
        return minSum;        
    }

    int process(int[][] matrix, int r, int c)
    {
        int min = Integer.MAX_VALUE;
        int sum = matrix[r][c];
        if (r+1== matrix.length) return sum;
        int a= c-1 <0 ? 0 : c-1;
        int b = (c+1> matrix[0].length -1) ? matrix[0].length -1 : c+1;
        for (int i =a ; i<=b; i++)
        {
            String key = Integer.valueOf(r+1) + ":" + Integer.valueOf(i);
            if (!memo.containsKey(key))
            {
                memo.put(key, process(matrix, r+1, i));
            }
            min = Math.min(min, memo.get(key));
        }
        return sum + min;      
    }
}