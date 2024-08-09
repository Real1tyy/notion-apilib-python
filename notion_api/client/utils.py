# Standard Library
from typing import Optional

# Third Party
from custom_types import json_
from requests import Response


def _access_children(response: Response) -> Optional[json_]:
    return response.json()['results']


def _access_child_id(child: json_) -> str:
    return child['id']
