from datetime import datetime
from typing import Literal, Optional

from pydantic import BaseModel

from Property import PageProperty, DatabaseProperty


class FormulaStructure(BaseModel):
    type: Literal['boolean', 'date', 'number', 'string']
    number: Optional[float] = None
    boolean: Optional[bool] = None
    date: Optional[datetime] = None
    string: Optional[str] = None


class FormulaPage(PageProperty):
    formula: FormulaStructure


class FormulaDatabase(DatabaseProperty):
    expression: str
