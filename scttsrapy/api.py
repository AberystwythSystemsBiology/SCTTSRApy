# Copyright (C) 2022 Keiron O'Shea <keiron@fastmail.co.uk>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


class EndpointBuilder:
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
            parse = False
            if type(value) == str:
                parameter_str = "%s=%s&" % (parameter, value)
                parse = True
            elif type(value) == bool:
                parameter_str = "%s=%s&" % (parameter, str(value).lower())
                parse = True
            elif type(value) == int:
                parameter_str = "%s=%s&" % (parameter, str(value))
                parse = True
            elif type(value) == list and len(value) > 0:
                parameter_str = ""
                for entry in value:
                    parameter_str += "%s=%s&" % (parameter, str(entry))
                parse = True
            elif type(value) == None:
                pass

            if parse:
                url += parameter_str

        return url

    def set_api_endpoint(
        self,
        api_url: str,
    ) -> None:
        if not api_url.endswith("/"):
            api_url += "/"
        self._api_endpoint = api_url

    def set_branch(self, branch: str) -> None:
        self._branch = branch

    def set_headers(self, headers: dict) -> None:
        self._headers.update(headers)

    # SNOWSTORM ENTITIES

    ## branching.py

    @property
    def base_branch_url(self) -> str:
        return self.api_endpoint + "branches/"

    @property
    def branch_url(self) -> str:
        return self.base_branch_url + "%s" % (str(self.branch))

    ## code_systems.py

    @property
    def base_code_system_url(self) -> str:
        return self.api_endpoint + "codesystems/"

    def generate_code_system_url(self, short_name: str) -> str:
        return self.base_code_system_url + "%s" % (short_name)

    ## concepts.py

    @property
    def base_concept_url(self) -> str:
        return self.api_endpoint + self.branch + "/concepts"

    @property
    def browser_concept_url(self) -> str:
        return self.api_endpoint + "browser/" + self.branch + "/concepts"
