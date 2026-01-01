### 1935 | Maximum Number of Words You Can Type ⌨️ - Leetcode Day 7

**The Challenge:** You are given a string text of words and a string ```brokenLetters```. You need to count how many words in the text can be fully typed using a keyboard where the brokenLetters do not work.

**💡 The "Aha!" Moment**

I realized that a word is only "typeable" if none of its letters are in the broken set. Instead of checking every letter of every word, I can assume a word is good and "disqualify" it the moment I hit a single broken key. This "guilty until proven innocent" logic for the letters makes the code much faster. 

**🛠️ My Strategy: The "Filter & Flag" Method

* **Data Structure:** I used a List of strings (created by .split()) to isolate each word.
* **Mechanism:**
    1.  **Isolation:** Use .split() to turn the long sentence into individual words.
    2.  **The Integrity Check:** For every word, I set a flag can_type to True. I then loop through the brokenLetters
    3.  **The Shortcut:** If a letter from brokenLetters is found in the word, I flip the flag to False and break the loop immediately. There's no point checking the rest of the letters if the word is already broken!
    4.  **The Tally:** if the flag remains True, it means the word is safe to type, so I increment my count.
 ---
**🐍 Python Implementation**

```python
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()  #  Split the sentence into individual words
        count = 0             #  Counter for words we can type
        
        for word in words:    #  Loop through each word in the list
            can_type = True   #  Flag to track if the word is typable
            
            for letter in brokenLetters: #  Check each broken letter
                if letter in word:       #  If a broken letter is found...
                    can_type = False     #  Flip the flag to False
                    break                #  Stop checking this word early
            
            if can_type:      #  If the flag is still True, we can type it!
                count += 1    #  Add 1 to our successful count
                
        return count
```
---
📊 Performance Reflection

- Time Complexity: $O(N \cdot M)$ — where $N$ is the number of words and $M$ is the number of broken letters.
- Space Complexity: $O(N)$ — The split() function creates a new list of words, which takes up space proportional to the input text.
 ---
 ✅ Proof of Acceptance :
 
<img width="1358" height="704" alt="image" src="https://github.com/user-attachments/assets/8d81d86b-4bb6-4023-b49c-7abb18d1342f" />
