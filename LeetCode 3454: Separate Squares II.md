# 🟦 LeetCode 3454: Separate Squares II (Beginner Friendly)

## 1. The Core Idea
We have many squares on a graph. Some overlap. We need to find a **horizontal line (y)** that splits the combined area into two equal parts (top half and bottom half).

### The Challenge
If squares didn't overlap, we could just sum their areas. But because they **overlap**, we must calculate the **Union Area** (only counting overlapping parts once).

---

## 2. Step-by-Step Logic

### Step A: Identify Horizontal "Slices"
Imagine all squares are on a table. Every time a square starts (at its bottom `y`) or ends (at its top `y`), it creates a new "horizontal slice" or strip.
1. We collect every bottom $y$ and every top $y$.
2. We sort them from lowest to highest.
3. These are our **Events**.



### Step B: The "Smart Ruler" (Segment Tree)
As we move from one $y$-event to the next, we need to know: **"In this slice, what is the total width covered on the X-axis?"**
A **Segment Tree** is a special tool that handles this:
- **`cnt`**: Tracks how many squares currently cover a specific section.
- **`length`**: Calculates the actual union length. If one square covers $x=0$ to $x=10$ and another covers $x=5$ to $x=15$, the ruler knows the total length is **15**, not 20.

### Step C: Calculate Area Slices
For every strip between two $y$-coordinates:
- $Area = (y_{next} - y_{current}) \times \text{Union Width from Segment Tree}$
- We keep a running total of these areas.

### Step D: The Final Cut
Once we have the total area, we look for the exact $y$ where we hit 50%. We find the slice where the 50% mark falls and use a simple ratio to find the exact decimal coordinate:
- $HeightNeeded = \frac{MissingArea}{CurrentWidth}$

---

## 3. The Code

```python
class SegmentTree:
    def __init__(self, xs):
        self.xs = xs
        self.n = len(xs) - 1
        # 4*N is standard size for segment trees to avoid index errors
        self.cnt = [0] * (4 * self.n)
        self.length = [0.0] * (4 * self.n)

    def update(self, v, tl, tr, l, r, add):
        if l >= r: return
        # If the current node matches the range we want to update
        if l == tl and r == tr:
            self.cnt[v] += add
        else:
            # Otherwise, go deeper into the tree (split into left/right)
            tm = (tl + tr) // 2
            self.update(2 * v, tl, tm, l, min(r, tm), add)
            self.update(2 * v + 1, tm, tr, max(l, tm), r, add)
        
        # After updating, recalculate the length covered at this level
        if self.cnt[v] > 0:
            # If cnt > 0, this whole segment is fully covered
            self.length[v] = self.xs[tr] - self.xs[tl]
        else:
            # If cnt == 0, length is the sum of its children's lengths
            if tl + 1 < tr:
                self.length[v] = self.length[2 * v] + self.length[2 * v + 1]
            else:
                self.length[v] = 0

class Solution:
    def separateSquares(self, squares):
        # 1. Coordinate Compression: Collect all X boundaries
        x_coords = set()
        for x, y, l in squares:
            x_coords.add(x)
            x_coords.add(x + l)
        sorted_x = sorted(list(x_coords))
        x_map = {val: i for i, val in enumerate(sorted_x)}
        
        # 2. Sweep Line: Collect all Y boundaries (Events)
        events = []
        for x, y, l in squares:
            events.append((y, 1, x, x + l))     # Bottom edge (start)
            events.append((y + l, -1, x, x + l)) # Top edge (end)
        events.sort() # Process from ground up
        
        st = SegmentTree(sorted_x)
        total_area = 0.0
        y_areas = [] # Keep track of area accumulated in each slice
        
        # 3. Process each horizontal slice
        for i in range(len(events) - 1):
            y, type, x1, x2 = events[i]
            # Tell the Segment Tree a square started or ended
            st.update(1, 0, st.n, x_map[x1], x_map[x2], type)
            
            # The gap between this Y and the next Y event
            dy = events[i+1][0] - y
            if dy > 0:
                width = st.length[1] # Root of Segment Tree has total union width
                area_slice = dy * width
                total_area += area_slice
                # Store: start_y, end_y, width, total_area_so_far
                y_areas.append((y, events[i+1][0], width, total_area))
            
        # 4. Find the cut line
        target = total_area / 2
        for y_start, y_end, width, accum_area in y_areas:
            if accum_area >= target:
                # We reached the half-way point in this slice!
                # Calculate the area we had BEFORE this slice
                prev_area = accum_area - (y_end - y_start) * width
                needed = target - prev_area
                # Final Y = start of slice + (needed area / slice width)
                return y_start + (needed / width) if width > 0 else y_start
                
        return events[-1][0]
        ```
```
4. Why this works for "Hard" constraints
- Sorting: $O(N \log N)$
- Segment Tree Updates: $O(N \log N)$
- This is much faster than checking every square against every other square, which would be $O(N^2)$ and would fail.

---

PROOF:


<img width="1307" height="631" alt="image" src="https://github.com/user-attachments/assets/f6bb5d40-5744-4919-8e8f-3cffd47c0130" />
