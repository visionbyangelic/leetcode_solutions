# 🟦 LeetCode 3314: Bitwise User Array I

## 1. The Core Idea
We are looking for the smallest integer `ans` such that `ans | (ans + 1) == nums[i]`. 

For any number `n`, performing `n | (n + 1)` effectively takes the rightmost `0` in binary and turns it into a `1`. To find the **smallest** original number, we need to find the **last bit** in that block of trailing ones and turn it back into a `0`.

---

## 2. The Logic of Your Code

### Step 1: Filter Even Numbers
If a number is even (like `2` or `10`), it ends in `0`. Any `x | (x + 1)` will always result in an **odd** number. Therefore, if `n` is even, no solution exists.
* **Code:** `if n & 1:` (Checks if the number is odd).

### Step 2: The Bitwise Calculation
For an odd number, we need to flip the **lowest** bit of the **trailing ones** sequence.
* **Example:** `n = 11` (Binary `1011`).
* We want to turn the `1` at the `2`'s place off to get `9` (Binary `1001`).



---

## 3. The Full Code Gist

```python
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            # If the number is odd, we can find a result
            if n & 1:
                # 1. (n + 1) & ~n : Finds the first '0' bit from the right
                # 2. >> 1 : Moves that bit one position right to the last '1'
                # 3. ~ (...) : Creates a mask to turn that specific bit OFF
                # 4. n & ... : Applies the mask to get the smallest x
                res.append(n & ~(((n + 1) & ~n) >> 1))
            else:
                # Even numbers cannot be formed by x | (x + 1)
                res.append(-1)
        return res

```

---

## 4. Line-by-Line Breakdown

If **n = 15** (Binary `1111`):

1. **`(n + 1)`**: `16` (Binary `10000`)
2. **`~n`**: (Binary `...0000`) — The inverse of 15.
3. **`(n + 1) & ~n`**: `16` (Binary `10000`). This isolates the bit that "flipped" the trailing ones.
4. **`>> 1`**: `8` (Binary `01000`). This points exactly to the highest bit of the original trailing ones.
5. **`n & ~(8)`**: `15 & ~8`  `1111 & 0111` = `0111` (**7**).

**Verification:** `7 | (7 + 1)`  `7 | 8` = `15`. It works!




---
<img width="1326" height="677" alt="image" src="https://github.com/user-attachments/assets/def9d833-6779-4846-96a3-fe036cee3d01" />
