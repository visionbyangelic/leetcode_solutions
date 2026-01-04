# 2154 | Keep Multiplying Found Values by Two 🔢 — LeetCode Day 10

## 🧩 The Challenge
You are given an array of integers `nums` and a starting integer `original`.

- If `original` is found in `nums`, you multiply it by **two**
- You must **repeat this process** until the new value is **no longer present** in the array

---

## 💡 The “Aha!” Moment
This problem is a **chain reaction**.

A simple `if` statement won’t work because:
- Every time we double the value,
- We must check the array **again** for the new number.

The realization:  
👉 a **`while` loop** is perfect here — it keeps running until the condition finally fails.

---

## 🛠️ My Strategy: *The Continuous Search Method*

### Mechanism
- **The Loop**:  
  Use `while original in nums`  
  → “As long as this value exists, keep going.”

- **The Doubling**:  
  Inside the loop, update `original = original * 2`

- **The Exit**:  
  Once the doubled value is no longer in `nums`, the condition becomes `False` and the loop stops.

- **The Return**:  
  Return the final value of `original`.

---

## 🐍 Python Implementation

```python
class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        # Keep searching and doubling as long as the value is found
        while original in nums:
            original = 2 * original 
        
        # Once the loop breaks, we've found the final value
        return original
```



<img width="375" height="99" alt="image" src="https://github.com/user-attachments/assets/98ee2db3-f327-4da2-8cff-182dcb0a7ed0" />

