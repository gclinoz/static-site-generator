import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType
from utils import text_node_to_html_node

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", "test words", children=None, props={"href": "https://www.xyz.net", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.xyz.net" target="_blank"')

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

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_tag(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, "This is a bold text node")

    def test_text_link(self):
        node = TextNode("This is a link text node", TextType.LINK, "https://www.abc.xyz")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.value, "This is a link text node")
        self.assertEqual(html_node.props, {"href": "https://www.abc.xyz"})

if __name__ == "__main__":
    unittest.main()
