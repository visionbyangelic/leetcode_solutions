# 🟦 LeetCode 1200: Minimum Absolute Difference

### 1. The Core Idea 💡
The objective is to find all pairs of elements in an array that have the smallest possible absolute difference. 

Because we want the "closest" numbers, the most efficient strategy is to **sort** the array. Once sorted, the numbers with the smallest differences are guaranteed to be immediate neighbors. This changes the problem from comparing every possible pair ($O(n^2)$) to just comparing adjacent neighbors ($O(n)$).

---

### 2. Solution Strategy 🛠️

**Step 1: Sorting**
We sort the array in ascending order. This groups similar values together.

**Step 2: Find the Minimum Gap**
We iterate through the sorted array once to find the smallest gap between any two adjacent elements ($arr[i+1] - arr[i]$). This value is our "target" difference.

**Step 3: Collect the Pairs**
We iterate through the sorted array a second time. Any pair that matches our target difference is added to our result list. Because we traverse from left to right, the pairs are naturally collected in ascending order.

---

### 3. The Code 💻

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # 1. Sort the array to bring closest values together
        arr.sort()
        
        # 2. Find the minimum absolute difference between neighbors
        # We look at every pair (i, i+1) and find the smallest gap
        min_diff = min(arr[i+1] - arr[i] for i in range(len(arr) - 1))
        
        # 3. Identify and collect all pairs that match the min_diff
        result = []
        for i in range(len(arr) - 1):
            if arr[i+1] - arr[i] == min_diff:
                # Add the pair in [a, b] format where a < b
                result.append([arr[i], arr[i+1]])
                
        return result

---

### 4. Line-by-Line Beginner Breakdown 🔍

* **arr.sort():** This organizes the input. In an unsorted array, `1` and `2` could be miles apart; now they are neighbors.
* **min(... for i in range(len(arr) - 1)):** The `range` stops at the second-to-last element so that `i+1` never goes out of bounds.
* **min_diff:** This variable holds the "world record" for the smallest gap found in this specific array.
* **result.append([arr[i], arr[i+1]]):** Since the array is sorted, `arr[i]` is always smaller than `arr[i+1]`, satisfying the requirement $a < b$.

---

### 5. Complexity Analysis 📊

* **Time Complexity: $O(n \log n)$**
  The sorting step takes $O(n \log n)$. Finding the minimum and collecting pairs both take $O(n)$. Since $n \log n$ is larger, it dominates the total time.
* **Space Complexity: $O(n)$**
  We need space to store the list of pairs we return. The sorting process itself also typically uses $O(\log n)$ or $O(n)$ extra space depending on the language.
  
  ---
<img width="1361" height="763" alt="image" src="https://github.com/user-attachments/assets/193eb8cf-ed30-4a08-a09b-6e3193301b36" />
