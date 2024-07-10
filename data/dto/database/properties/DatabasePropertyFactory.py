from client.requests.types import json_
from database.properties.PropertyTypes import PropertyTypes
from database.properties.RelationPropertyDTO import RelationPropertyDTO


class DatabasePropertyFactory:
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
