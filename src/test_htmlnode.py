import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
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

class TestLeafNode(unittest.TestCase):
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
            LeafNode("a", None).to_html()
    def test_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com", "attr": "more"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" attr="more">Click me!</a>')

class TestParentNode(unittest.TestCase):
    def test_to_html_many_children(self):
        nodes = ParentNode(
            "p",[
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            ],
        )
        node = ParentNode(
            "p",[
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
            ParentNode("a",[nodes])
            ],
        )
        self.assertEqual(node.to_html(),
            '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text<a><p><b>Bold text</b>Normal text<i>italic text</i></p></a></p>'
        )

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),"<div><span><b>grandchild</b></span></div>",)

    def test_no_tag_exception(self):
        with self.assertRaises(ValueError):
            child_node = LeafNode("span", "child")
            ParentNode(None, [child_node]).to_html()

    def test_no_children_exception(self):
        with self.assertRaises(ValueError):
            ParentNode("a", None).to_html()

    def test_with_props(self):
        child_node = LeafNode("span", "child")
        node = ParentNode("a", [child_node], {"href": "https://www.google.com", "attr": "more"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" attr="more"><span>child</span></a>')

if __name__ == "__main__":
    unittest.main()