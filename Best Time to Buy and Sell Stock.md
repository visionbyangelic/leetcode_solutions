### 121 | Best Time to Buy and Sell Stock 📈 - Leetcode Day 4

**The Challenge:** You are given an array `prices` where `prices[i]` is the price of a given stock on the `i-th` day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

**💡 The "Aha!" Moment**

I first thought about checking every possible pair of buy and sell days (nested loops), but that would be too slow ($O(N^2)$). I realized I only need to keep track of the **lowest price I've seen so far**. As I move through the list, I just calculate "What if I sold today?" based on that minimum price.

**🛠️ My Strategy: The "Buy Low, Sell High" Walker**

* **Variables:** I tracked `min_price` (lowest price seen so far) and `max_profit`.
* **Logic:**
    1.  Iterate through the prices exactly once.
    2.  If the current price is **lower** than my `min_price`, I update `min_price`. (I found a better day to buy).
    3.  Otherwise, I calculate the profit if I sold today (`current_price - min_price`). If this is higher than my current `max_profit`, I update it.

---
**🐍 Python Implementation**

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit
```
---
📊 Performance Reflection

 Time Complexity: $O(N)$ — We iterate through the list of prices exactly once.
 
 Space Complexity: $O(1)$ — We only use two variables (```min_price``` and ```max_profit```) regardless of how long the list is.
 
 
 ---
 ✅ Proof of Acceptance :
 
 
<img width="1354" height="610" alt="image" src="https://github.com/user-attachments/assets/6f6911a3-d780-43e4-b6be-1656ce2c51d5" />


