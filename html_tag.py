def get_html(body_content: str, head: str) -> str:
    html_tag = '<html lang="en">' + head + body_content + "</html>"
    return html_tag
