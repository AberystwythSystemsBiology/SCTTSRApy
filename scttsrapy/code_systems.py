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


def all_code_systems(for_branch: str = None, **kwargs) -> dict:
    """List all code systems. for_branch is an optional parameter to find the code system which the specified branch is within.

    Args:
        for_branch (str, optional): forBranch. Defaults to None.

    Returns:
        dict: Model
    """
    if "endpoint_builder" not in kwargs:
        endpoint_builder = EndpointBuilder()
    else:
        endpoint_builder = kwargs["endpoint_builder"]

    if for_branch == None:
        for_branch = endpoint_builder.branch

    url = endpoint_builder.with_parameters(
        endpoint_builder.base_code_system_url, parameters={"for_branch": for_branch}
    )

    response = requests.get(url, headers=endpoint_builder.headers)

    if response.status_code == 200:
        return {"success": True, "content": response.json()}
    else:
        return {"success": False, "content": response.content}


def code_system(short_name: str, **kwargs) -> dict:
    """Retrieve a code system.

    Args:
        short_name (str): Code system short name.

    Returns:
        dict: Model
    """
    if "endpoint_builder" not in kwargs:
        endpoint_builder = EndpointBuilder()
    else:
        endpoint_builder = kwargs["endpoint_builder"]

    response = requests.get(
        endpoint_builder.generate_code_system_url(short_name),
        headers=endpoint_builder.headers,
    )

    if response.status_code == 200:
        return {"success": True, "content": response.json()}
    else:
        return {"success": False, "content": response.content}


def code_system_versions(
    short_name: str,
    show_future_f_versions: bool = False,
    show_internal_releases: bool = False,
    **kwargs
) -> dict:
    """Retrieve versions of a code system.

    Args:
        short_name (str): Code system short name.
        show_future_f_versions (bool, optional): Should versions with a future effective-time be shown. Defaults to False.
        show_internal_releases (bool, optional): Should versions marked as 'internalRelease' be shown. Defaults to False.

    Returns:
        dict: Model
    """

    if "endpoint_builder" not in kwargs:
        endpoint_builder = EndpointBuilder()
    else:
        endpoint_builder = kwargs["endpoint_builder"]

    url = endpoint_builder.with_parameters(
        endpoint_builder.generate_code_system_url(short_name) + "/versions",
        parameters={
            "showFutureFVersions": show_future_f_versions,
            "showInternalReleases": show_internal_releases,
        },
    )

    response = requests.get(url, headers=endpoint_builder.headers)

    if response.status_code == 200:
        return {"success": True, "content": response.json()}
    else:
        return {"success": False, "content": response.content}
