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
