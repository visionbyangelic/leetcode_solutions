
# 🟦 LeetCode 1984: Minimum Difference Between Highest and Lowest of K Scores

## 1. The Core Idea
To minimize the difference between the highest and lowest values in a group of $k$ students, we need those students to have scores as close as possible. By **sorting** the array, the values that are closest to each other will become neighbors.

Once sorted, any optimal group of $k$ students must be a **consecutive** sub-segment of the array.

---

## 2. Solution Strategy

### Step 1: Sorting
We sort the array in ascending order. This ensures that for any window of size $k$, the "lowest" score is at the start of the window and the "highest" score is at the end.

### Step 2: Sliding Window
We slide a window of size $k$ across the sorted array. 
- The window starts at index `i`.
- The window ends at index `i + k - 1`.
- The difference for that specific group is `nums[i + k - 1] - nums[i]`.



---

## 3. The Code

```python
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # Sort the array in ascending order to group similar values together
        nums.sort()
      
        # Find the minimum difference between max and min in any window of size k
        # We iterate through all possible windows of size k
        # For each window starting at index i, the difference is nums[i+k-1] - nums[i]
        return min(nums[i + k - 1] - nums[i] for i in range(len(nums) - k + 1))

```

---

## 4. Line-by-Line Beginner Breakdown

* **`nums.sort()`**: We organize the scores from smallest to largest.
* **`range(len(nums) - k + 1)`**: This loop ensures we stop sliding the window once the "right side" of the window hits the end of the array. If we have 5 elements and , we can only start at index 0, 1, or 2 ().
* **`nums[i + k - 1]`**: This looks at the student with the highest score in our current group of .
* **`nums[i]`**: This looks at the student with the lowest score in our current group of .
* **`min(...)`**: This keeps track of the smallest gap we found while sliding across the whole array.

## 5. Complexity Analysis

* **Time Complexity:**  because of the sorting step. The search through the windows is .
* **Space Complexity:**  (or  depending on the language's internal sort) because we modify the list in place.

---


---
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/93f2c30e-2d1c-4e7e-a47a-26e12e149c7e" />
