from typing import List

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        len1 = len(nums1)
        len2 = len(nums2)
        dp = {}

        def solve(i, j):
            if (i, j) in dp:
                return dp[(i, j)]

            if i == len1 or j == len2:
                return float("-inf")

            take_both = nums1[i] * nums2[j] + solve(i + 1, j + 1)
            skip_first = solve(i + 1, j)
            skip_second = solve(i, j + 1)
            take_only = nums1[i] * nums2[j]

            dp[(i, j)] = max(
                take_both,
                skip_first,
                skip_second,
                take_only
            )
            return dp[(i, j)]

        return solve(0, 0)