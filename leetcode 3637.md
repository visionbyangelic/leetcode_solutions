# 🟦 LeetCode 3637: Trionic Array I

## What Are We Doing?

Imagine you're hiking: you **go uphill**, then **go downhill**, then **go uphill again**.

A trionic array is the same idea with numbers:
- Numbers go **UP** ⬆️
- Then numbers go **DOWN** ⬇️  
- Then numbers go **UP** again ⬆️

**Example:**
```
[1, 3, 5, 4, 2, 6]
 ⬆️ ⬆️ ⬇️ ⬇️ ⬆️

1 → 3 → 5 (going up)
5 → 4 → 2 (going down)
2 → 6 (going up again)
✅ This is trionic!
```

## The Rules

1. You **MUST** have all 3 parts (up, down, up)
2. Each number must be **different** from the next (no repeats like 5, 5)
3. You can't skip any parts

## The Code
```python
class Solution:
    def isTrionic(self, nums: list[int]) -> bool:
        n = len(nums)
        i = 0
        
        # Step 1: Go uphill (numbers getting bigger)
        while i < n - 1 and nums[i] < nums[i + 1]:
            i += 1
        
        # Did we actually go uphill? If not, return False
        if i == 0:
            return False
        
        # Step 2: Go downhill (numbers getting smaller)
        start_of_downhill = i
        while i < n - 1 and nums[i] > nums[i + 1]:
            i += 1
        
        # Did we actually go downhill? If not, return False
        # Also, did we reach the end? If yes, no room for going up again!
        if i == start_of_downhill or i == n - 1:
            return False
        
        # Step 3: Go uphill again (numbers getting bigger)
        while i < n - 1 and nums[i] < nums[i + 1]:
            i += 1
        
        # Did we reach the very end of the array?
        return i == n - 1
```

## How It Works (Step by Step)

Let's use `[1, 3, 5, 4, 2, 6]`:

**Step 1: Go Uphill**
```
i = 0: Is 1 < 3? Yes! Move to i = 1
i = 1: Is 3 < 5? Yes! Move to i = 2
i = 2: Is 5 < 4? No! Stop here.

We moved! So uphill part exists ✅
```

**Step 2: Go Downhill**
```
i = 2: Is 5 > 4? Yes! Move to i = 3
i = 3: Is 4 > 2? Yes! Move to i = 4
i = 4: Is 2 > 6? No! Stop here.

We moved AND didn't reach the end! So downhill part exists ✅
```

**Step 3: Go Uphill Again**
```
i = 4: Is 2 < 6? Yes! Move to i = 5
i = 5: This is the last position!

We reached the end! ✅
```

**Answer: True!** We successfully went up, down, and up again.

## Why It Might Return False

**Example 1:** `[5, 4, 3, 2, 1]` (only going down)
```
Step 1: i stays at 0 (we never went up)
Return False immediately ❌
```

**Example 2:** `[1, 2, 3, 4, 5]` (only going up)
```
Step 1: Go up to i = 4
Step 2: Can't go down, i stays at 4
i == n-1, so return False ❌
```

**Example 3:** `[1, 3, 2]` (up, down, but no second up)
```
Step 1: Go up to i = 1
Step 2: Go down to i = 2
Step 3: i = 2 is already the last position (n-1)
We didn't go up again, return False ❌
```

## Practice Examples
```python
# Try these yourself!

[1, 5, 3, 7]
# 1→5 (up), 5→3 (down), 3→7 (up)
# Answer: True ✅

[2, 1, 3]
# 2→1 is down first, we need up first!
# Answer: False ❌

[1, 2, 3]
# Only going up
# Answer: False ❌

[3, 1, 2, 4, 6, 5, 8]
# 3→1 (down first, wrong!)
# Answer: False ❌

[1, 4, 2, 5]
# 1→4 (up), 4→2 (down), 2→5 (up)
# Answer: True ✅
```

## Key Takeaways

💡 **The pattern is always:** UP → DOWN → UP

💡 **We use one pointer** (`i`) that walks through the array

💡 **Each while loop** handles one phase of the journey

💡 **We check** if we actually moved in each phase

💡 **At the end**, we must reach the last position (`i == n - 1`)

That's it! You're checking if the numbers go uphill, downhill, then uphill again. 🏔️⛰️🏔️
