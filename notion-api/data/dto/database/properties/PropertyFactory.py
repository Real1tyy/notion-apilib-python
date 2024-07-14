from client.api_requests.custom_types import json_
from database.properties.PropertyType import PropertyType


class PropertyFactory:
    from database.properties.concrete.CheckboxPropertyDTO import CheckboxPropertyDTO
    from values.DatePropertyDTO import DatePropertyDTO
    from values.EmailPropertyDTO import EmailPropertyDTO
    from values.FilesPropertyDTO import FilesPropertyDTO
    from database.properties.concrete.FormulaPropertyDTO import FormulaPropertyDTO
    from number.NumberPropertyDTO import NumberPropertyDTO
    from PeoplePropertyDTO import PeoplePropertyDTO
    from values.PhoneNumberPropertyDTO import PhoneNumberPropertyDTO
    from StatusPropertyDTO import StatusPropertyDTO
    from database.properties.concrete.UniqueIDPropertyDTO import UniqueIDPropertyDTO
    from values.UrlPropertyDTO import UrlPropertyDTO
    from database.properties.concrete.relations.RelationPropertyDTO import RelationPropertyDTO
    from database.properties.concrete.relations.RollupPropertyDTO import RollupPropertyDTO
    from database.properties.concrete.select.MultiSelectPropertyDTO import MultiSelectPropertyDTO
    from database.properties.concrete.select.SelectPropertyDTO import SelectPropertyDTO
    from database.properties.concrete.text.RichTextPropertyDTO import RichTextPropertyDTO
    from database.properties.concrete.text.TitlePropertyDTO import TitlePropertyDTO
    from database.properties.concrete.time.CreatedTimePropertyDTO import CreatedTimePropertyDTO
    from database.properties.concrete.time.LastEditedTimePropertyDTO import LastEditedTimePropertyDTO
    from database.properties.concrete.users.CreatedByPropertyDTO import CreatedByPropertyDTO
    from database.properties.concrete.users.LastEditedByPropertyDTO import LastEditedByPropertyDTO
    PROPERTY_TYPE_MAP = {
        PropertyType.TITLE: TitlePropertyDTO,
        PropertyType.RICH_TEXT: RichTextPropertyDTO,
        PropertyType.NUMBER: NumberPropertyDTO,
        PropertyType.SELECT: SelectPropertyDTO,
        PropertyType.MULTI_SELECT: MultiSelectPropertyDTO,
        PropertyType.DATE: DatePropertyDTO,
        PropertyType.PEOPLE: PeoplePropertyDTO,
        PropertyType.FILES: FilesPropertyDTO,
        PropertyType.CHECKBOX: CheckboxPropertyDTO,
        PropertyType.URL: UrlPropertyDTO,
        PropertyType.EMAIL: EmailPropertyDTO,
        PropertyType.PHONE_NUMBER: PhoneNumberPropertyDTO,
        PropertyType.FORMULA: FormulaPropertyDTO,
        PropertyType.RELATION: RelationPropertyDTO,
        PropertyType.ROLLUP: RollupPropertyDTO,
        PropertyType.CREATED_TIME: CreatedTimePropertyDTO,
        PropertyType.CREATED_BY: CreatedByPropertyDTO,
        PropertyType.LAST_EDITED_TIME: LastEditedTimePropertyDTO,
        PropertyType.LAST_EDITED_BY: LastEditedByPropertyDTO,
        PropertyType.UNIQUE_ID: UniqueIDPropertyDTO,
        PropertyType.STATUS: StatusPropertyDTO,
    }

    @staticmethod
    def create_concrete_property_dto(data: json_):
        property_type = PropertyType(data["type"])
        return PropertyFactory.PROPERTY_TYPE_MAP[property_type](**data)
