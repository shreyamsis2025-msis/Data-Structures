import re

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop() if not self.is_empty() else None
    def is_empty(self):
        return len(self.stack) == 0

def match_html_tags(file_path):
    with open(file_path, 'r') as f:
        html = f.read()

    s = Stack()
    tags = re.findall(r"</?[a-zA-Z0-9]+[^>]*>", html)

    for full_tag in tags:
        tag_name_match = re.match(r"</?([a-zA-Z0-9]+)", full_tag)
        if not tag_name_match:
            continue  

        tag_name = tag_name_match.group(1)

        if full_tag.startswith("</"):  
            if s.is_empty() or s.pop() != tag_name:
                return False
        elif full_tag.endswith("/>"):
            continue  
        else:  
            s.push(tag_name)

    return s.is_empty()

file_path = "Stack/sample.html"
print(match_html_tags(file_path))


# def is_html_balanced_from_file(file_path):
#     with open(file_path, 'r') as f:
#         html = f.read()

#     stack = []
#     i = 0
#     while i < len(html):
#         if html[i] == '<':
#             j = html.find('>', i + 1)
#             if j == -1:
#                 return False  # Missing closing '>'
#             tag = html[i+1:j].strip()

#             # Ignore self-closing tags and comments
#             if not tag.endswith('/') and not tag.startswith('!'):
#                 if not tag.startswith('/'):
#                     # Opening tag
#                     stack.append(tag.split()[0])  # Handle attributes
#                 else:
#                     # Closing tag
#                     closing_tag = tag[1:]
#                     if not stack or stack[-1] != closing_tag:
#                         return False
#                     stack.pop()
#             i = j
#         i += 1

#     return len(stack) == 0


# # Example usage
# file_path = 'Stack\sample.html'  # your HTML file
# if is_html_balanced_from_file(file_path):
#     print("HTML tags are properly matched.")
# else:
#     print("HTML tags are NOT matched.")