# 循环实现二叉树的前序遍历
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution1:
    def preorderraversal(self, root):
        ret, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                # 注意压入栈的顺序,先压入右节点，再压入左节点
                stack.append(node.right)
                stack.append(node.left)
            return ret


# 循环实现二叉树的中序遍历


class Solution2(object):
    def inorderraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret,stack=[],[]
        while stack or root:
            if root:
                stack.append(root)
                root=root.left
            else:
                root = stack.pop()
                ret.append(root.val)
                root = root.right
        return ret


# 循环实现二叉树的后序遍历


class Solution3:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret, stack = [], []
        while root or stack:
            if root:
                stack.append(root)
                ret.insert(0, root.val)
                root = root.right
            else:
                node = stack.pop()
                root = node.left
        return ret


# 递归实现二叉树的前序遍历


class Solution4(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        return [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right)