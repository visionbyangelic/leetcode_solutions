# 1975 | Maximum Matrix Sum 🧮 — LeetCode Day 11

## 🧠 Problem Summary
You are given an `n x n` integer matrix.  
In one operation, you may choose **any two adjacent elements** and multiply **both** by `-1`.

You may perform this operation **any number of times**.

👉 **Goal:** Return the **maximum possible sum** of the matrix after applying optimal operations.

---

## 💡 Key Observations

1. **Flipping two adjacent elements flips two signs**
   - This means negatives can cancel each other out.
   - Only the **parity (odd/even)** of negative numbers matters.

2. **Absolute values dominate the sum**
   - We want every number to be **positive** if possible.
   - So we sum the absolute value of every element.

3. **Odd number of negatives = one must stay negative**
   - If the total count of negative numbers is **odd**, one element must remain negative.
   - To minimize loss, that element should have the **smallest absolute value**.

---

## ✅ Strategy

- Traverse the matrix
- Track:
  - `total` → sum of absolute values
  - `negative_count` → number of negative elements
  - `min_abs` → smallest absolute value seen
- If `negative_count` is even → return `total`
- If odd → subtract `2 * min_abs` from `total`

---

## 🧪 Example Intuition

Matrix:
[[-1, 2],
[ 3, 4]]


- Absolute sum = `1 + 2 + 3 + 4 = 10`
- Negative count = `1` (odd)
- Smallest abs = `1`

➡️ Result = `10 - 2 * 1 = 8`

---

## 🧑‍💻 Python Solution

```python
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        min_abs = float('inf')
        negative_count = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                val = matrix[i][j]
                total += abs(val)

                if val < 0:
                    negative_count += 1

                min_abs = min(min_abs, abs(val))

        if negative_count % 2 == 0:
            return total
        else:
            return total - 2 * min_abs
```

⏱️ Complexity Analysis

Time Complexity: O(n²) Every element in the matrix is visited once.

Space Complexity: O(1) Only constant extra variables used.

🏁 Final Notes

This problem is not about simulation, It’s about:

- parity

- invariants

- minimizing unavoidable loss

---

PROOF
<img width="1330" height="720" alt="image" src="https://github.com/user-attachments/assets/81e297bb-2551-4e16-86a6-9e68f092d452" />


