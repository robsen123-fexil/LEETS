from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
       ar2=[0]*len(arr)
     
       for i in range(len(arr)):
          ar2[i]=max(arr[i+1,len(ar2)])
       return ar2

s = Solution()
input_arr = [17, 18, 5, 4, 6, 1]
output_arr = s.replaceElements(input_arr)
print(output_arr)
