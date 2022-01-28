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


def all_branches(**kwargs):
    if "endpoint_builder" not in kwargs:
        endpoint_builder = EndpointBuilder()
    else:
        endpoint_builder = kwargs["endpoint_builder"]

    response = requests.get(
        endpoint_builder.base_branch_url, headers=endpoint_builder.headers
    )

    if response.status_code == 200:
        return {"success": True, "content": response.json()}
    else:
        return {"success": False, "content": response.content}


def single_branch(branch: str, include_inherited_metadata: bool = False, **kwargs):
    if "endpoint_builder" not in kwargs:
        endpoint_builder = EndpointBuilder()
    else:
        endpoint_builder = kwargs["endpoint_builder"]
    endpoint_builder.set_branch(branch)

    url = endpoint_builder.with_parameters(
        endpoint_builder.branch_url,
        parameters={"includeInheritedMetadata": include_inherited_metadata},
    )

    response = requests.get(url, headers=endpoint_builder.headers)

    if response.status_code == 200:
        return {"success": True, "content": response.json()}
    else:
        return {"success": False, "content": response.content}


def branch_children(
    branch: str,
    immediateChildren: bool = True,
    page: int = 0,
    size: int = 100,
    **kwargs
):
    if "endpoint_builder" not in kwargs:
        endpoint_builder = EndpointBuilder()
    else:
        endpoint_builder = kwargs["endpoint_builder"]

    endpoint_builder.set_branch(branch)

    url = endpoint_builder.with_parameters(
        endpoint_builder.branch_url + "/children",
        parameters={"immediateChildren": immediateChildren, "page": page, "size": size},
    )

    response = requests.get(url, headers=endpoint_builder.headers)

    if response.status_code == 200:
        return {"success": True, "content": response.json()}
    else:
        return {"success": False, "content": response.content}
