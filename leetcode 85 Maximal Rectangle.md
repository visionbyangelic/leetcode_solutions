# Gist: Solving Maximal Rectangle (LeetCode 85)

## 1. The Core Insight
You cannot solve this by simply counting the total number of $1\text{s}$. Instead, treat each row of the matrix as the base of a **Histogram**. 

* **Row 0** is your first histogram.
* **Row 1** is a new histogram where bars "stack" on top of Row 0 (only where there's a $1$).
* **Row 2** stacks on Row 1, and so on.



---

## 2. The Implementation

This approach uses a **Monotonic Stack** to solve the "Largest Rectangle in Histogram" problem for every row in $O(M)$ time.

```python
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        cols = len(matrix[0])
        # We add an extra 0 at the end as a 'sentinel' to flush the stack
        heights = [0] * (cols + 1)
        max_area = 0
        
        for row in matrix:
            # Step 1: Update heights for the current row
            for i in range(cols):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            
            # Step 2: Monotonic Stack logic for the current histogram
            stack = [-1] # Start with -1 to make width calculation easier
            for i in range(cols + 1):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)
                
        return max_area
```

---
## 3. Step-by-Step Logic

### Phase A: Building the Histogram (Row by Row)
Maintain an array called `heights` of size `columns`. As you iterate through each row:
* If `matrix[row][col] == '1'`, `heights[col] += 1`.
* If `matrix[row][col] == '0'`, `heights[col] = 0`. (The vertical chain is broken).

### Phase B: Finding the Largest Rectangle in the Histogram
For every row, take that `heights` array and find the largest rectangle. We use a **Monotonic Stack** to do this in $O(M)$ time.

1.  **The Stack Rule:** Keep indices of heights in the stack such that the heights are always **increasing**.
2.  **When a height decreases:** It means the taller bar in the stack can no longer extend to the right. 
3.  **Calculate Area:** * `Height` = height of the popped index.
    * `Width` = current index - index of the new stack top - 1.
    * `Area` = Height × Width.


---
## 4. Visual Representation
Matrix:
1 0 1
1 1 1

Row 0 Histogram: [1, 0, 1] -> Max Area = 1
Row 1 Histogram: [2, 1, 2] -> Max Area = 3 (The middle '1' supports a 1x3 rectangle)


---
## 5. Complexity
* **Time:** $O(R \times C)$ — We touch every cell a constant number of times.
* **Space:** $O(C)$ — We only store the heights for one row at a time.

