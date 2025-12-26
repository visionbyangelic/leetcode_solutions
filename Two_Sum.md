# 001 | Two Sum 🎯

> **The Challenge:** Find two numbers in a list that add up to a specific target.

---

### 💡 The "Aha!" Moment
Initially, I thought about checking every single pair (which is slow). Then I realized: if I'm looking at a number like `7` and the target is `10`, I am essentially **hunting for a `3`**. Instead of looking forward, I can keep a "memory" of what I've already seen to find that `3` instantly.

### 🛠️ My Strategy: The "Memory" Map
- **Data Structure:** I used a Python Dictionary (`{}`).
- **Mechanism:** As I iterate, I calculate `complement = target - current_number`.
- **Logic:** If the `complement` is in my "memory," I'm done! If not, I "remember" the current number and move on.

### 🐍 Python Implementation

```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # 'seen' stores { value: index }
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in seen:
                return [seen[complement], i]
            
            # Store current number for future lookups
            seen[num] = i 
 ```
 
 📊 Performance Reflection
 
 - Time Complexity: $O(n)$ — We only loop through the list once.
 - Space Complexity: $O(n)$ — We store up to $n$ elements in the dictionary.
 
 
 ✅ Proof of Acceptance 
            
 <img width="1334" height="666" alt="image" src="https://github.com/user-attachments/assets/4ee96cc7-1652-4e31-add9-5124a0d6485a" />

 
