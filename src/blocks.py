from enum import Enum
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
