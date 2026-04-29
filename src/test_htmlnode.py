import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", "test words", children=None, props={"href": "https://www.xyz.net", "target": "_blank"})
        expected = ' href="https://www.xyz.net" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_leaf_to_html(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.xyz.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.xyz.com">Click me!</a>') 

    def test_to_html_no_child(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_more_children(self):
        child_node = LeafNode("span", "child")
        child_node2 = LeafNode("b", "many child")
        parent_node = ParentNode("div", [child_node, child_node2])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span><b>many child</b></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()
