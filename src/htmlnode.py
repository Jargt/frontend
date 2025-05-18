class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        string = ''
        if self.props is not None:
            for x in self.props:
                string += ' ' + x + '="' + self.props[x] + '"'
        return string
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})'
    
    def __eq__(self, other):
        return (
            other.tag == self.tag and
            other.value == self.value and
            other.children == self.children and
            other.props == self.props
        )
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if self.tag == None:
            return self.value
        if self.value == None:
            raise ValueError("invalid HTML: no value")
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props})'
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("invalid HTML: no tag")
        if self.children == None:
            raise ValueError("invalid HTML: no children")
        recursion_text = "".join(list(map(lambda x: x.to_html(), self.children)))
        return f'<{self.tag}{self.props_to_html()}>{recursion_text}</{self.tag}>'
        
    def __repr__(self):
        return f'ParentNode({self.tag}, children: {self.children}, {self.props})'
    