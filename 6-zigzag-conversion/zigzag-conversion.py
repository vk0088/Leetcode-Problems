class Solution:
    def convert(self, s: str, numRows: int) -> str:
        z=len(s)
        g=0
        move=0
        ls=[]
        k=0
        while k<len(s):
            if g==0:
                move+=1

            else:
                move-=1

            if move==numRows:
                g=1

            elif move<=1:
                g=0   

            if k<numRows:
                ls.append([s[k]])

                
            else:
                ls[move-1].append(s[k]) 

            k+=1

        word=""    
        for i in ls:
            word+="".join(i)
        return word