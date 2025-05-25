from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        else:
            parts = old_node.text.split(delimiter)
            if len(parts) == 1:
                new_nodes.append(old_node)
            if len(parts) % 2 == 0:
                raise ValueError("invalid markdown, formatted section not closed")
            for i in range(len(parts)):
                types = [TextType.TEXT, text_type]
                if len(parts[i]) != 0:
                    new_nodes.append(TextNode(parts[i], types[i % 2]))
    return new_nodes
