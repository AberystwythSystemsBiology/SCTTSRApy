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


def search_concept_descriptions(
    term: str,
    active: bool = False,
    module: list = [],
    language: list = [],
    type: list = [],
    semantic_tags: list = [],
    preferred_in: list = [],
    acceptable_in: list = [],
    preferred_or_acceptable_in: list = [],
    concept_active: bool = None,
    group_by_concept: bool = False,
    search_mode: str = "standard",
    offset: int = 0,
    limit: int = 50,
    **kwargs,
) -> dict:
    """Search for concept descriptions.

    Args:
        term (str): term.
        active (bool, optional): active. Defaults to False.
        module (list, optional): List of modules. Defaults to [].
        language (list, optional): The Accept-Language header is used to specify the user's preferred language, 'en' is always added as a fallback if not already included in the list.. Defaults to [].
        type (list, optional): Set of description type ids to use include. Defaults to [].
        semantic_tags (list, optional): Set of semantic tags. Defaults to [].
        preferred_in (list, optional): Set of description language reference sets. The description must be preferred in at least one of these to match. Defaults to [].
        acceptable_in (list, optional): Set of description language reference sets. The description must be acceptable in at least one of these to match. Defaults to [].
        preferred_or_acceptable_in (list, optional): Set of description language reference sets. The description must be preferred OR acceptable in at least one of these to match. Defaults to [].
        concept_active (bool, optional): conceptActive. Defaults to None.
        group_by_concept (bool, optional): groupByConcept.  Defaults to False.
        search_mode (str, optional): searchMode. One of standard, regex or whole_word. Defaults to "standard".
        offset (int, optional): offset. Defaults to 0.
        limit (int, optional): limit. Defaults to 50.

    Raises:
        Exception: If one of standard, regex or whole_word is not search_mode as form, an exception is thrown.

    Returns:
        dict: Model.
    """    
    if "endpoint_builder" not in kwargs:
        endpoint_builder = EndpointBuilder()
    else:
        endpoint_builder = kwargs["endpoint_builder"]

    search_modes = ["standard", "regex", "whole_word"]

    if search_mode.lower() not in search_modes:
        raise Exception(
            "search_mode %s is not one of %s"
            % (search_mode.lower(), ",".join(search_modes))
        )

    url = endpoint_builder.with_parameters(
        endpoint_builder.api_endpoint
        + "browser/%s/descriptions" % (endpoint_builder.branch),
        parameters={
            "term": term,
            "active": active,
            "language": language,
            "type": type,
            "offset": offset,
            "limit": limit,
            "semanticTags": semantic_tags,
            "preferredIn": preferred_in,
            "module": module,
            "acceptableIn": acceptable_in,
            "prefferedOrAcceptableIn": preferred_or_acceptable_in,
            "conceptActive": concept_active,
            "groupByConcept": group_by_concept,
            "searchMode": search_mode.upper(),
        },
    )

    response = requests.get(url, headers=endpoint_builder.headers)

    if response.status_code == 200:
        return {"success": True, "content": response.json()}
    else:
        return {"success": False, "content": response.content}


def find_descriptions(
    concept_ids: list, offset: int = 0, limit: int = 50, **kwargs
) -> dict:
    if "endpoint_builder" not in kwargs:
        endpoint_builder = EndpointBuilder()
    else:
        endpoint_builder = kwargs["endpoint_builder"]

    url = endpoint_builder.with_parameters(
        endpoint_builder.base_descriptions_url,
        parameters={"conceptIds": concept_ids, "offset": offset, "limit": limit},
    )

    response = requests.get(url, headers=endpoint_builder.headers)

    if response.status_code == 200:
        return {"success": True, "content": response.json()}

    else:
        return {"success": False, "content": response.content}


def list_semantic_tags(**kwargs) -> dict:
    if "endpoint_builder" not in kwargs:
        endpoint_builder = EndpointBuilder()
    else:
        endpoint_builder = kwargs["endpoint_builder"]

    response = requests.get(
        endpoint_builder.base_descriptions_url + "/semantictags",
        headers=endpoint_builder.headers,
    )

    if response.status_code == 200:
        return {"success": True, "content": response.json()}
    else:
        return {"success": False, "content": response.content}


def fetch_description(description_id: str, **kwargs) -> dict:
    if "endpoint_builder" not in kwargs:
        endpoint_builder = EndpointBuilder()
    else:
        endpoint_builder = kwargs["endpoint_builder"]

    response = requests.get(
        endpoint_builder.base_descriptions_url + "/%s" % (description_id),
        headers=endpoint_builder.headers,
    )

    if response.status_code == 200:
        return {"success": True, "content": response.json()}
    else:
        return {"success": False, "content": response.content}
