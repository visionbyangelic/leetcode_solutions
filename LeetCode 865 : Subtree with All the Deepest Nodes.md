
````markdown
# LeetCode 865 : Subtree with All the Deepest Nodes

**Goal:** Find the smallest subtree containing all the deepest nodes in a binary tree using DFS.  

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return 0, None  # height, candidate node

            left_height, left_node = dfs(node.left)
            right_height, right_node = dfs(node.right)

            if left_height > right_height:
                return left_height + 1, left_node
            elif right_height > left_height:
                return right_height + 1, right_node
            else:
                return left_height + 1, node

        return dfs(root)[1]
````

**Notes:**

* DFS returns `(height, node)` for each subtree.
* Node with equal left/right subtree heights is the LCA of deepest nodes.
* Time Complexity: `O(n)`, Space Complexity: `O(h)` (recursion stack).

```
<img width="1316" height="688" alt="image" src="https://github.com/user-attachments/assets/1076bb68-cc94-46a4-8067-8ce746e642c6" />

