'''
Problem Statement -> Given a binary array, find the maximum length of a contiguous subarray
                     with equal number of 0 and 1.
                     
Example -> Input: [0,1,0]
           Output: 2
           Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
'''

#Solution - Using HashMap : Time O(n), Space O(n)

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dd = {}
        dd[0] = -1
        count = 0
        max_length = 0
        for i in range(len(nums)):
            curr = nums[i]
            if curr == 0:
                count -= 1
            else:
                count += 1
                
            if count in dd:
                max_length = max(max_length, (i-dd[count]))
            else:
                dd[count] = i
            
        return max_length
        
