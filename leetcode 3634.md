
# LeetCode 3634 Solution: Minimum Removals

### Problem Approach
The strategy is to find the **longest valid subarray** where the maximum element is no more than $k$ times the minimum element. Once we find this maximum length, the minimum number of removals is simply the total length of the array minus this maximum length.

### Implementation
```python
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        max_len = 0
        
        for j in range(len(nums)):
            while nums[j] > nums[i] * k:
                i += 1
            max_len = max(max_len, j - i + 1)
            
        return len(nums) - max_len

```

---

### Logic Breakdown

1. **Sorting**: We sort the array so that for any window `[i...j]`, `nums[i]` is the minimum and `nums[j]` is the maximum. This makes the condition `max <= min * k` easy to check.
2. **Sliding Window**:
* The `j` pointer expands the window by iterating through the array.
* The `while` loop shrinks the window from the left (`i += 1`) if the current element `nums[j]` exceeds the allowed range ().


3. **Maximum Window**: `max_len` tracks the largest window that satisfied the condition.
4. **Final Result**: To minimize removals, we maximize keeps. Result = `Total - Max Kept`.

### Complexity

* **Time Complexity**:  due to sorting. The sliding window traversal is .
* **Space Complexity**:  (ignoring the space used by the sorting algorithm).

```

