def markdown_to_blocks(text):
    blocks = text.split("\n\n")

    result = []
    for b in blocks:
        if b.strip() == "":
            continue
        else:
            result.append(b.strip())

    return result
