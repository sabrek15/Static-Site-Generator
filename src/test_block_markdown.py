import unittest

from block_markdown import (BlockType, markdown_to_blocks, block_to_block_type, markdown_to_html_node)

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
    
    def test_headings(self):
        md = """
# Heading 1
## Heading 2
### Heading 3
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3</h3></div>",
        )

    def test_blockquote(self):
        md = """
> This is a quote
> that spans multiple lines.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote that spans multiple lines.</blockquote></div>",
        )

    def test_unordered_list(self):
        md = """
- Item 1
- Item 2
- Item 3
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. First item
2. Second item
3. Third item
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First item</li><li>Second item</li><li>Third item</li></ol></div>",
        )


if __name__ == "__main__":
    unittest.main()