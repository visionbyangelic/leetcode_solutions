# 1339. Maximum Product of Splitted Binary Tree

# question:
Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.

---

# Intuition
To maximize the product of two subtrees, we need to split the tree such that the sums of the two resulting parts are as balanced as possible. Mathematically, for a fixed total sum $S$, the product $x \cdot (S - x)$ is at its maximum when $x$ is closest to $S/2$.

# Approach
1. Subtree Sums: Use a Depth-First Search (DFS) to calculate the sum of every possible subtree in the binary tree.
2. Storage: During the DFS, append each calculated subtree sum to a list (all_sums).
3. Total Sum: The sum returned by the initial call to the root is the total_sum of the entire tree.
3. Maximize Product: Iterate through all values in all_sums. 
4. For each subtree sum $s$, calculate the product of the two resulting trees: $s \cdot (\text{total\_sum} - s)$.
5. Modulo: Keep track of the maximum product and return it modulo $10^9 + 7$.

# Complexity
- Time complexity: $O(n)$We traverse the tree once to find all subtree sums ($O(n)$) and then iterate through the list of sums once ($O(n)$).
- Space complexity:$O(n)$We store $n$ sums in a list and the recursion stack can go up to $O(n)$ in the case of a skewed tree.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # Step 1: Create a list to store every subtree sum we find
        all_sums = []

        # Step 2: Define a DFS to calculate sums and populate our list
        def calculate_sums(node):
            if not node:
                return 0
            
            # Subtree sum = current value + left child sum + right child sum
            current_sum = node.val + calculate_sums(node.left) + calculate_sums(node.right)
            all_sums.append(current_sum)
            return current_sum

        # The result of the root call is the total sum of the entire tree
        total_sum = calculate_sums(root)
        
        # Step 3: Iterate through all recorded sums to find the max product
        max_product = 0
        for s in all_sums:
            # The product is (sum of one part) * (total - sum of that part)
            product = s * (total_sum - s)
            if product > max_product:
                max_product = product
        
        # Step 4: Return result modulo 10^9 + 7
        return max_product % (10**9 + 7)
```

<img width="1364" height="677" alt="image" src="https://github.com/user-attachments/assets/4e5201f0-88fe-4376-8b3f-355d0212fb47" />
