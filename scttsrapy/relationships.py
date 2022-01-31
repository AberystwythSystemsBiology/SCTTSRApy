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

import requests
from .api import EndpointBuilder


def find_relationship(
    active: bool = None,
    module: str = None,
    effective_time: str = None,
    source: str = None,
    relationship_type: str = None,
    destination: str = None,
    characteristic_type: str = None,
    group: str = None,
    offset: int = 0,
    limit: int = 50,
    **kwargs
) -> dict:
    if "endpoint_builder" not in kwargs:
        endpoint_builder = EndpointBuilder()
    else:
        endpoint_builder = kwargs["endpoint_builder"]

    url = endpoint_builder.with_parameters(
        endpoint_builder.base_relationships_url,
        parameters={
            "active": active,
            "module": module,
            "effective_time": effective_time,
            "source": source,
            "type": relationship_type,
            "destination": destination,
            "characteristicType": characteristic_type,
            "group": group,
            "offset": offset,
            "limit": limit,
        },
    )

    response = requests.get(url, headers=endpoint_builder.headers)

    if response.status_code == 200:
        return {"success": True, "content": response.json()}
    else:
        return {"success": False, "content": response.content}


def fetch_relationship(relationship_id: str, **kwargs) -> dict:
    if "endpoint_builder" not in kwargs:
        endpoint_builder = EndpointBuilder()
    else:
        endpoint_builder = kwargs["endpoint_builder"]

    response = requests.get(
        endpoint_builder.base_relationships_url + "/%s" % (relationship_id),
        headers=endpoint_builder.headers,
    )

    if response.status_code == 200:
        return {"success": True, "content": response.json()}
    else:
        return {"success": False, "content": response.content}
