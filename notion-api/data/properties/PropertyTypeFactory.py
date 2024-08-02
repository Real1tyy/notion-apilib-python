from CheckboxProperty import CheckboxProperty
from Date import Date
from FormulaProperty import FormulaProperty
from MultiSelectProperty import MultiSelectProperty
from NumberProperty import NumberProperty
from PropertyType import PropertyType
from RelationProperty import RelationProperty
from ResourcesProperties import PhoneNumberProperty, UrlProperty, EmailProperty, FilesProperty
from RichTextProperty import RichTextProperty
from RollupProperty import RollupProperty
from SelectProperty import SelectProperty
from StatusProperty import StatusProperty
from TimeProperties import CreatedTimeProperty, LastEditedTimeProperty
from TitleProperty import TitleProperty
from UniqueIDProperty import UniqueIDProperty
from UsersProperties import LastEditedByProperty, CreatedByProperty, PeopleProperty
from custom_types import json_

PROPERTY_TYPE_MAP = {
    "title": TitleProperty,
    "rich_text": RichTextProperty,
    "number": NumberProperty,
    "select": SelectProperty,
    "multi_select": MultiSelectProperty,
    "date": Date,
    "people": PeopleProperty,
    "files": FilesProperty,
    "checkbox": CheckboxProperty,
    "url": UrlProperty,
    "email": EmailProperty,
    "phone_number": PhoneNumberProperty,
    "formula": FormulaProperty,
    "relation": RelationProperty,
    "rollup": RollupProperty,
    "created_time": CreatedTimeProperty,
    "created_by": CreatedByProperty,
    "last_edited_time": LastEditedTimeProperty,
    "last_edited_by": LastEditedByProperty,
    "unique_id": UniqueIDProperty,
    "status": StatusProperty,
}


def create_concrete_property_type(data: json_):
    property_type = PropertyType(data["type"])
    return PROPERTY_TYPE_MAP[property_type](**data)
