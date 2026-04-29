import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_p2h_1(self):
        node = HTMLNode("h1", "test words", children=None, props={"href": "https://www.xyz.net"})
        expected = ' href="https://www.xyz.net"'
        self.assertEqual(node.props_to_html(), expected)

    def test_p2h_2(self):
        node = HTMLNode("p", "test words", children=None, props={"href": "https://www.xyz.net", "target": "_blank"})
        expected = ' href="https://www.xyz.net" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_p2h_3(self):
        node = HTMLNode("a", "test words", children=None, props={"href": "https://www.xyz.net", "id": "920"})
        expected = ' href="https://www.xyz.net" id="920"'
        self.assertEqual(node.props_to_html(), expected)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>") 

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.xyz.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.xyz.com">Click me!</a>') 

if __name__ == "__main__":
    unittest.main()
