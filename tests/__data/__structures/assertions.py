def assert_rich_text_structure(rich_text, expected_rich_text: dict):
    assert len(rich_text) == len(expected_rich_text)
    for index, text in enumerate(rich_text):
        assert_rich_text_value(text, expected_rich_text[index])


def assert_text_structure(text, expected_text: dict):
    assert text.content == expected_text["content"]
    assert text.link.url == expected_text["link"]["url"]


def assert_template_mention_structure(template_mention, expected_template_mention: dict):
    assert template_mention.type == expected_template_mention["type"]
    match template_mention.type:
        case "template_mention_date":
            assert template_mention.template_mention_date.type == expected_template_mention["template_mention_date"][
                "type"]
            assert template_mention.template_mention_user.template_mention_date == expected_template_mention[
                "template_mention_date"][
                "template_mention_date"]

        case "template_mention_user":
            assert template_mention.template_mention_user.type == expected_template_mention["template_mention_user"][
                "type"]
            assert template_mention.template_mention_user.template_mention_user == expected_template_mention[
                "template_mention_user"][
                "template_mention_user"]


def assert_mention_structure(mention, expected_mention: dict):
    assert mention.type == expected_mention["type"]
    match mention.type:
        case "database":
            assert mention.database.id == expected_mention["database"]["id"]
        case "date":
            assert mention.date.start == expected_mention["date"]["start"]
            assert mention.date.end == expected_mention["date"]["end"]
        case "link_preview":
            assert mention.link_preview.url == expected_mention["link_preview"]["url"]
        case "page":
            assert mention.page.id == expected_mention["page"]["id"]
        case "template_mention":
            assert_template_mention_structure(mention.template_mention, expected_mention["template_mention"])


def assert_equation_structure(equation, expected_equation: dict):
    assert equation.expression == expected_equation["expression"]


def assert_rich_text_value(rich_text, expected_rich_text: dict):
    assert rich_text.annotations.bold == expected_rich_text["annotations"]["bold"]
    assert rich_text.annotations.italic == expected_rich_text["annotations"]["italic"]
    assert rich_text.annotations.strikethrough == expected_rich_text["annotations"]["strikethrough"]
    assert rich_text.annotations.underline == expected_rich_text["annotations"]["underline"]
    assert rich_text.annotations.code == expected_rich_text["annotations"]["code"]
    assert rich_text.annotations.color == expected_rich_text["annotations"]["color"]
    assert rich_text.plain_text == expected_rich_text["plain_text"]
    assert rich_text.href == expected_rich_text["href"]

    assert rich_text.type == expected_rich_text["type"]
    match rich_text.type:
        case "text":
            assert_text_structure(rich_text.text, expected_rich_text["text"])
        case "mention":
            assert_mention_structure(rich_text.mention, expected_rich_text["mention"])
        case "equation":
            assert_equation_structure(rich_text.equation, expected_rich_text["equation"])


def assert_icon_structure(icon, expected_icon: dict):
    assert icon.type == expected_icon["type"]
    assert icon.emoji == expected_icon["emoji"]
    match icon.type:
        case "file_type":
            assert icon.file_type.url == expected_icon["file_type"]["url"]
            assert icon.file_type.expiry_time == expected_icon["file_type"]["expiry_time"]
        case "external":
            assert icon.external.url == expected_icon["external"]["url"]


def assert_user_structure(user, expected_user: dict):
    assert user.object == expected_user["object"]
    assert user.id == expected_user["id"]


def assert_parent_structure(parent, expected_parent: dict):
    assert parent.type == expected_parent["type"]
    match parent.type:
        case "database_id":
            assert parent.database_id == expected_parent["database_id"]
        case "page_id":
            assert parent.page_id == expected_parent["page_id"]
        case "workspace":
            assert parent.workspace
        case "block_id":
            assert parent.block_id == expected_parent["block_id"]
