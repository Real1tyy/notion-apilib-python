# Third Party
from pydantic import BaseModel

from blocks.block import Block


class ChildAttributes(BaseModel):
    """
    Represents the attributes of a child in the Notion API.

    :param title: The title of the child.
    :type title: str
    """
    title: str


class ChildDatabase(Block):
    """
    Represents a ChildDatabase block in the Notion API.

    :param child_database: The attributes of the child database.
    :type child_database: ChildAttributes
    """
    child_database: ChildAttributes


class ChildPage(Block):
    """
    Represents a ChildPage block in the Notion API.

    :param child_page: The attributes of the child page.
    :type child_page: ChildAttributes
    """
    child_page: ChildAttributes
