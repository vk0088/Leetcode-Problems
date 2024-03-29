class Solution:
    # Intuitions
    # Using sliding window,
        #1. Find a smallest window with atleast k max_element count
        #2. fact: If there are x elements to the left of window,
            # then ans is incremented by x. but how?

            # adding each elements to the smallest window found in step 1.
                #we will still get a valid window

    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_element=max(nums)
        #using left and right pointers
        l=0
        r=0
        ans=0
        while r<len(nums):
            #expanding right
            if nums[r]==max_element:
                k-=1
            # found a window but shrinking left to find small window
            while k==0:
                if nums[l]==max_element:
                    k+=1
                l+=1
            #adding no of elements to the left of the window
            ans+=l
            #find a new small window
            r+=1
        return ans





        