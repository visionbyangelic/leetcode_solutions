### 231 |  Power of Two 🔢 - Leetcode Day 9

**The Challenge:** Given an integer n, return true if it is a power of two. Otherwise, return false. An integer n is a power of two if there exists an integer x such that $n = 2^x$.💡

**💡 The "Aha!" Moment**

The "Aha!" MomentI realized that if a number is a power of two, it is essentially "pure" in its factors—it should contain nothing but 2s. If I repeatedly "strip away" those 2s by dividing, a true power of two will eventually be whittled down to exactly 1. If I hit any other odd number during the process, I know it's an impostor!🛠️

**🛠️ My Strategy: The "Repeated Division" Method

* **Data Structure:** Basic Integer (No extra storage required).
* **Mechanism:**
    1. **Positive Guard**: Powers of two ($2^0, 2^1, ...$) are always positive. If $n \le 0$, it's an immediate False.
    2. **🛡️The Whittle Down:** Use a while loop to check if the number is even (n % 2 == 0). As long as it is, keep dividing by 2.
    3. **✂️The Final Verdict:** Once the loop ends (meaning the number is now odd), check if it equals
    
 ---
**🐍 Python Implementation**

```python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
 
# 1. Base Case: Powers of two are always positive
        if n <= 0:
            return False
        
        # 2. Keep dividing by 2 as long as the remainder is 0
        while n % 2 == 0:
            n //= 2  # Integer division to keep it clean
            
        # 3. If we reached 1, it's a power of two!
        return n == 1
```
---
📊 Performance Reflection

- Time Complexity: $O(\log N)$ — We reduce the input by half in every iteration of the loop.
- Space Complexity: $O(1)$ — No extra memory is used, just the input variable itself.✅ Proof of Acceptance :
 ---
 ✅ Proof of Acceptance :
 
<img width="1354" height="734" alt="image" src="https://github.com/user-attachments/assets/135da8ab-5d90-4252-aa91-0977de080b73" />




