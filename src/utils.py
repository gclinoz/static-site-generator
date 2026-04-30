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
