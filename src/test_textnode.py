import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        node3 = TextNode("This is a text node", TextType.BOLD)
        node4 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node3, node4)
    def test_not_eq(self):
        node5 = TextNode("This is a text node", TextType.ITALIC)
        node6 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node5, node6)
        node7 = TextNode("This is a text node", TextType.BOLD)
        node8 = TextNode("This is a Text Node", TextType.BOLD)
        self.assertNotEqual(node7, node8)
        node9 = TextNode("This is a text node", TextType.BOLD)
        node10 = TextNode("This is a Text Node", TextType.BOLD, url='Not a real URL')
        self.assertNotEqual(node9, node10)
        
        


if __name__ == "__main__":
    unittest.main()