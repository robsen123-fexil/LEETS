class Solution:
    def majority(self, nums: []) -> int:
        count = 0
        cand = 0
        n = len(nums)

        for num in nums:
            if count == 0:
                cand = num
            if num==cand:
                count += 1
            else:
                count -= 1

        return cand

# Example usage:
obj = Solution()
result = obj.majority([2,2,2,3,4,1,6,7])
print(result)
