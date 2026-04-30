from htmlnode import LeafNode
from textnode import TextNode, TextType
import re

def text_node_to_html_node(text_node):
    if text_node.text_type.value == 'text':
        return LeafNode(None, text_node.text)
    elif text_node.text_type.value == 'bold':
        return LeafNode('b', text_node.text)
    elif text_node.text_type.value == 'italic':
        return LeafNode('i', text_node.text)
    elif text_node.text_type.value == 'code':
        return LeafNode('code', text_node.text)
    elif text_node.text_type.value == 'link':
        return LeafNode('a', text_node.text, {"href": text_node.url})
    elif text_node.text_type.value == 'image':
        return LeafNode('img', '', {"src": text_node.url, "alt": text_node.text})
    else:
        raise Exception("Invalid text type")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for n in old_nodes:
        if n.text_type.value != 'text':
            new_nodes.append(n)
        else:
            chunks = n.text.split(delimiter)
            if len(chunks) % 2 == 0:
                raise Exception("Unmatched delimiter")

            for index, c in enumerate(chunks):
                if index % 2 == 0:
                    new_nodes.append(TextNode(c, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(c, text_type))

    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)

def split_nodes_image(old_nodes):
    new_nodes = []

    for n in old_nodes:
        if n.text == "":
            continue

        out = extract_markdown_images(n.text)
        if len(out) == 0:
            new_nodes.append(n)
            continue

        text = n.text
        for t in out:
            image_alt, image_link = t[0], t[1]
            sections = text.split(f"![{image_alt}]({image_link})", 1)
            text = sections[1]
            new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))

        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for n in old_nodes:
        if n.text == "":
            continue

        out = extract_markdown_links(n.text)
        if len(out) == 0:
            new_nodes.append(n)
            continue

        text = n.text
        for t in out:
            link_text, link_address = t[0], t[1]
            sections = text.split(f"[{link_text}]({link_address})", 1)
            text = sections[1]
            new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link_text, TextType.LINK, link_address))

        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes

def text_to_textnodes(text):
    raw = TextNode(text, TextType.TEXT)
    nodes = split_nodes_image([raw])
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    return nodes
