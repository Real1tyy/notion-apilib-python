# Standard Library
from typing import Optional

from notion_api.data.properties import QueryFilter, Sort
from notion_api.data.blocks import Block, deserialize_block
# Third Party
from requests import Response

from typing import TypeVar, Callable, Any
import requests

T = TypeVar('T')


def _handle_pagination(
        result: T, response: Response, method_to_call: Callable[..., T], **kwargs: Any) -> T:
    """
    Handles paginated API responses by recursively retrieving data from subsequent pages.

    This function checks if there are additional pages of data available in the API response.
    If more pages are available, it extracts the `next_cursor` from the response and invokes the provided
    `method_to_call` to fetch the next page of data, accumulating the results in `result`.
    If no further pages are available, it returns the fully accumulated `result`.

    Args:
        result (T): The current object containing accumulated data from previous pages.
        response (requests.Response): The API response object from the current request.
        method_to_call (Callable[..., T]): A callable that takes `result`, `next_cursor`, and any number of additional
                                           arguments, and retrieves the next page of data.
        *args (Any): Additional positional arguments to pass to `method_to_call`.
        **kwargs (Any): Additional keyword arguments to pass to `method_to_call`.

    Returns:
        T: The fully accumulated object after all pages of data have been retrieved.
    """
    data = response.json()
    has_more = data['has_more']
    next_cursor = data['next_cursor']
    return method_to_call(result, next_cursor, **kwargs) if has_more else result


def _get_children_from_json(response: Response) -> list[dict[str, Any]]:
    return response.json()['results']


def _get_child_id_from_json(child: dict) -> str:
    return child['id']


def _create_children_json_payload(children_blocks: list[Block], after_block_id: str) -> dict:
    children = dict()
    children['children'] = [child.serialize_to_json() for child in children_blocks]
    if after_block_id:
        children['after'] = after_block_id
    return children


def _parse_and_serialize_result(response: dict) -> list[Block]:
    results = response['results']
    return [deserialize_block(block) for block in results]


def _prepare_query_data(
        next_cursor: Optional[str] = None, sort: Optional[list[Sort]] = None,
        filter: Optional[QueryFilter] = None) -> dict[str, Any]:
    data = dict()
    if next_cursor:
        data['start_cursor'] = next_cursor
    if sort:
        data['sorts'] = [s.serialize_to_json() for s in sort]
    if filter:
        data['filter'] = filter.serialize_to_json()
    return data
