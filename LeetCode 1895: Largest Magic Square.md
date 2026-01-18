# 🧠 Breaking Down LeetCode 1895: Largest Magic Square
**Difficulty:** Medium | **Topic:** Array, Matrix, Prefix Sum

## 1. The Goal
We need to find the **largest possible square** (size `k x k`) inside a grid where:
1. Every **row** sums to the same number.
2. Every **column** sums to the same number.
3. Both **diagonals** (main and anti) sum to that same number.

If no magic square exists larger than 1x1, the answer is always `1`.

---

## 2. The "Aha!" Moment (Analyzing Constraints)
Before writing code, look at the constraints.
* `m` (rows) and `n` (cols) are at most **50**.

**What this tells us:**
Usually, in DSA, we fear $O(N^3)$ or $O(N^4)$ solutions. But because $N$ is so small ($50$), even an $O(N^4)$ solution results in roughly ~6 million operations, which is well within the time limit (usually ~100 million ops).

**The Strategy:**
We don't need a complex dynamic programming trick. We can use **"Smart Brute Force"**:
1.  Check every possible square size `k`.
2.  Check every possible position `(row, col)`.
3.  Validate if it's "Magic".

---

## 3. The Problem with "Dumb" Brute Force
If we just use loops for everything, checking one square takes too long.
* To check a $10 \times 10$ square, you sum 10 rows + 10 cols + 2 diagonals.
* Doing this repeatedly for every spot in the grid is inefficient.

**The Solution: The "Cheat Sheet" (Prefix Sums)**
We can pre-calculate the sums so we don't have to add numbers one by one every time.

### The 1D Concept
Imagine a row: `[3, 1, 4, 2]`
* If I ask: "Sum of index 1 to 3?", you do `1+4+2 = 7`.
* **Prefix Array:** `[0, 3, 4, 8, 10]` (Running total).
* **Math:** `Prefix[4] - Prefix[1]` = `10 - 3 = 7`.
* **Result:** We turned a loop (slow) into a subtraction (instant/O(1)).

---

## 4. The Algorithm (Step-by-Step)

### Step 1: Pre-computation
Create two "Cheat Sheets" (2D Matrices):
1.  `rowSum[i][j]`: Sum of row `i` up to column `j`.
2.  `colSum[i][j]`: Sum of column `j` up to row `i`.

### Step 2: Search Strategy (Greedy)
We want the **largest** square.
* Don't start at `k=2` and go up.
* Start at `k = min(rows, cols)` (the biggest possible size) and count **down**.
* **Why?** The moment we find *any* valid magic square, we know it's the largest possible one. We return immediately. fast!

### Step 3: The Validation Loop
For a specific square at `(r, c)` of size `k`:
1.  **Diagonals:** Calculate these manually with a simple loop. If `diag1 != diag2`, fail immediately.
2.  **Rows:** Use `rowSum` cheat sheet to check if all rows equal `diag1`.
3.  **Cols:** Use `colSum` cheat sheet to check if all cols equal `diag1`.

---

## 5. Python Implementation (Heavily Commented)

```python
class Solution:
    def largestMagicSquare(self, grid: list[list[int]]) -> int:
        R, C = len(grid), len(grid[0])
        
        # --- PHASE 1: Build the Cheat Sheets (Prefix Sums) ---
        # We make them (R+1) x (C+1) to handle "zero" boundaries easily.
        row_prefix = [[0] * (C + 1) for _ in range(R)]
        col_prefix = [[0] * (C + 1) for _ in range(R + 1)]
        
        for r in range(R):
            for c in range(C):
                # Standard prefix sum formula: current val + previous total
                row_prefix[r][c+1] = row_prefix[r][c] + grid[r][c]
                col_prefix[r+1][c] = col_prefix[r][c] + grid[r][c]

        # --- PHASE 2: The Helper Function ---
        def is_magic(r, c, k):
            """Checks if square at (r,c) with size k is Magic"""
            
            # 1. Check Diagonals (Manual Loop - Fast enough)
            d1, d2 = 0, 0
            for i in range(k):
                d1 += grid[r+i][c+i]           # Top-left to bot-right
                d2 += grid[r+i][c+k-1-i]       # Top-right to bot-left
            
            if d1 != d2: return False
            target = d1 # This is the number every row/col must match
            
            # 2. Check Rows (Using Cheat Sheet)
            for i in range(k):
                # Formula: Sum(start, end) = Prefix[end+1] - Prefix[start]
                current_row_sum = row_prefix[r+i][c+k] - row_prefix[r+i][c]
                if current_row_sum != target: return False
            
            # 3. Check Cols (Using Cheat Sheet)
            for j in range(k):
                current_col_sum = col_prefix[r+k][c+j] - col_prefix[r][c+j]
                if current_col_sum != target: return False
                
            return True

        # --- PHASE 3: The Search (Largest to Smallest) ---
        max_possible_size = min(R, C)
        
        # Loop k downwards: 50 -> 49 -> ... -> 2
        for k in range(max_possible_size, 1, -1):
            # Try every possible top-left coordinate (r, c)
            # limiting range so the square doesn't go out of bounds
            for r in range(R - k + 1):
                for c in range(C - k + 1):
                    if is_magic(r, c, k):
                        return k # Found the biggest one!
        
        return 1 # Fallback: A 1x1 square is always magic
        
```

<img width="1302" height="633" alt="image" src="https://github.com/user-attachments/assets/b04ddb24-74cc-4834-bd42-44362c144256" />
