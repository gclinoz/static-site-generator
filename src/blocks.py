from enum import Enum
from htmlnode import LeafNode, ParentNode
from textnode import TextNode, TextType
from utils import text_to_textnodes, text_node_to_html_node, extract_title
from pathlib import Path
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
            text = line[3:] 
            children = text_to_children(text.strip())
            li_nodes.append(ParentNode("li", children))
        return ParentNode("ol", li_nodes)
    else:
        for line in lines:
            text = line[2:] 
            children = text_to_children(text.strip())
            li_nodes.append(ParentNode("li", children))
        return ParentNode("ul", li_nodes)

def markdown_to_html_node(text):

    block_nodes = []
    blocks = markdown_to_blocks(text)

    for b in blocks:
        b_type = block_to_block_type(b).value

        if b_type == "quote":
            input_text = b.replace(">", "").strip()
            new_node = ParentNode("blockquote", text_to_children(input_text))
            block_nodes.append(new_node)
        elif b_type == "paragraph":
            input_text = b.replace("\n", " ").strip()
            new_node = ParentNode("p", text_to_children(input_text))
            block_nodes.append(new_node)
        elif b_type == "heading":
            level_h = len(re.match(r"#{1,6}", b).group())
            input_text = b.replace("#", "").strip()
            new_node = ParentNode(f"h{level_h}", text_to_children(input_text))
            block_nodes.append(new_node)
        elif b_type == "unordered_list":
            block_nodes.append(list_to_html_node(b, "ul"))
        elif b_type == "ordered_list":
            block_nodes.append(list_to_html_node(b, "ol"))
        elif b_type == "code":
            input_text = b.replace("`", "").strip()
            text_node = TextNode(input_text, TextType.CODE)
            inner = text_node_to_html_node(text_node)
            block_nodes.append(ParentNode("pre", [inner]))
        else:
            raise Exception("Invalid block type")

    return ParentNode("div", block_nodes)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as file:
        md = file.read()

    with open(template_path, "r") as file:
        tp = file.read()

    html = markdown_to_html_node(md).to_html()
    page_title = extract_title(md)
    final = tp.replace("{{ Title }}", page_title).replace("{{ Content }}", html)

    dest = Path(dest_path)
    if not dest.parent.exists():
        dest.parent.mkdir(parents=True)

    with open(dest, "w") as f:
        f.write(final)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    src = Path(dir_path_content)
    dest = Path(dest_dir_path)

    md_list = list(src.rglob("*.md"))
    for md in md_list:
        new_dest = str(md).replace(src.name, dest.name).replace("md", "html")
        generate_page(md, template_path, new_dest)
