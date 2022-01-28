class EndpointBuilder():
    _branch = "MAIN"
    _api_endpoint = "https://snowstorm.ihtsdotools.org/snowstorm/snomed-ct/"
    _headers = {"Accept": "application/json"}

    def __init__(self):
        pass

    @property
    def api_endpoint(self) -> str:
        return self._api_endpoint
    
    @property
    def branch(self) -> str:
        return self._branch

    @property
    def headers(self) -> dict:
        return self._headers

    def with_parameters(self, url: str, parameters: dict = {}):
        if len(parameters.keys()) >= 1:
            url += "?"

        for parameter, value in parameters.items():
            if type(value) == str:
                parameter_str = "%s=%s&" % (parameter, value)
            elif type(value) == bool:
                parameter_str = "%s=%s&" % (parameter, str(value).lower())
            elif type(value) == int:
                parameter_str = "%s=%s&" % (parameter, str(value))

            url += parameter_str
        return url

    def set_api_endpoint(self, api_url: str,) -> None:
        if not api_url.endswith("/"):
            api_url += "/"
        self._api_endpoint = api_url

    def set_branch(self, branch: str) -> None:
        self._branch = branch

    def set_headers(self, headers: dict) -> None:
        self._headers.update(headers)

    @property
    def base_branch_url(self) -> str:
        return self.api_endpoint + "branches/"

    @property
    def branch_url(self) -> str:
        return self.base_branch_url + "%s" % (str(self.branch))
