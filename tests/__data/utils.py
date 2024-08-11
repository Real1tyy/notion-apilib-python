def create_rich_text_data(content: str, color: str) -> dict:
    return {
        "type": "text",
        "text": {
            "content": content,
            "link": None
        },
        "annotations": {
            "bold": False,
            "italic": False,
            "strikethrough": False,
            "underline": False,
            "code": False,
            "color": color
        },
        "plain_text": content,
        "href": None
    }


def create_emoji_data(emoji: str) -> dict:
    return {
        "type": "emoji",
        "emoji": emoji
    }


def assert_rich_text_data(rich_text, content: str, color: str):
    assert rich_text.type == "text"
    assert rich_text.text.content == content
    assert rich_text.text.link is None
    assert rich_text.annotations.bold is False
    assert rich_text.annotations.italic is False
    assert rich_text.annotations.strikethrough is False
    assert rich_text.annotations.underline is False
    assert rich_text.annotations.code is False
    assert rich_text.annotations.color == color
    assert rich_text.plain_text == content
    assert rich_text.href is None
