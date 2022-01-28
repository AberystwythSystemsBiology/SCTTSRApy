import requests
from .api import EndpointBuilder


def find_concepts_term(
    term: str,
    term_active: bool = True,
    language: str = "en",
    return_id_only: bool = False,
    offset: int = 0,
    limit: int = 50,
    search_after: int = None,
    is_published: bool = True,
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
            "module": module
        }
    )

    response = requests.get(url, headers=endpoint_builder.headers)

    if response.status_code == 200:
        return {"success": True, "content": response.json()}
    else:
        return {"success": False, "content": response.content}


def find_concepts_concept_id(

):
    pass