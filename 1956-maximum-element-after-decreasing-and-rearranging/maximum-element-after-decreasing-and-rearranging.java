class Solution {
    public int maximumElementAfterDecrementingAndRearranging(int[] arr) {
        Arrays.sort(arr);
        arr[0] = 1;
        for(int i=0 ; i<arr.length-1 ; i++){
            if(Math.abs(arr[i] - arr[i+1]) <= 1){  
              
            }else{
                arr[i+1] = arr[i]+1;
            }
        }
        return arr[arr.length-1];
    }
}