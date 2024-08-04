# Third Party
from Block import Block, _create_block
from BlockType import BlockType
from Parent import Parent


class Divider(Block):
    pass


def create_divider(parent: Parent) -> Divider:
    """
    Factory method to create Divider object
    :param parent: parent object
    :return: newly created Divider Object
    """
    return _create_block(
        Divider,
        parent=parent,
        block_type=BlockType.DIVIDER,
    )


class ColumnList(Block):
    pass


def create_column_list(parent: Parent) -> ColumnList:
    """
    Factory method to create ColumnList object
    :param parent: parent object
    :return: newly created ColumnList Object
    """
    return _create_block(
        ColumnList,
        parent=parent,
        block_type=BlockType.COLUMN_LIST,
    )


class Breadcrumb(Block):
    pass


def create_breadcrumb(parent: Parent) -> Breadcrumb:
    """
    Factory method to create Breadcrumb object
    :param parent: parent object
    :return: newly created Breadcrumb Object
    """
    return _create_block(
        Breadcrumb,
        parent=parent,
        block_type=BlockType.BREADCRUMB,
    )


class Unsupported(Block):
    pass


def create_unsupported(parent: Parent) -> Unsupported:
    """
    Factory method to create Unsupported object
    :param parent: parent object
    :return: newly created Unsupported Object
    """
    return _create_block(
        Unsupported,
        parent=parent,
        block_type=BlockType.UNSUPPORTED,
    )
