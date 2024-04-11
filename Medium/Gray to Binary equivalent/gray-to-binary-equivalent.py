#User function Template for python3

class Solution:    
    ##Complete this function
    # function to convert a given Gray equivalent n to Binary equivalent.
    def grayToBinary(self,n):
        ##Your code here
        bi=bin(n)[2:]
        g=[0]
        for i in bi:
            temp=int(i)^g[-1]
            g.append((temp))
        g=[str(i) for i in g]
        g.pop(0)
        g=''.join(g)
        g=int(g,2)
        return g

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        print(ob.grayToBinary(n))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends