class Solution {
    public List<List<Integer>> findMatrix(int[] nums) {
        int arr[]=new int[201];
        List<List<Integer>> ans=new ArrayList<>();
        boolean flag1=true;
        for(int i=0;i<nums.length;i++){
            arr[nums[i]]++;
        }
        for(int j=0;j<=200;j++){
            int count=arr[j];
            if(count>ans.size()){
                while(count!=ans.size()){
                    ans.add(new ArrayList<>());
                }
            }
            int k=0;
            while(count!=0){
                ans.get(k).add(j);
                count--;
                k++;
            }
        }
        return ans;
    }
}