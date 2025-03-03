import unittest

from block_markdown import (BlockType, markdown_to_blocks, block_to_block_type)

class TestBlockMarkdown(unittest.TestCase):
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
    
    def test_empty_markdown(self):
        self.assertEqual(markdown_to_blocks(""), [])
    
    def test_only_newlines(self):
        md = "\n\n\n"
        self.assertEqual(markdown_to_blocks(md), [])
    
    def test_mixed_content(self):
        md = """
# Heading

Some paragraph here.

- Item 1
- Item 2

Another paragraph with **bold text**.
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# Heading",
                "Some paragraph here.",
                "- Item 1\n- Item 2",
                "Another paragraph with **bold text**."
            ]
        )


    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Small Heading"), BlockType.HEADING)
    
    def test_code_block(self):
        self.assertEqual(block_to_block_type("```\nprint('Hello, world!')\n```"), BlockType.CODE)
    
    def test_quote(self):
        self.assertEqual(block_to_block_type("> This is a quote\n> Another quote line"), BlockType.QUOTE)
    
    def test_unordered_list(self):
        self.assertEqual(block_to_block_type("- Item 1\n- Item 2"), BlockType.UNORDERED_LIST)
    
    def test_ordered_list(self):
        self.assertEqual(block_to_block_type("1. First\n2. Second"), BlockType.ORDERED_LIST)
    
    def test_paragraph(self):
        self.assertEqual(block_to_block_type("This is a normal paragraph."), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()