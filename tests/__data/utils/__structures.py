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


def assert_rich_text_structure(rich_text, content: str, color: str):
    assert len(rich_text) == 1
    assert_rich_text_value(rich_text[0], content, color)


def assert_rich_text_value(value, content: str, color: str):
    assert value.type == "text"
    assert value.text.content == content
    assert value.text.link is None
    assert value.annotations.bold is False
    assert value.annotations.italic is False
    assert value.annotations.strikethrough is False
    assert value.annotations.underline is False
    assert value.annotations.code is False
    assert value.annotations.color == color
    assert value.plain_text == content
    assert value.href is None
