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
):
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
):
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


def get_concept(concept_id: str, **kwargs):
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


def _get_concept_misc(concept_id: str, req: str, endpoint_builder):

    url = endpoint_builder.base_concept_url + "/%s/%s" % (concept_id, req)

    response = requests.get(url, headers=endpoint_builder.headers)

    if response.status_code == 200:
        return {"success": True, "content": response.json()}
    else:
        return {"success": False, "content": response.content}


def get_concept_authoring_form(concept_id: str, **kwargs):
    if "endpoint_builder" not in kwargs:
        endpoint_builder = EndpointBuilder()
    else:
        endpoint_builder = kwargs["endpoint_builder"]

    return _get_concept_misc(concept_id, "authoring-form", endpoint_builder)


def get_concept_descriptions(concept_id: str, **kwargs):
    if "endpoint_builder" not in kwargs:
        endpoint_builder = EndpointBuilder()
    else:
        endpoint_builder = kwargs["endpoint_builder"]

    return _get_concept_misc(concept_id, "descriptions", endpoint_builder)


def get_concept_inbound_relationships(concept_id: str, **kwargs):
    if "endpoint_builder" not in kwargs:
        endpoint_builder = EndpointBuilder()
    else:
        endpoint_builder = kwargs["endpoint_builder"]

    return _get_concept_misc(concept_id, "inbound-relationships", endpoint_builder)


def get_concept_descendants(
    concept_id: str, stated: bool = False, offset: int = 0, limit: int = 50, **kwargs
):

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


def get_concept_normal_form(
    concept_id: str, stated_view: bool = False, include_terms: bool = False, **kwargs
):
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
):

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
    **kwargs):
    
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
    **kwargs):
    
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