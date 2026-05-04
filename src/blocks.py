from enum import Enum
from htmlnode import LeafNode, ParentNode
from textnode import TextNode, TextType
from utils import text_to_textnodes, text_node_to_html_node
import re

class BlockType(Enum):
    PA = "paragraph"
    H = "heading"
    CO = "code"
    Q = "quote"
    UL = "unordered_list"
    OL = "ordered_list"

def block_to_block_type(text):
    if re.match(r"#{1,6}", text):
        return BlockType.H
    elif re.match(r"```", text):
        return BlockType.CO
    elif re.match(r">", text):
        return BlockType.Q
    elif re.match(r"- ", text):
        return BlockType.UL
    elif re.match(r"1. ", text):
        return BlockType.OL
    else:
        return BlockType.PA

def markdown_to_blocks(text):
    blocks = text.split("\n\n")

    result = []
    for b in blocks:
        if b.strip() == "":
            continue
        else:
            result.append(b.strip())

    return result

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return list(map(text_node_to_html_node, text_nodes))

def list_to_html_node(block, li_type):
    lines = block.split("\n")
    li_nodes = []
    if li_type == "ol":
        for line in lines:
            text = lines[3:] 
            children = text_to_children(text)
            li_nodes.append(ParentNode("li", children))
        return ParentNode("ol", li_nodes)
    else:
        for line in lines:
            text = lines[2:] 
            children = text_to_children(text)
            li_nodes.append(ParentNode("li", children))
        return ParentNode("ul", li_nodes)

def markdown_to_html_node(text):

    block_nodes = []
    blocks = markdown_to_blocks(text)

    for b in blocks:
        b_type = block_to_block_type(b).value

        if b_type == "quote":
            new_node = ParentNode("blockquote", text_to_children(b))
            block_nodes.append(new_node)
        elif b_type == "paragraph":
            input_text = b.replace("\n", " ").strip()
            new_node = ParentNode("p", text_to_children(input_text))
            block_nodes.append(new_node)
        elif b_type == "heading":
            level_h = len(re.match(r"#{1,6}", b).group())
            new_node = ParentNode(f"h{level_h}", text_to_children(b))
            block_nodes.append(new_node)
        elif b_type == "unordered_list":
            block_nodes.append(list_to_html_node(b, "ul"))
        elif b_type == "ordered_list":
            block_nodes.append(list_to_html_node(b, "ol"))
        else:
            input_text = b.replace("`", "").strip()
            text_node = TextNode(input_text, TextType.CODE)
            inner = text_node_to_html_node(text_node)
            block_nodes.append(ParentNode("pre", [inner]))

    return ParentNode("div", block_nodes)
