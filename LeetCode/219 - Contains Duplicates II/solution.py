class Solution:
    def containsNearbyDuplicate(self, nums, k):

        window = set()
        left = 0

        for right in range(len(nums)):

            while right - left > k:
                window.remove(nums[left])
                left += 1

            if nums[right] in window:
                return True

            window.add(nums[right])

        return False
