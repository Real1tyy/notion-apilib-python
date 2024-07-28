from custom_types import json_


def validate_rich_text(v: json_):
    rich_text = v.pop('rich_text')
    if len(rich_text) > 0:
        rich_text[0].pop('type')
        v.update(rich_text[0])
    else:
        v['plain_text'] = ''
    return v
