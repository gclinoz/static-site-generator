import unittest
from htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main()
