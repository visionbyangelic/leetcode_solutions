
# LeetCode 1292: Maximum Side Length of a Square with Sum Less than or Equal to Threshold

### Problem Statement
Given a matrix `mat` and an integer `threshold`, return the maximum side-length of a square with a sum less than or equal to `threshold` or return 0 if there is no such square.

### Solution Explanation
This solution uses **Binary Search** combined with a **2D Prefix Sum** array to efficiently find the answer.

1.  **Prefix Sum Calculation ($O(M \cdot N)$):**
    First, we build a 2D prefix sum table. `prefix[i][j]` stores the sum of the rectangle from `(0,0)` to `(i-1, j-1)`. This allows us to calculate the sum of any sub-rectangle in $O(1)$ time using the inclusion-exclusion principle:
    $$Sum = P(r2, c2) - P(r1, c2) - P(r2, c1) + P(r1, c1)$$

2.  **Binary Search ($O(\log(\min(M,N)))$):**
    We need to find the maximum side length `k`. Since the property is monotonic (if a side length `k` works, any length smaller than `k` also works), we can binary search on the side length.
    * **Range:** 0 to `min(m, n)`.
    * **Check:** For a given `mid` (side length), we iterate through all possible squares of that size in the grid. If we find *any* square with `sum <= threshold`, then `mid` is a valid size, and we try to find a larger one (`left = mid + 1`). Otherwise, we look for a smaller one (`right = mid - 1`).

### Code

```python
class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        m, n = len(mat), len(mat[0])

        # Build 2D Prefix Sum Array
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = mat[i][j] + prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j]

        # Binary Search for the maximum side length
        left, right, ans = 0, min(m, n), 0
        while left <= right:
            mid = (left + right) // 2
            found = False
            
            # Iterate through all squares of size 'mid'
            for i in range(mid, m + 1):
                for j in range(mid, n + 1):
                    # Calculate sum of square using prefix sums
                    total = prefix[i][j] - prefix[i - mid][j] - prefix[i][j - mid] + prefix[i - mid][j - mid]
                    if total <= threshold:
                        found = True
                        break
                if found:
                    break
            
            if found:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
```
---
<img width="1322" height="685" alt="image" src="https://github.com/user-attachments/assets/28850fb8-bccd-49e6-942d-72840ae77644" />
