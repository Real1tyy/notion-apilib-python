from main.data.Properties import *


class PageProperties(BaseModel):
    Quality: RelationProperty
    Tasks: RelationProperty
    Tags: RelationProperty
    Files_and_media: FilesProperty = Field(..., alias='Files & media')
    ID: UniqueIDProperty
    Area: RollupProperty
    Description: RichTextProperty
    Status: StatusProperty
    Resources: RelationProperty
    Archive: CheckboxProperty
    Sub_Notes: RelationProperty = Field(..., alias='Sub-Notes')
    Notebook: RelationProperty
    Goals: RelationProperty
    Projects: RelationProperty
    Rank_For_Quality_Sorting: RollupProperty = Field(..., alias='Rank For Quality Sorting')
    Last_edited_time: TimeProperty = Field(..., alias='Last edited time')
    Parent_Note: RelationProperty = Field(..., alias='Parent Note')
    Created_time: TimeProperty = Field(..., alias='Created time')
    Name: TitleProperty
