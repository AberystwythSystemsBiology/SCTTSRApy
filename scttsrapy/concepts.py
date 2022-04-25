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


def find_concepts_term(
    term: str,
    term_active: bool = None,
    language: str = "en",
    return_id_only: bool = None,
    offset: int = 0,
    limit: int = 50,
    search_after: int = None,
    is_published: bool = None,
    module: list = [],
    **kwargs
) -> dict:
    """Find a concept using the term.

    Args:
        term (str): Search term to match against concept descriptions using a case-insensitive multi-prefix matching strategy.
        term_active (bool, optional): termActive. Defaults to None.
        language (str, optional): Set of two character language codes to match. Defaults to "en".
        return_id_only (bool, optional): returnIdOnly. Defaults to None.
        offset (int, optional): offset. Defaults to 0.
        limit (int, optional): limit. Defaults to 50.
        search_after (int, optional): searchAfter. Defaults to None.
        is_published (bool, optional): isPublished. Defaults to None.
        module (list, optional): Set of module ids to filter concepts by. Defaults to any. Defaults to [].

    Returns:
        dict: Model.
    """
    if "endpoint_builder" not in kwargs:
        endpoint_builder = EndpointBuilder()
    else:
        endpoint_builder = kwargs["endpoint_builder"]

    url = endpoint_builder.with_parameters(
        endpoint_builder.base_concept_url,
        parameters={
            "term": term,
            "termActive": term_active,
            "language": language,
            "returnIdOnly": return_id_only,
            "offset": offset,
            "limit": limit,
            "searchAfter": search_after,
            "isPublished": is_published,
            "module": module,
        },
    )

    response = requests.get(url, headers=endpoint_builder.headers)

    if response.status_code == 200:
        return {"success": True, "content": response.json()}
    else:
        return {"success": False, "content": response.content}


def find_concepts_concept_id(
    concept_ids: list = [],
    term_active: bool = None,
    language: str = "en",
    return_id_only: bool = None,
    offset: int = 0,
    limit: int = 50,
    search_after: int = None,
    is_published: bool = None,
    module: list = [],
    **kwargs
) -> dict:
    """Find concept using concept ID.

    Args:
        concept_ids (list, optional): List of cuids. Defaults to [].
        term_active (bool, optional): termActive. Defaults to None.
        language (str, optional): Set of two character language codes to match. Defaults to "en".
        return_id_only (bool, optional): returnIdOnly. Defaults to None.
        offset (int, optional): offset. Defaults to 0.
        limit (int, optional): limit. Defaults to 50.
        search_after (int, optional): searchAfter. Defaults to None.
        is_published (bool, optional): isPublished. Defaults to None.
        module (list, optional): Set of module ids to filter concepts by. Defaults to any. Defaults to []

    Returns:
        dict: Model.
    """
    if "endpoint_builder" not in kwargs:
        endpoint_builder = EndpointBuilder()
    else:
        endpoint_builder = kwargs["endpoint_builder"]

    url = endpoint_builder.with_parameters(
        endpoint_builder.base_concept_url,
        parameters={
            "conceptIds": concept_ids,
            "termActive": term_active,
            "language": language,
            "returnIdOnly": return_id_only,
            "offset": offset,
            "limit": limit,
            "searchAfter": search_after,
            "isPublished": is_published,
            "module": module,
        },
    )

    response = requests.get(url, headers=endpoint_builder.headers)

    if response.status_code == 200:
        return {"success": True, "content": response.json()}
    else:
        return {"success": False, "content": response.content}


def get_concept(concept_id: str, **kwargs) -> dict:
    """Find concept

    Args:
        concept_id (str): Concept ID.

    Returns:
        dict: Model.
    """
    if "endpoint_builder" not in kwargs:
        endpoint_builder = EndpointBuilder()
    else:
        endpoint_builder = kwargs["endpoint_builder"]

    url = endpoint_builder.base_concept_url + "/%s" % (concept_id)

    response = requests.get(url, headers=endpoint_builder.headers)

    if response.status_code == 200:
        return {"success": True, "content": response.json()}
    else:
        return {"success": False, "content": response.content}


def _get_concept_misc(concept_id: str, req: str, endpoint_builder) -> dict:

    url = endpoint_builder.base_concept_url + "/%s/%s" % (concept_id, req)

    response = requests.get(url, headers=endpoint_builder.headers)

    if response.status_code == 200:
        return {"success": True, "content": response.json()}
    else:
        return {"success": False, "content": response.content}


def get_concept_authoring_form(concept_id: str, **kwargs) -> dict:
    """Get Concept Authoring Form.

    Args:
        concept_id (str): Concept ID.

    Returns:
        dict: Model
    """
    if "endpoint_builder" not in kwargs:
        endpoint_builder = EndpointBuilder()
    else:
        endpoint_builder = kwargs["endpoint_builder"]

    return _get_concept_misc(concept_id, "authoring-form", endpoint_builder)


def get_concept_descriptions(concept_id: str, **kwargs) -> dict:
    """Get Concept Descriptions.

    Args:
        concept_id (str): Concept ID.

    Returns:
        dict: Model
    """
    if "endpoint_builder" not in kwargs:
        endpoint_builder = EndpointBuilder()
    else:
        endpoint_builder = kwargs["endpoint_builder"]

    return _get_concept_misc(concept_id, "descriptions", endpoint_builder)


def get_concept_inbound_relationships(concept_id: str, **kwargs) -> dict:
    """Get Concept Inbound Relationships.

    Args:
        concept_id (str): Concept ID.

    Returns:
        dict: Model
    """
    if "endpoint_builder" not in kwargs:
        endpoint_builder = EndpointBuilder()
    else:
        endpoint_builder = kwargs["endpoint_builder"]

    return _get_concept_misc(concept_id, "inbound-relationships", endpoint_builder)


def get_concept_descendants(
    concept_id: str, stated: bool = False, offset: int = 0, limit: int = 50, **kwargs
) -> dict:
    """Get Concept Descendants.

    Args:
        concept_id (str): Concept ID.
        stated (bool, optional): stated. Defaults to False.
        offset (int, optional): offset. Defaults to 0.
        limit (int, optional): limit. Defaults to 50.

    Returns:
        dict: Model.
    """
    if "endpoint_builder" not in kwargs:
        endpoint_builder = EndpointBuilder()
    else:
        endpoint_builder = kwargs["endpoint_builder"]

    url = endpoint_builder.with_parameters(
        endpoint_builder.base_concept_url + "/%s/%s" % (concept_id, "descendants"),
        parameters={"stated": stated, "offset": offset, "limit": limit},
    )

    response = requests.get(url, headers=endpoint_builder.headers)

    if response.status_code == 200:
        return {"success": True, "content": response.json()}
    else:
        return {"success": False, "content": response.content}

def get_concept_ancestors(
    concept_id: str,
    form: str = "inferred",
    **kwargs
) -> dict:
    """Find Concept Ancestors

    Args:
        concept_id (str):  Concept ID.
        form (str, optional): form. One of inferred, stated or additional. Defaults to "inferred".

    Returns:
        dict: Model.
    """
    if "endpoint_builder" not in kwargs:
        endpoint_builder = EndpointBuilder()
    else:
        endpoint_builder = kwargs["endpoint_builder"]

    forms = ["inferred", "stated", "additional"]

    if form.lower() not in forms:
        raise Exception("form %s not one of %s" % (form, ",".join(forms)))

    url = endpoint_builder.with_parameters(
        endpoint_builder.browser_concept_url + "/%s/%s" % (concept_id, "ancestors"),
        parameters={"form": form},
    )

    response = requests.get(url, headers=endpoint_builder.headers)

    if response.status_code == 200:
        return {"success": True, "content": response.json()}
    else:
        return {"success": False, "content": response.content}


def get_concept_normal_form(
    concept_id: str, stated_view: bool = False, include_terms: bool = False, **kwargs
) -> dict:
    """Get concept normal form.

    Args:
        concept_id (str): Concept ID.
        stated_view (bool, optional): statedView. Defaults to False.
        include_terms (bool, optional): includeTerms. Defaults to False.

    Returns:
        dict: Model.
    """
    if "endpoint_builder" not in kwargs:
        endpoint_builder = EndpointBuilder()
    else:
        endpoint_builder = kwargs["endpoint_builder"]

    url = endpoint_builder.with_parameters(
        endpoint_builder.base_concept_url + "/%s/%s" % (concept_id, "normal-form"),
        parameters={"statedView": stated_view, "includeTerms": include_terms},
    )

    response = requests.get(url, headers=endpoint_builder.headers)

    if response.status_code == 200:
        return {"success": True, "content": response.json()}
    else:
        return {"success": False, "content": response.content}


def get_concept_relationships(
    concept_id: str, stated: bool = False, offset: int = 0, limit: int = 1000, **kwargs
) -> dict:
    """Find concepts which reference this concept in the inferred or stated form (including stated axioms).

    Args:
        concept_id (str): Concept IDs
        stated (bool, optional): stated. Defaults to False.
        offset (int, optional): offset. Defaults to 0.
        limit (int, optional): limit. Defaults to 1000.

    Returns:
        dict: Model.
    """
    if "endpoint_builder" not in kwargs:
        endpoint_builder = EndpointBuilder()
    else:
        endpoint_builder = kwargs["endpoint_builder"]

    url = endpoint_builder.with_parameters(
        endpoint_builder.base_concept_url + "/%s/%s" % (concept_id, "references"),
        parameters={"stated": stated, "offset": offset, "limit": limit},
    )

    response = requests.get(url, headers=endpoint_builder.headers)

    if response.status_code == 200:
        return {"success": True, "content": response.json()}
    else:
        return {"success": False, "content": response.content}


def get_concept_children(
    concept_id: str,
    form: str = "inferred",
    include_descendant_count: bool = False,
    **kwargs
) -> dict:
    """findConceptChildren

    Args:
        concept_id (str): Concept ID.
        form (str, optional): form. One of inferred, stated or additional. Defaults to "inferred".
        include_descendant_count (bool, optional): includeDescendantCount. Defaults to False.

    Raises:
        Exception: If one of inferred, stated or additional is not passed as form, an exception is thrown.

    Returns:
        dict: Model.
    """

    if "endpoint_builder" not in kwargs:
        endpoint_builder = EndpointBuilder()
    else:
        endpoint_builder = kwargs["endpoint_builder"]

    forms = ["inferred", "stated", "additional"]

    if form.lower() not in forms:
        raise Exception("form %s not one of %s" % (form, ",".join(forms)))

    url = endpoint_builder.with_parameters(
        endpoint_builder.browser_concept_url + "/%s/%s" % (concept_id, "children"),
        parameters={"form": form, "includeDescendantCount": include_descendant_count},
    )

    response = requests.get(url, headers=endpoint_builder.headers)

    if response.status_code == 200:
        return {"success": True, "content": response.json()}
    else:
        return {"success": False, "content": response.content}


def get_concept_parents(
    concept_id: str,
    form: str = "inferred",
    include_descendant_count: bool = False,
    **kwargs
) -> dict:
    """findConceptParents

    Args:
        concept_id (str): Concept ID.
        form (str, optional): form. One of inferred, stated or additional. Defaults to "inferred".
        include_descendant_count (bool, optional): includeDescendantCount. Defaults to False.

    Raises:
        Exception: If one of inferred, stated or additional is not passed as form, an exception is thrown.

    Returns:
        dict: Model.
    """
    if "endpoint_builder" not in kwargs:
        endpoint_builder = EndpointBuilder()
    else:
        endpoint_builder = kwargs["endpoint_builder"]

    forms = ["inferred", "stated", "additional"]

    if form.lower() not in forms:
        raise Exception("form %s not one of %s" % (form, ",".join(forms)))

    url = endpoint_builder.with_parameters(
        endpoint_builder.browser_concept_url + "/%s/%s" % (concept_id, "parents"),
        parameters={"form": form, "includeDescendantCount": include_descendant_count},
    )

    response = requests.get(url, headers=endpoint_builder.headers)

    if response.status_code == 200:
        return {"success": True, "content": response.json()}
    else:
        return {"success": False, "content": response.content}
