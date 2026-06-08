class Solution:
    def runningSum(self, nums):
        ans = []

        for i in range(len(nums)):
            total = 0

            for j in range(i + 1):
                total += nums[j]

            ans.append(total)

        return ans
