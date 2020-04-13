'''
Problem Statement -> Given an array nums, write a function to move all 0's
                     to the end of it while maintaining the relative order
                     of the non-zero elements.
                   
Example -> Input: [0,1,0,3,12]
           Output: [1,3,12,0,0]
           
'''

#Solution 1 : Time - O(n^2), Space - O(1)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        x = nums.count(0)
        while 0 in nums:
            nums.remove(0)
        for i in range(x):
            nums.append(0)
            
#Solution 2 : Time - O(n), Space - O(n)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nxt = 0
        for i in nums:
            if i != 0:
                nums[nxt] = i
                nxt += 1
        
        for i in range(nxt,len(nums)):
            nums[i] = 0
