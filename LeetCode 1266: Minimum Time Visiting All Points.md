

## LeetCode 1266: Minimum Time Visiting All Points

###  The Problem Description

On a 2D plane, you are given a sequence of points. You need to visit them in the exact order they appear in the list. The goal is to find the **minimum time** (in seconds) to complete the trip.

**The Movement Rules:**

* **Vertical/Horizontal:** 1 unit = 1 second.
* **Diagonal:** 1 unit diagonally (covering both 1 unit of  and 1 unit of  at once) = 1 second.

---

### The "Aha!" Moment: The Geometry

To understand the solution, you have to realize that moving diagonally is "efficient." If you need to move 3 units right and 4 units up:

1. You can move **diagonally** for 3 seconds. This gets you 3 units right and 3 units up.
2. Now you are only 1 unit away from your destination (you still need to go 1 unit up).
3. You move **vertically** for 1 more second.
4. **Total time:**  seconds.

Notice that **4 seconds** is simply the **maximum** of the two distances ( and ). This is the secret to the problem: the time taken to travel between two points is always the maximum of the horizontal and vertical differences.

---

###  Step-by-Step Logic

1. **Start at the beginning:** We start at the first point in the list.
2. **Calculate the "Gaps":** For every next point, we calculate how far away it is in terms of  (left/right) and  (up/down).
3. **Find the Maximum:** We take the absolute value (to ensure the distance is positive) and find which gap is larger.
4. **Keep Score:** Add that maximum value to a running total.

---

###  The Code Solution

```python
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # 1. Initialize our total time counter
        total_time = 0
        
        # 2. Loop through the points, starting from the second one (index 1)
        # We compare the current point 'i' with the previous point 'i-1'
        for i in range(1, len(points)):
            
            # Find the horizontal distance (x-axis)
            x_distance = abs(points[i][0] - points[i-1][0])
            
            # Find the vertical distance (y-axis)
            y_distance = abs(points[i][1] - points[i-1][1])
            
            # The time to travel is the maximum of the two distances
            total_time += max(x_distance, y_distance)
            
        # 3. Return the final accumulated time
        return total_time

```

---

### Why this is efficient (Analysis)

* **Time Complexity:** . We only visit each point in the list exactly once. Whether the list has 10 points or 1,000, the logic remains fast and linear.
* **Space Complexity:** . We aren't creating any new lists or complex data structures; we are just using one variable (`total_time`) to store an integer.

---

###  Beginner Glossary

* **`abs()`**: Stands for *Absolute Value*. It turns negative numbers into positive ones (e.g., `abs(-5)` becomes `5`). This is vital because distance cannot be negative.
* **`max()`**: A function that compares two or more numbers and gives you the largest one.
* **`range(1, len(points))`**: This tells the code to start at the second item (index 1) and go to the end. We do this because you can't calculate the distance to the "previous" point if you start at the very first one!



<img width="1310" height="637" alt="image" src="https://github.com/user-attachments/assets/85180ed1-3d5b-4234-9d01-46137e7c7c9d" />
