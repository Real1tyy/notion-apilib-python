from requests import Response

import time
from client.api_requests.constants.status_codes import SUCCESS, RATE_LIMIT


class RequestsStatusChecker:

    @staticmethod
    def check_response_status(response: Response) -> bool:
        if response.status_code == SUCCESS:
            return True
        if response.status_code == RATE_LIMIT:
            print("Timed out rate limit reached")
            time.sleep(1)
        return False
