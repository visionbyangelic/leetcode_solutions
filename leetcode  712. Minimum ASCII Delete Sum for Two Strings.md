

# 712. Minimum ASCII Delete Sum for Two Strings 🧩

### 📊 Performance Summary
- **Status:** Accepted (93/93 testcases)
- **Runtime:** 147 ms (Beats 99.70%)
- **Memory:** 20.39 MB (Beats 72.97%)
- **Date:** Jan 10, 2026

---

### 💡 The Mindset: Maximize the "Keepers"
Instead of directly calculating which characters to delete, we calculate the **Maximum ASCII Sum** of characters that can be kept (The Longest Common Subsequence).

1. **Total ASCII:** Sum every character in both `s1` and `s2`.
2. **DP Logic:** Use a 2D grid to find the highest value shared between the strings.
3. **The Result:** Since the shared characters exist in both strings, we subtract their value twice (`2 * dp[0][0]`) from the total. What remains is the minimum cost of deletions.

---

### 💻 Implementation

```python
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # m and n represent the lengths of our two strings
        m, n = len(s1), len(s2)
        
        # Initialize a 2D DP table with an extra row and column for empty string cases
        # dp[i][j] represents the max ASCII sum we can keep using suffixes s1[i:] and s2[j:]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Iterate backwards through both strings (Bottom-Up DP)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # CASE 1: The characters match
                if s1[i] == s2[j]:
                    # We 'keep' this character. Its value is added to the 
                    # best result from the remaining suffixes (diagonal move).
                    dp[i][j] = ord(s1[i]) + dp[i + 1][j + 1]
                else:
                    # CASE 2: The characters do NOT match
                    # We must choose the better path:
                    # - Skip s1[i] and see the max we can get (dp[i + 1][j])
                    # - Skip s2[j] and see the max we can get (dp[i][j + 1])
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        # Step 1: Calculate the total ASCII sum of both strings combined
        total_ascii = sum(ord(c) for c in s1) + sum(ord(c) for c in s2)
        
        # Step 2: Subtract twice the max shared ASCII sum from the total
        # We subtract twice because the 'kept' characters were counted in both strings.
        return total_ascii - 2 * dp[0][0]

```

---

### 🏗️ Why it Works

* **Matching:** When `s1[i] == s2[j]`, we use the diagonal `dp[i+1][j+1]` because those two characters are now "paired up" and cannot be used again.
* **Mismatching:** We take the `max()` of the bottom and right cells because we want to preserve the path that keeps the most ASCII value.


---
proof:
<img width="1312" height="632" alt="image" src="https://github.com/user-attachments/assets/980bc634-c9f3-48d0-b089-7f24f393a33b" />
