def visit(value):
    pass


class BinaryTree:
    """
    Class representing a binary tree with inorder, preorder, and postorder
    traversal methods.

    This class provides methods to perform inorder, preorder, and postorder
    traversal of a binary tree. It is initialized with a root node and can
    traverse its nodes by calling specific methods.

    :ivar root: The root node of the binary tree.
    :type root: Node
    """

    def __init__(self, root):
        self.root = root

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            visit(node.value)
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            visit(node.value)
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            visit(node.value)
