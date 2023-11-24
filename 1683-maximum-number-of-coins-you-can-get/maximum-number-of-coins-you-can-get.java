class Solution {
    public int maxCoins(int[] piles) {
        Arrays.sort(piles);
        int count = piles.length/3;
        int i=piles.length-2;
        int sum=0;
        while (count>0){
            sum+=piles[i];
            i-=2;
            count--;
        }
        return sum;
    }
}