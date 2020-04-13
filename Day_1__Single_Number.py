'''
Problem Statement -> Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note -> Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1 -> Input: [2,2,1], Output: 1
Example 2 -> Input: [4,1,2,1,2], Output: 4
'''

#Solution 1 Using HashMap : Time - O(n), Space O(n)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_count = {}
        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1
                
        for i in num_count:
            if num_count[i] == 1:
                return i
                
#Solution 2 Using Bit Manipulation : Time - O(n), Space O(1)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res = res^i
        return res
                
