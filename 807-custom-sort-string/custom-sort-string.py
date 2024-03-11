class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        count={}
        ans=[]
        i=0
        set_order=set(order)
        for ele in s:
            if ele in count:
                count[ele]+=1
            else:
                count[ele]=1
        for ele in order:
            if ele in count:
                for j in range(count[ele]):
                    ans.append(ele)
                    i+=1
        for ele in count:
            if ele not in set_order:
                for j in range(count[ele]):
                    ans.append(ele)
        return ''.join(ans)