class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        fmt_str = ''

        if self.props == None or len(self.props) == 0:
            return fmt_str

        for k in self.props:
            fmt_str += f' {k}="{self.props[k]}"'

        return fmt_str

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        else:
            if self.props == None or len(self.props) == 0:
                return f"<{self.tag}>{self.value}</{self.tag}>"
            else:
                fmt_str = ''
                for k in self.props:
                    fmt_str += f' {k}="{self.props[k]}"'
                return f'<{self.tag}{fmt_str}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
