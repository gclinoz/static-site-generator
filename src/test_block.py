import unittest
from blocks import markdown_to_blocks, block_to_block_type, BlockType

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


if __name__ == "__main__":
    unittest.main()
