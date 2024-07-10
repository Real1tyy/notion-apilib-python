from typing import Optional

from pydantic import BaseModel, Field

from general.ObjectDTO import ObjectDTO


class Properties(ObjectDTO):
    pass


class UniqueID(BaseModel):
    prefix: str
    number: int


class StatusDetail(BaseModel):
    id: str
    name: str
    color: str


class RelationItem(BaseModel):
    id: Optional[str] = None


class FileItem(BaseModel):
    # Assuming structure for files if needed, adjust based on actual file structure
    pass


class Rollup(BaseModel):
    type: str
    array: list = []
    function: str


class RichTextItem(BaseModel):
    type: str
    text: dict
    annotations: dict
    plain_text: str
    href: Optional[str] = None


class PropertyBase(BaseModel):
    id: str
    type: str


class RelationProperty(PropertyBase):
    relation: list[RelationItem]
    has_more: bool


class FilesProperty(PropertyBase):
    files: list[FileItem]


class UniqueIDProperty(PropertyBase):
    unique_id: UniqueID


class RollupProperty(PropertyBase):
    rollup: Rollup


class RichTextProperty(PropertyBase):
    rich_text: list[RichTextItem]


class StatusProperty(PropertyBase):
    status: StatusDetail


class CheckboxProperty(PropertyBase):
    checkbox: bool


class TimeProperty(PropertyBase):
    last_edited_time: Optional[str] = Field(None, alias='last_edited_time')
    created_time: Optional[str] = Field(None, alias='created_time')


class TitleProperty(PropertyBase):
    title: list[RichTextItem]
