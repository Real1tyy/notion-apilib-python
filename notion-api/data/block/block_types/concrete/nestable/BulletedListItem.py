from Block import Block
from RichText import RichText


class BulletedListItem(Block):
    color: str
    children: list[Block]
    rich_text: list[RichText]
