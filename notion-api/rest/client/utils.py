from typing import Optional

from requests import Response

from custom_types import json_


def _access_children(response: Response) -> Optional[json_]:
    return response.json()['results']


def _access_child_id(child: json_) -> str:
    return child['id']
