from htmlnode import LeafNode
from textnode import TextNode, TextType

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
