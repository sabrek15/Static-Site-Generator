import re
from enum import Enum
from htmlnode import HTMLNode, LeafNode, ParentNode

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = [block.strip() for block in markdown.strip().split("\n\n")]

    return [block for block in blocks if block]


def block_to_block_type(block):
    block = block.strip()
    lines = [line for line in block.split('\n')]

    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    elif all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    elif all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    elif all(re.match(r"^\d+\. ", line) for line in lines):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
    
def convert_inline_markdown(text):
    text = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", text)  # **bold** -> <b>bold</b>
    text = re.sub(r"\_(.*?)\_", r"<i>\1</i>", text)      # _italic_ -> <i>italic</i>
    text = re.sub(r"\`(.*?)\`", r"<code>\1</code>", text) # `code` -> <code>code</code>
    return text

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        blocktype = block_to_block_type(block)
        
        if blocktype == BlockType.HEADING:
            for line in block.split('\n'):
                level = len(line) - len(line.lstrip("#"))
                tag = f"h{level}"
                value = line[level:].strip()
                children.append(LeafNode(tag, convert_inline_markdown(value), None))

        elif blocktype == BlockType.CODE:
            value = block[3:-3]
            children.append(LeafNode("pre", convert_inline_markdown(value), None))

        elif blocktype == BlockType.QUOTE:
            tag = "blockquote"
            value = " ".join([line.lstrip("> ").strip() for line in block.split('\n')])
            children.append(LeafNode(tag, convert_inline_markdown(value)))

        elif blocktype == BlockType.ORDERED_LIST:
            list_items = [LeafNode("li", convert_inline_markdown(line[2:].strip())) for line in block.split('\n')]
            children.append(ParentNode("ol", list_items))

        elif blocktype == BlockType.UNORDERED_LIST:
            list_items = [LeafNode("li", convert_inline_markdown(line[2:].strip())) for line in block.split('\n')]
            children.append(ParentNode("ul", list_items))

        else:
            paragraph_text = " ".join(block.split('\n')).strip()
            children.append(LeafNode("p", convert_inline_markdown(paragraph_text)))

    return ParentNode("div", children)