import unittest

from pva4.BreadthFirstTraverser import BreadthFirstTraverser
from pva4.DepthFirstTraverser import DepthFirstTraverser
from pva4.DepthFirstTraverserStack import DepthFirstTraverserStack
from pva4.TreeIterator import TreeIterator
from pva4.TreeNode import TreeNode


class TestTraverser(unittest.TestCase):
    def setUp(self):
        nodeA = TreeNode("A")
        nodeA.children.append(nodeA1 := TreeNode("A1"))
        nodeA.children.append(nodeA2 := TreeNode("A2"))
        nodeA1.children.append(nodeA11 := TreeNode("A11"))
        nodeA1.children.append(nodeA12 := TreeNode("A12"))
        nodeA2.children.append(nodeA21 := TreeNode("A21"))
        nodeA2.children.append(nodeA22 := TreeNode("A22"))
        self.tree = nodeA

    def test_recursive_traverser(self):
        list_pre = []
        list_post = []

        class DepthFirstTraverserImpl(DepthFirstTraverser):
            def pre_visit_node(self, value):
                list_pre.append(value)

            def post_visit_node(self, value):
                list_post.append(value.lower())

        trav = DepthFirstTraverserImpl()
        trav.traverse(self.tree)

        list_pre_exp  = ["A",   "A1",  "A11", "A12", "A2",  "A21", "A22"]
        list_post_exp = ["a11", "a12", "a1",  "a21", "a22", "a2",  "a"]

        self.assertEqual(list_pre, list_pre_exp)
        self.assertEqual(list_post, list_post_exp)

    def test_depth_first_traverser_stack(self):
        list_pre = []

        class DepthFirstTraverserStackImpl(DepthFirstTraverserStack):
            def pre_visit_node(self, value):
                list_pre.append(value)

        trav = DepthFirstTraverserStackImpl()
        trav.traverse(self.tree)

        list_pre_exp = ["A", "A1", "A11", "A12", "A2", "A21", "A22"]

        self.assertEqual(list_pre, list_pre_exp)

    def test_breadth_first_traverser(self):
        list_pre = []

        class BreadthFirstTraverserImpl(BreadthFirstTraverser):
            def pre_visit_node(self, value):
                list_pre.append(value)

        trav = BreadthFirstTraverserImpl()
        trav.traverse(self.tree)

        list_pre_exp = ["A", "A1", "A2", "A11", "A12", "A21", "A22"]

        self.assertEqual(list_pre, list_pre_exp)

    def test_tree_iterator_class(self):
        it = TreeIterator(self.tree)
        self.perform_iterator_tests(it)

    def test_tree_iterator_generator(self):
        it = traverse_tree(self.tree)
        self.perform_iterator_tests(it)

    def perform_iterator_tests(self, it):
        self.assertEqual(next(it), "A")
        self.assertEqual(next(it), "A1")
        self.assertEqual(next(it), "A11")
        self.assertEqual(next(it), "A12")
        self.assertEqual(next(it), "A2")
        self.assertEqual(next(it), "A21")
        self.assertEqual(next(it), "A22")
        with self.assertRaises(StopIteration):
            next(it)


if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
