### 242 | Valid Anagram 🔄 - Leetcode Day 3

**The Challenge:** Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise. (An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.)

**💡 The "Aha!" Moment**

I initially thought about just checking if every letter in `s` existed in `t`. But I realized that fails for words with duplicate letters (like "Apple" vs "Pale"). Just knowing a letter *exists* isn't enough; I needed to know *how many times* it appears. I needed a full inventory, not just a guest list.

**🛠️ My Strategy: The "Inventory Check"**

* **Data Structure:** I used two **Hash Maps** (Dictionaries) to store character counts.
* **Mechanism:** I treated the dictionaries like inventory receipts.
* **Logic:**
    1.  **Fail Fast:** If the strings have different lengths, they can't be anagrams. Return `False`.
    2.  **Count:** Loop through each string and count how many times each letter appears.
    3.  **Compare:** Check if the "inventory receipt" for `s` is identical to `t`.
---
**🐍 Python Implementation**

```
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # 1. Fail Fast: Different lengths? Not anagrams.
        if len(s) != len(t):
            return False

        # create dictionary to store count
        countS = {}
        countT = {}

        # search
        for letter in s:
            if letter in countS:
                countS[letter] += 1 
            else:
                countS[letter] = 1
                
        for letter in t:
            if letter in countT:
                countT[letter] += 1
            else:
                countT[letter] = 1

        # Check if the dictionaries are identical
        return countS == countT
```
---
📊 Performance Reflection

 Time Complexity: $O(N)$ — We iterate through the strings exactly once to build the counts.
 
 Space Complexity: $O(1)$ — Although we use a dictionary, the English alphabet has a fixed size (26 letters). Our dictionary will never grow larger than 26 keys, regardless of how long the input string is.
 
 
 ---
 ✅ Proof of Acceptance :
 <img width="1345" height="722" alt="image" src="https://github.com/user-attachments/assets/fc9c5bc8-d350-4ce0-b957-352b888209ed" />




github gist; https://gist.github.com/visionbyangelic/63564a5f4d04b31461332d58e6d1b07e
