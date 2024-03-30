

from typing import *
from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(
        self,
        nums: List[ int ],
        k: int
        ) -> int:
        
        left_index_included = 0
        counter_of_occurrences = defaultdict(int)
        result = 0
        
        for right_index_included, num in enumerate(nums):
            
            counter_of_occurrences[ nums[ right_index_included ] ] += 1
            
            if len( counter_of_occurrences ) == k + 1:
                
                while len( counter_of_occurrences ) == k + 1:
                    
                    counter_of_occurrences[ nums[ left_index_included ] ] -= 1
                    
                    if not counter_of_occurrences[ nums[ left_index_included ] ]:
                        del counter_of_occurrences[ nums[ left_index_included ] ]
                        
                    left_index_included += 1 # won't reach right index because k >= 1
            
            if len( counter_of_occurrences ) == k: # test necessary because we might be below k
                
                result += 1
                # print( nums[ left_index_included: right_index_included + 1 ] )
                left = left_index_included
                counter_copy = counter_of_occurrences.copy()
                
                while counter_copy[ nums[ left ] ] > 1:
                    counter_copy[ nums[ left ] ] -= 1
                    left += 1
                    result += 1
                    # print( nums[ left: right_index_included + 1 ] )
                    
        return( result )
                    
        
        