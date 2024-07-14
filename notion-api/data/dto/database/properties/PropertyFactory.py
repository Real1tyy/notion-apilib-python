from client.api_requests.custom_types import json_
from database.properties.PropertyTypes import PropertyTypes


class DatabasePropertyFactory:
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
        PropertyTypes.TITLE: TitlePropertyDTO,
        PropertyTypes.RICH_TEXT: RichTextPropertyDTO,
        PropertyTypes.NUMBER: NumberPropertyDTO,
        PropertyTypes.SELECT: SelectPropertyDTO,
        PropertyTypes.MULTI_SELECT: MultiSelectPropertyDTO,
        PropertyTypes.DATE: DatePropertyDTO,
        PropertyTypes.PEOPLE: PeoplePropertyDTO,
        PropertyTypes.FILES: FilesPropertyDTO,
        PropertyTypes.CHECKBOX: CheckboxPropertyDTO,
        PropertyTypes.URL: UrlPropertyDTO,
        PropertyTypes.EMAIL: EmailPropertyDTO,
        PropertyTypes.PHONE_NUMBER: PhoneNumberPropertyDTO,
        PropertyTypes.FORMULA: FormulaPropertyDTO,
        PropertyTypes.RELATION: RelationPropertyDTO,
        PropertyTypes.ROLLUP: RollupPropertyDTO,
        PropertyTypes.CREATED_TIME: CreatedTimePropertyDTO,
        PropertyTypes.CREATED_BY: CreatedByPropertyDTO,
        PropertyTypes.LAST_EDITED_TIME: LastEditedTimePropertyDTO,
        PropertyTypes.LAST_EDITED_BY: LastEditedByPropertyDTO,
        PropertyTypes.UNIQUE_ID: UniqueIDPropertyDTO,
        PropertyTypes.STATUS: StatusPropertyDTO,
    }

    @staticmethod
    def create_concrete_property_dto(data: json_):
        property_type = PropertyTypes(data["type"])
        return DatabasePropertyFactory.PROPERTY_TYPE_MAP[property_type](**data)
