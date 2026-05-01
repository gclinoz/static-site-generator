import unittest
from blocks import markdown_to_blocks

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

    def test_markdown_to_blocks_blink(self):
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


if __name__ == "__main__":
    unittest.main()
