import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(tag=None, value=None, children=None, props=None)
        node2 = HTMLNode()
        self.assertEqual(node, node2)
        node3 = HTMLNode(tag='asd', value='12', children='fe', props={'href':'some stuff','attr':'other stuff'})
        node4 = HTMLNode(tag='asd', value='12', children='fe', props={'href':'some stuff','attr':'other stuff'})
        self.assertEqual(node3.props_to_html(), ' href="some stuff" attr="other stuff"')
        self.assertEqual(node3, node4)
    def test_not_eq(self):
        node = HTMLNode(tag=None, value=None, children=None, props=None)
        node2 = HTMLNode(tag = 'a')
        self.assertNotEqual(node, node2)
        node = HTMLNode(children = 'fgh', tag = 'a')
        node2 = HTMLNode(tag = 'a')
        self.assertNotEqual(node, node2)
    def test_not_implemented(self):
        node = HTMLNode(children = 'fgh', tag = 'a')
        self.assertRaises(NotImplementedError,node.to_html)

if __name__ == "__main__":
    unittest.main()