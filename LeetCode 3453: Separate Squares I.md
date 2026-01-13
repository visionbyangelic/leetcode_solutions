 ## LeetCode 3453: Separate Squares I

### 1. The Visual Concept

Imagine you have several squares of various sizes sitting on a table. Some are tall, some are short, and some overlap. You need to find a height (a horizontal "cut") where the total area of the plastic below the cut is exactly equal to the area above.

---

### 2. Why "Binary Search on Answer" is the Best Tool

Usually, we search through lists of numbers. Here, we are searching through a **continuous range of heights** (-coordinates).

* **The Problem:** If we move our line up by 0.00001, the area changes. There are infinite possible heights.
* **The Solution:** Binary Search. Instead of checking every height, we "bracket" the answer. We check the middle, see if the area is too big or too small, and throw away the wrong half.

**Wait, what about the Runtime?**
The reason the "brute force" version is slow is that it performs math operations inside the search loop that could be done once at the beginning.

---

### 3. The "High-Performance" Logic

To make the code faster and use less memory, we use these three optimizations:

1. **Coordinate Stripping:** The -coordinate (left/right position) does not affect the area of a horizontal cut. We ignore it entirely to save memory.
2. **Pre-Calculation:** Instead of calculating `y + side` (the top of the square) thousands of times inside the search, we calculate it once at the start.
3. **The "Sweet Spot" Iteration:** 100 iterations is safe, but 80 iterations provides the exact same result on LeetCode while being 20% faster.

---

### 4. The Optimized Code (Python 3)

```python
class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:
        # Step 1: Pre-process data (Memory Optimization)
        # We strip 'x' and pre-calculate the 'top' of each square
        refined_data = []
        total_area = 0
        min_y = float('inf')
        max_y = float('-inf')
        
        for _, y, side in squares:
            top = y + side
            refined_data.append((y, top, side))
            total_area += side * side
            
            # Track the absolute bottom and top of all squares
            if y < min_y: min_y = y
            if top > max_y: max_y = top
            
        target_half = total_area / 2.0
        low, high = min_y, max_y
        
        # Step 2: Precision Binary Search (Runtime Optimization)
        # 80 iterations reaches 10^-7 precision, exceeding requirements
        for _ in range(80):
            mid = (low + high) / 2.0
            area_below = 0
            
            for y, top, side in refined_data:
                if top <= mid:
                    # Square is fully below the line
                    area_below += side * side
                elif y < mid:
                    # Line cuts through the square (Rectangle Area = Width * Height)
                    # Width = side, Height = mid - y
                    area_below += side * (mid - y)
            
            # Step 3: Narrow the range
            if area_below < target_half:
                low = mid
            else:
                high = mid
                
        return low

```

---

### 5. Step-by-Step Execution for Beginners

Let's say we have one square at  with  (Total Area = 4, Target = 2).

1. **Initial Boundaries:** `low = 0`, `high = 2`.
2. **First Guess:** `mid = 1.0`.
3. **Check Area Below:** The square starts at 0 and ends at 2. Our line is at 1. The part below is a rectangle of .
4. **Comparison:** 2 is our target! The binary search will continue to narrow down, but it will stay centered around 1.0.
5. **Final Answer:** `1.0`.

---

<img width="1309" height="639" alt="image" src="https://github.com/user-attachments/assets/a5358f0c-c58c-4eae-b6cf-361814688f66" />


---
