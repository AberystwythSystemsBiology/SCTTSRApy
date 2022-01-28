import requests
from .api import EndpointBuilder

def all_code_systems(for_branch: str = None, **kwargs):
    if "endpoint_builder" not in kwargs:
        endpoint_builder = EndpointBuilder()
    else:
        endpoint_builder = kwargs["endpoint_builder"]

    if for_branch == None:
        for_branch = endpoint_builder.branch

    url = endpoint_builder.with_parameters(
        endpoint_builder.base_code_system_url,
        parameters={"for_branch": for_branch}
    )
    
    response = requests.get(
        url,
        headers=endpoint_builder.headers
    )

    if response.status_code == 200:
        return {"success": True, "content": response.json()}
    else:
        return {"success": False, "content": response.content}


def code_system(short_name: str, **kwargs):
    if "endpoint_builder" not in kwargs:
        endpoint_builder = EndpointBuilder()
    else:
        endpoint_builder = kwargs["endpoint_builder"]

    response = requests.get(
        endpoint_builder.generate_code_system_url(short_name),
        headers=endpoint_builder.headers
    )

    if response.status_code == 200:
        return {"success": True, "content": response.json()}
    else:
        return {"success": False, "content": response.content}


def code_system_versions(short_name: str,  showFutureFVersions: bool = False,  showInternalReleases: bool = False, **kwargs):
    if "endpoint_builder" not in kwargs:
        endpoint_builder = EndpointBuilder()
    else:
        endpoint_builder = kwargs["endpoint_builder"]
    
    url = endpoint_builder.with_parameters(
        endpoint_builder.generate_code_system_url(short_name) + "/versions",
        parameters={
            "showFutureFVersions": showFutureFVersions,
            "showInternalReleases": showInternalReleases,
        }
    )

    response = requests.get(
        url,
        headers=endpoint_builder.headers
    )

    if response.status_code == 200:
        return {"success": True, "content": response.json()}
    else:
        return {"success": False, "content": response.content}