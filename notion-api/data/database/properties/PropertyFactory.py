from custom_types import json_
from database.properties.PropertyType import PropertyType


class PropertyFactory:
    from database.properties.concrete.CheckboxProperty import CheckboxProperty
    from values.DateProperty import DateProperty
    from values.EmailProperty import EmailProperty
    from values.FilesProperty import FilesProperty
    from database.properties.concrete.FormulaProperty import FormulaProperty
    from NumberProperty import NumberProperty
    from PeopleProperty import PeopleProperty
    from values.PhoneNumberProperty import PhoneNumberProperty
    from StatusProperty import StatusProperty
    from database.properties.concrete.UniqueIDProperty import UniqueIDProperty
    from values.UrlProperty import UrlProperty
    from database.properties.concrete.relations.RelationProperty import RelationProperty
    from database.properties.concrete.relations.RollupPropertyDTO import RollupProperty
    from database.properties.concrete.select.MultiSelectProperty import MultiSelectProperty
    from database.properties.concrete.select.SelectProperty import SelectProperty
    from database.properties.concrete.text.RichTextProperty import RichTextProperty
    from database.properties.concrete.text.TitleProperty import TitleProperty
    from database.properties.concrete.time.CreatedTimeProperty import CreatedTimeProperty
    from database.properties.concrete.time.LastEditedTimeProperty import LastEditedTimeProperty
    from database.properties.concrete.users.CreatedByProperty import CreatedByProperty
    from database.properties.concrete.users.LastEditedByProperty import LastEditedByProperty
    PROPERTY_TYPE_MAP = {
        PropertyType.TITLE: TitleProperty,
        PropertyType.RICH_TEXT: RichTextProperty,
        PropertyType.NUMBER: NumberProperty,
        PropertyType.SELECT: SelectProperty,
        PropertyType.MULTI_SELECT: MultiSelectProperty,
        PropertyType.DATE: DateProperty,
        PropertyType.PEOPLE: PeopleProperty,
        PropertyType.FILES: FilesProperty,
        PropertyType.CHECKBOX: CheckboxProperty,
        PropertyType.URL: UrlProperty,
        PropertyType.EMAIL: EmailProperty,
        PropertyType.PHONE_NUMBER: PhoneNumberProperty,
        PropertyType.FORMULA: FormulaProperty,
        PropertyType.RELATION: RelationProperty,
        PropertyType.ROLLUP: RollupProperty,
        PropertyType.CREATED_TIME: CreatedTimeProperty,
        PropertyType.CREATED_BY: CreatedByProperty,
        PropertyType.LAST_EDITED_TIME: LastEditedTimeProperty,
        PropertyType.LAST_EDITED_BY: LastEditedByProperty,
        PropertyType.UNIQUE_ID: UniqueIDProperty,
        PropertyType.STATUS: StatusProperty,
    }

    @staticmethod
    def create_concrete_property_dto(data: json_):
        property_type = PropertyType(data["type"])
        return PropertyFactory.PROPERTY_TYPE_MAP[property_type](**data)
