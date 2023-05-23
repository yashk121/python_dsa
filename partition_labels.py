from ast import List
import sys
def partitionLabels( s: str):
    ans = []
    l = len(s)
    pivot = 0
    i=0
    while(i < l):

        # if s[i] in visited:
        #     i = i+1
        #     continue
        start_of_string = i
        pivot = i
        while( i <= pivot and i < l):
            f = s.find(s[i])
            e = s.rfind(s[i])

            if e > pivot:
                pivot = e
            i = i+1

        ans.append(pivot-start_of_string+1)

       

        

    return ans
    

class Solution:
    def jump(self, nums):
        return partitionLabels( nums)


if __name__ == '__main__':
    f = Solution()

    print(f.jump("ababcbacadefegdehijhklij"))
