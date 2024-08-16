# Standard Library
import time

# Third Party
from requests import Response

# First Party
from notion_api.client._api_requests.constants.status_codes import RATE_LIMIT, SUCCESS


def check_response_status(response: Response) -> bool:
    if response.status_code == SUCCESS:
        return True
    if response.status_code == RATE_LIMIT:
        print("Timed out rate limit reached")
        time.sleep(1)
    return False
