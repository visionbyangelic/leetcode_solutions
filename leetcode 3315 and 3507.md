# 🟦 LeetCode 3315: Construct the Minimum Bitwise Array II And 🟦 LeetCode 3507: Minimum Pair Removal to Sort Array I

## 1. The Core Idea
We need to find the smallest number `ans` where `ans | (ans + 1) == nums[i]`. 

In binary, the operation `x | (x + 1)` takes the lowest `0` and turns it into a `1`. To reverse this and find the smallest possible `ans`, we need to find the **lowest continuous block of 1s** in the binary number and turn the **last 1** in that block back into a `0`.

---

## 2. The Logic of Your Code

### Step 1: The "2" Exception
The problem states `nums` contains prime integers. The only even prime is **2**.
- Binary of 2 is `10`. 
- No `x | (x + 1)` can result in `10` because that operation always results in an odd number (ending in `1`).
- **Code:** `if n != 2:` (Handles all odd primes).

### Step 2: The Bitwise Trick `(n + 1) & (-n - 1)`
This is a high-level bitwise shortcut to find the value of the **lowest zero bit**.
- `-n - 1` is mathematically the same as `~n` (the bitwise NOT).
- `(n + 1) & ~(n)` isolates the bit that represents the first `0` from the right.



### Step 3: Dividing by 2
By dividing that isolated bit by 2 (using `// 2`), you target the bit immediately to its right—which is the **highest bit of the trailing ones**. Subtracting this from `n` flips that `1` to a `0`.

---

## 3. Full Code Gist

```python
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            # All primes except 2 are odd. 
            # Even numbers cannot be formed by x | (x + 1).
            if n != 2:
                # 1. (n + 1) & (-n - 1) finds the power of 2 
                #    corresponding to the first '0' from the right.
                # 2. // 2 finds the power of 2 for the last '1' 
                #    in the trailing ones block.
                # 3. Subtracting it from n flips that '1' to '0'.
                ans.append(n - ((n + 1) & (-n - 1)) // 2)
            else:
                # No solution for n = 2
                ans.append(-1)
        return ans

```

---

## 4. Manual Trace Example

Let's use **n = 11** (Binary `1011`):

1. **`n + 1`**: `12` (Binary `...01100`)
2. **`-n - 1`**: (Same as `~11`)  Binary `...10100`
3. **`(n + 1) & (-n - 1)`**:
* `01100` & `10100` = `00100` (Decimal **4**)


4. **`4 // 2`**: **2**
5. **`n - 2`**: `11 - 2 = 9` (Binary `1001`)

**Check:** `9 | (9 + 1)`  `9 | 10`  `1001 | 1010` = `1011` (**11**).
The logic successfully found the smallest value!


---
<img width="1323" height="682" alt="image" src="https://github.com/user-attachments/assets/ed9844c3-e9ab-487a-b5c3-7218d24dfe56" />
---
# 🟦 LeetCode 3507: Minimum Pair Removal to Sort Array I

This problem, **LeetCode 3507: Minimum Pair Removal to Sort Array I**, is a simulation problem. Even though the goal is to find the *minimum* number of operations, the rules are very strict about which pair you must pick, which actually simplifies things: you don't have to decide what to pick; the problem tells you.

---

### 1. The Core Rules

You are looking for the "Stop" condition: the array becomes **non-decreasing** ().

Until then, you must:

1. Find the **minimum sum** of any two adjacent elements.
2. If there's a tie, take the **leftmost** one.
3. Combine them into one number (their sum).
4. Count how many times you did this.

---

### 2. The Strategy: "Greedy Simulation"

Because the constraints are very small (), we can simply **simulate** the process exactly as described. We don't need fancy math; we just need a loop that keeps merging until the array is sorted.

#### Step-by-Step Logic:

1. **Check:** Is the array already sorted? If yes, return 0.
2. **Find:** Loop through the array and calculate  for every index.
3. **Identify:** Keep track of the smallest sum found and the index where it happened.
4. **Merge:** Replace  and  with their sum. (In Python, `nums[i:i+2] = [new_sum]`).
5. **Repeat:** Go back to Step 1 and increment your operation counter.

---

### 3. The Code Gist (Beginner Friendly)


## A. The Concept
This is a **Simulation** problem. The rules tell us exactly which pair to pick in every step. We just need to follow those instructions until the array is sorted (non-decreasing).

## B. Why Simulation Works
The array size is very small (max 50 elements). Even if we reduce the array one element at a time, we will only perform a maximum of 49 operations. This is very fast for a computer.

---

## C. Python Solution

```python
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_sorted(arr):
            # Check if every element is <= the next one
            for i in range(len(arr) - 1):
                if arr[i] > arr[i+1]:
                    return False
            return True
        
        operations = 0
        
        # Simulation: keep merging until non-decreasing
        while not is_sorted(nums):
            min_sum = float('inf')
            best_idx = -1
            
            # 1. Find the adjacent pair with the minimum sum
            for i in range(len(nums) - 1):
                current_sum = nums[i] + nums[i+1]
                if current_sum < min_sum:
                    min_sum = current_sum
                    best_idx = i
            
            # 2. Replace the leftmost pair with their sum
            new_val = nums[best_idx] + nums[best_idx + 1]
            nums[best_idx : best_idx + 2] = [new_val]
            
            # 3. Increment counter
            operations += 1
            
        return operations

```

---

## 4. Example Trace

**Input:** `nums = [5, 2, 3, 1]`

1. **Check:** `[5, 2, 3, 1]` is not sorted.
2. **Find Pairs:** (5+2=7), (2+3=5), (3+1=4).
3. **Minimum:** 4 is the smallest.
4. **Merge:** `[5, 2, 4]`. (Op count: 1)
5. **Check:** `[5, 2, 4]` is not sorted.
6. **Find Pairs:** (5+2=7), (2+4=6).
7. **Minimum:** 6 is the smallest.
8. **Merge:** `[5, 6]`. (Op count: 2)
9. **Check:** `[5, 6]` IS sorted. **Return 2.**



### Key Takeaway for Beginners
In many "Easy" LeetCode problems, if the constraints (like $N=50$) are very small, the best approach is often the most direct one: **do exactly what the prompt says.**



---

<img width="1320" height="680" alt="image" src="https://github.com/user-attachments/assets/4826cd85-4d94-45b0-97d1-634bbf518b1d" />
