from sre_constants import BRANCH
from urllib.parse import quote

class URLBuilder():
    _branch = ""
    _api_endpoint = "https://snowstorm.ihtsdotools.org/snowstorm/snomed-ct/"
    _headers = {}

    def __init__(self):
        pass

    @property
    def api_endpoint(self) -> str:
        return self._api_endpoint + self._branch

    @property
    def headers(self):
        return self._headers

    def set_api_endpoint(self, api_url: str,) -> None:
        if not api_url.endswith("/"):
            api_url += "/"
        self._api_endpoint = api_url

    def set_branch(self, branch: str) -> None:
        self._branch = branch

    def set_headers(self, headers: dict) -> None:
        self._headers = headers
