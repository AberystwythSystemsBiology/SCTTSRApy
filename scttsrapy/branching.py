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


def single_branch(branch: str, includeInheritedMetadata: bool = False, **kwargs):
    if "endpoint_builder" not in kwargs:
        endpoint_builder = EndpointBuilder()
    else:
        endpoint_builder = kwargs["endpoint_builder"]
    endpoint_builder.set_branch(branch)

    url = endpoint_builder.with_parameters(
        endpoint_builder.branch_url,
        parameters={"includeInheritedMetadata": includeInheritedMetadata},
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
