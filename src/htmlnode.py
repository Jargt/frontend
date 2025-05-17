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
        if len(self.props) != 0:
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