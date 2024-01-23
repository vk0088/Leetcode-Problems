class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ans=0
        def isunique(st):
            return len(set(st))==len(st)
        def helper(indx,temp):
            nonlocal ans
            if(indx==len(arr)):
                return
            
            if isunique(temp+arr[indx]):
                ans=max(ans,len(temp)+len(arr[indx]))
                helper(indx+1,temp+arr[indx])
            helper(indx+1,temp)
        
        helper(0,"")
        return ans
