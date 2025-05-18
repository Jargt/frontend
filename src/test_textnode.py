import unittest
from textnode import TextNode, TextType, text_node_to_html_node

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
        
class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.props, None)

    def test_text_bold(self):
        node = TextNode("This is bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, "This is bold text")
        self.assertEqual(html_node.props, None)

    def test_text_italic(self):
        node = TextNode("This is italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'i')
        self.assertEqual(html_node.value, "This is italic text")
        self.assertEqual(html_node.props, None)

    def test_text_code(self):
        node = TextNode("This is code text", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'code')
        self.assertEqual(html_node.value, "This is code text")
        self.assertEqual(html_node.props, None)

    def test_text_link(self):
        node = TextNode("This is a link", TextType.LINK, 'https://www.boot.dev/lessons')
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.value, "This is a link")
        self.assertEqual(html_node.props, {'href':'https://www.boot.dev/lessons'})

    def test_text_image(self):
        node = TextNode('This is an image', TextType.IMAGE, 'https://www.boot.dev/lessons')
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'img')
        self.assertEqual(html_node.value, None)
        self.assertEqual(html_node.props, {'src':'https://www.boot.dev/lessons', 'alt':'This is an image'})

    def test_not_text_type(self):
        with self.assertRaises(ValueError):
            node = TextNode('some text', 'link',)
            html_node = text_node_to_html_node(node)

if __name__ == "__main__":
    unittest.main()