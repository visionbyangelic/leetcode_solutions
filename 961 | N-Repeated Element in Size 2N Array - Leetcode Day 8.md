### 961 | N-Repeated Element in Size 2N Array 🎯 - Leetcode Day 8

**The Challenge:** In an array of $2n$ elements, there are $n+1$ unique elements. One specific element is repeated exactly $n$ times. Find and return that element.

**💡 The "Aha!" Moment**

I realized I didn't need to count all the way up to $n$ or use any complex math. The constraints tell us that only one number in the entire list repeats at all—every other number appears exactly once. This means the very first time I see a number for the second time, it must be the target. It's a race to find the first duplicate! 

**🛠️ My Strategy: The "First to Two" Race

* **Data Structure:** I used a Set to act as my "memory bank." 🧠
* **Mechanism:**
    1. **Iterate:** Walk through the list nums one by one.
    2. **Check Memory:** For each number, check if it's already in the seen set.
    3. **Return:** If it is in the set, I've found my answer. Return it immediately. 🏁
    4. **Record:** If not, add it to the set and keep moving.
 ---
**🐍 Python Implementation**

```python
class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        # 1. Create a set to store numbers we've encountered
        seen = set()
        
        # 2. Loop through the array
        for num in nums:
            # 3. If we see a number again, it's the n-repeated one
            if num in seen:
                return num
            
            # 4. Otherwise, add it to our memory
            seen.add(num)
            
        return -1 # Fallback, though constraints say a repeat always exists
```
---
📊 Performance Reflection

- Time Complexity: $O(N)$ — In the worst case, we check slightly more than half the array.
- Space Complexity: $O(N)$ — We store unique elements in the set until a duplicate is found.
 ---
 ✅ Proof of Acceptance :
 
 <img width="1359" height="736" alt="image" src="https://gist.github.com/user-attachments/assets/e07c6484-6d0f-4037-bec8-7bc8c6f8ae52" />
