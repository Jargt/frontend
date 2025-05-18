import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):

#Tests for HTMLNode

    def test_eq_html(self):
        node = HTMLNode(tag=None, value=None, children=None, props=None)
        node2 = HTMLNode()
        self.assertEqual(node, node2)
        node3 = HTMLNode(tag='asd', value='12', children='fe', props={'href':'some stuff','attr':'other stuff'})
        node4 = HTMLNode(tag='asd', value='12', children='fe', props={'href':'some stuff','attr':'other stuff'})
        self.assertEqual(node3.props_to_html(), ' href="some stuff" attr="other stuff"')
        self.assertEqual(node3, node4)
    def test_not_eq_html(self):
        node = HTMLNode(tag=None, value=None, children=None, props=None)
        node2 = HTMLNode(tag = 'a')
        self.assertNotEqual(node, node2)
        node = HTMLNode(children = 'fgh', tag = 'a')
        node2 = HTMLNode(tag = 'a')
        self.assertNotEqual(node, node2)
    def test_not_implemented(self):
        node = HTMLNode(children = 'fgh', tag = 'a')
        self.assertRaises(NotImplementedError,node.to_html)

#Tests for LeafNode

    def test_eq_leaf(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_variation(self):
        node1 = LeafNode(value='12', tag='asd')
        node2 = LeafNode('asd', '12')
        self.assertEqual(node1, node2)
    def test_no_tags(self):
        node = LeafNode(None, 'no tags baby!')
        self.assertEqual(node.to_html(), 'no tags baby!')
    def test_no_assign(self):
        self.assertEqual(LeafNode('p','my text').to_html(),'<p>my text</p>')
    def test_not_eq_leaf(self):
        node1 = LeafNode(value='11', tag='asd')
        node2 = LeafNode('asd', '12')
        self.assertNotEqual(node1, node2)
    def test_no_value_exception(self):
        with self.assertRaises(ValueError):
            node = LeafNode("a", None)
    def test_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com", "attr": "more"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" attr="more">Click me!</a>')

if __name__ == "__main__":
    unittest.main()