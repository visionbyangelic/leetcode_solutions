1390 | Four Divisors 🔢 — Leetcode Day 10

### The Challenge: You are given an integer array nums. For each integer in the array, you need to find its divisors. 
If an integer has exactly four divisors, add the sum of those four divisors to your final answer. If it doesn't have exactly four, ignore it.
---
### 💡 The "Aha!" Moment
I realized that checking every number up to num to find its divisors would be incredibly slow (linear time). The "Aha!" moment was remembering that divisors always come in pairs. If $2$ is a divisor of $12$, then $12 / 2 = 6$ must also be a divisor. By only searching up to the square root of the number, I can find all divisors much faster.
---
🛠️ My Strategy: The "Square Root Pair" MethodData Structure: I used a set() to store divisors. This is brilliant because if a number is a perfect square (like 16, where $4 \times 4 = 16$), the set will automatically prevent the number 4 from being counted twice.

Mechanism:Efficiency: Loop from 1 to sqrt(num).The Duo: Every time I find a divisor i, I also add its partner num // i.
The Early Exit: If at any point my set has more than 4 items, I break the loop immediately. There's no point in finishing the math for a number that's already "disqualified.
"The Sum: If and only if the set length is exactly 4, I add the sum of that set to my total_sum.

🐍 Python Implementation
```
class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = 0
        
        for num in nums:
            divisors = set()
            # Check divisors up to the square root to find pairs
            for i in range(1, int(num**0.5) + 1):
                if num % i == 0:
                    divisors.add(i)
                    divisors.add(num // i)
                
                # Optimization: Stop early if we exceed 4 divisors
                if len(divisors) > 4:
                    break
            
            # Only sum if the number has exactly 4 divisors
            if len(divisors) == 4:
                total_sum += sum(divisors)
                
        return total_sum
 ```

📊 Performance ReflectionTime Complexity: $O(N \cdot \sqrt{M})$ — where $N$ is the number of integers and $M$ is the value of the largest integer.
This is the gold standard for divisor problems.
Space Complexity: $O(1)$ — Since we only ever store a maximum of 5 divisors at a time, the memory usage is constant regardless of how big the input is.

✅ Proof of Acceptance: Successfully handled the constraints by using the square root property to optimize the search.

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/6dce3feb-51eb-4445-83b2-034cbd14ac1c" />
