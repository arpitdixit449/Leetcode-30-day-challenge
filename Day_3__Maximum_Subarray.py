'''
Problem Statement -> 
        Given an integer array nums, find the contiguous subarray (containing at least one number)
        which has the largest sum and return its sum.
   
Example ->Input: [-2,1,-3,4,-1,2,1,-5,4],
          Output: 6
          Explanation: [4,-1,2,1] has the largest sum = 6.
'''

#Solution 1 Using Dynamic Programming : Time - O(n), Space O(n)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0 :
            return 
        if len(nums) == 1:
            return nums[0]
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1,len(dp)):
            if dp[i-1] + nums[i] > nums[i]:
                dp[i] = dp[i-1] + nums[i]
            else:
                dp[i] = nums[i]
                
        return max(dp)
       
#Solution 2 Kadane's Algorithm : Time - O(n), Space O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float("-inf")
        a = 0
        for i in nums:
            a += i
            ans = max(ans, a)
            a = max(a, 0)
        return ans
