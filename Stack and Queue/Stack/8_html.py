import re

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0


def match_html_tags(html):
    s = Stack()

    # Regex to capture full tags, including attributes
    # e.g. <h1 class="title">, </h1>, <img src="x.png" />, <div id='a'>
    tags = re.findall(r"</?[a-zA-Z0-9]+(?:\s+[^>]*)?>", html)

    for full_tag in tags:
        # Extract the tag name only (ignoring attributes)
        tag_match = re.match(r"</?([a-zA-Z0-9]+)", full_tag)
        if not tag_match:
            continue
        tag_name = tag_match.group(1)

        if full_tag.startswith("</"):  # Closing tag
            if s.is_empty() or s.pop() != tag_name:
                return False

        elif full_tag.endswith("/>"):  # Self-closing tag (e.g. <img />, <br/>)
            continue

        else:  # Opening tag
            s.push(tag_name)

    return s.is_empty()


# ✅ Example usage
html1 = '<html><body><h1 class="title">Hello</h1></body></html>'
print(match_html_tags(html1))  # True

html2 = '<html><body><h1 class="title">Hello</body></html>'
print(match_html_tags(html2))  # False

html3 = '<html><body><div id="main"><p style="color:red">Hi</p></div></body></html>'
print(match_html_tags(html3))  # True

html4 = '<html><body><br/><img src="test.png" alt="sample"/></body></html>'
print(match_html_tags(html4))  # True
