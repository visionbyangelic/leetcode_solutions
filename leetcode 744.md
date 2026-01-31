
# LeetCode #744: Find Smallest Letter Greater Than Target
**Date:** January 31, 2026
**Topic:** Binary Search (Boundary Finding)
**Difficulty:** Easy

---

## 1. The Problem Explained (Newbie Version)
Imagine you have a row of sorted letter tiles on a table. I give you a "Target" letter. Your job is to find the **very first tile** that comes after the target in the alphabet. 

### The Rule:
* You need the smallest letter that is **strictly greater** than the target.
* **The "Wrap-Around" Twist:** If the target is 'z' (or any letter larger than everything on the table), you loop back to the beginning and pick the very first tile.

---

## 2. The Strategy: Binary Search
Since the letters are **sorted**, we don't need to check them one by one (Linear Search). Instead, we use **Binary Search** to find the "boundary" where the letters stop being "less than or equal to target" and start being "greater than target."

### How the pointers move:
1. Start with `left` at the beginning and `right` at the end.
2. Find the `mid` point.
3. **If `letters[mid]` is <= target:** The answer is definitely to the right. Move `left = mid + 1`.
4. **If `letters[mid]` is > target:** This could be our answer! But there might be a smaller one to the left. So, move `right = mid - 1`.



---

## 3. The Code (Python)

```python
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # 1. Initialize our search boundaries
        left, right = 0, len(letters) - 1
        
        # 2. Binary Search Loop
        while left <= right:
            mid = (left + right) // 2
            
            # If current letter is not big enough, move right
            if letters[mid] <= target:
                left = mid + 1
            # If current letter is bigger, it's a candidate; move left to find smaller ones
            else:
                right = mid - 1
        
        # 3. The Result
        # After the loop, 'left' points to the smallest letter > target.
        # We use % (modulo) to handle the wrap-around case.
        # If left == len(letters), left % len(letters) becomes 0.
        return letters[left % len(letters)]

```

---

## 4. Complexity Analysis

* **Time Complexity:**  — We cut the search space in half with every step.
* **Space Complexity:**  — We only use two pointers (`left` and `right`), no matter how big the input is.

---

## 5. Key Takeaway 

When a problem says **"Sorted"** and asks for the **"Smallest element greater than X,"** it is a classic **Binary Search Successor** problem. The binary search doesn't just find exact matches; it finds the "split point" between two conditions.
