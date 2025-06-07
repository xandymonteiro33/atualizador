import re


def parse_items(html):
    """Parse items from given HTML.

    Example expected HTML snippet:
        <li>Item 1</li>
        <li>Item 2</li>

    Returns a list of item strings.
    """
    if not isinstance(html, str):
        raise TypeError("html must be a string")
    return re.findall(r"<li>(.*?)</li>", html)

