import unittest
from blocks import markdown_to_blocks, block_to_block_type, BlockType, markdown_to_html_node

class TestBlock(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_empty(self):
        md = ""

        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_markdown_to_blocks_blank(self):
        md = """
This is _italic_ paragraph

This is another paragraph with ~~cancelled~~ text
This is the same paragraph on a new line



1. apple
2. banana

"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is _italic_ paragraph",
                "This is another paragraph with ~~cancelled~~ text\nThis is the same paragraph on a new line",
                "1. apple\n2. banana",
            ]
        )

    def test_block_type_normal(self):
        md = "There is nothing speical in this sentence."
        self.assertEqual(block_to_block_type(md), BlockType.PA)

    def test_block_type_head(self):
        md = "###There is nothing speical in this sentence."
        self.assertEqual(block_to_block_type(md), BlockType.H)

    def test_block_type_code(self):
        md = """```
for (i = 0; i < K; i++)
{
}
```
"""
        self.assertEqual(block_to_block_type(md), BlockType.CO)

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff</code></pre></div>",
        )

    def test_heading(self):
        md = "###Greatest title of all time"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h3>Greatest title of all time</h3></div>"
        )

    def test_unorder_list(self):
        md = """- this is a list
- with items
- with more items
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>this is a list</li><li>with items</li><li>with more items</li></ul></div>"
        )

    def test_list(self):
        md = """1. this is a list
2. with items
3. with more items
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>this is a list</li><li>with items</li><li>with more items</li></ol></div>"
        )

    def test_quote(self):
        md = """> this is quote text
the words are awesome
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>this is quote text\nthe words are awesome</blockquote></div>"
        )

if __name__ == "__main__":
    unittest.main()
