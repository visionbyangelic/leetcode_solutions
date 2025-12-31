### 169 | Majority Element 🗳️ - Leetcode Day 5

**The Challenge:** Given an array `nums` of size `n`, return the majority element. The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

**💡 The "Aha!" Moment**

I realized that just finding the "most frequent" number isn't enough; I needed to verify strictly that it holds more than half the "votes." This meant I couldn't just scan the list once; I needed to build a full count of every number first, and then run a second check to see who won the election.

**🛠️ My Strategy: The "Ballot Box" Inventory**

* **Data Structure:** I used a **Hash Map** (Dictionary) to act as my ballot box.
* **Mechanism:**
    1.  **Count Votes:** I iterated through the list, adding each number to the dictionary. If it was new, I started its count at 1. If it was already there, I incremented it.
    2.  **Declare Winner:** Once the counting was done, I looped through my dictionary to find the number whose count was greater than `n // 2`.

---
**🐍 Python Implementation**

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numcount = {}
        
        # 1. Build the inventory (Count the votes)
        for i in nums:
            if i in numcount:
                numcount[i] += 1
            else:
                numcount[i] = 1
        
        # 2. Check for the winner (After counting is done)
        for number, count in numcount.items():
            if count > len(nums) // 2:
                return number
```
---
📊 Performance Reflection

- Time Complexity: $O(N)$ — We iterate through the list once to count, and then through the dictionary once to check values.
- Space Complexity: $O(N)$ — In the worst case (where every number is unique), our dictionary would store $N$ distinct entries.
 
 ---
 ✅ Proof of Acceptance :
 
<img width="1324" height="676" alt="image" src="https://gist.github.com/user-attachments/assets/8c628fb3-37b8-46cd-8582-4b8e05dfdffc" />
