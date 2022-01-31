# <img src="https://svgshare.com/i/dke.svg" align="right" width="180px" />SCTTSRApy: Python Interface to the SNOMED CT Snowstorm Terminology Server REST API


[![GitHub commits](https://badgen.net/github/commits/AberystwythSystemsBiology/SCTTSRApy/main)](https://GitHub.com/AberystwythSystemsBiology/SCTTSRApy/main/commit/)
![GitHub issues](https://img.shields.io/github/issues/AberystwythSystemsBiology/SCTTSRApy)
![GitHub repo size](https://img.shields.io/github/repo-size/AberystwythSystemsBiology/SCTTSRApy)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

Interrogate the SNOMED CT clinical ontology using the SNOMED International Terminology Server REST API.


## Installing

You can install the development version directly from GitHub with:

```
pip install git+https://github.com/AberystwythSystemsBiology/SCTTSRApy
```

## Features

We currently support the following API endpoints:

- Branching
- Code Systems
- Concepts
- Descriptions
- Relationships

## Example

Retrieve all children of `363908000`:

```python
>>> from scttsrapy.concepts import get_concept_children
>>> get_concept_children("363908000")
{
    "success": true,
    "content": [
        {
            "conceptId": "763699005",
            "active": true,
            "definitionStatus": "PRIMITIVE",
            "moduleId": "900000000000207008",
            "fsn": {
                "term": "Clinical Opiate Withdrawal Scale score (observable entity)",
                "lang": "en"
            },
            "pt": {
                "term": "Clinical Opiate Withdrawal Scale score",
                "lang": "en"
            },
            "isLeafInferred": true,
            "id": "763699005"
        },
        ...
    ]
}
>>>
```

If you're using a custom Snowstorm instance, you can easily configure a custom `endpoint_builder`:

```python
>>> from scttsrapy.api import EndpointBuilder
>>> endpoint_builder = EndpointBuilder()
>>> # Setting up the custom API endpoint
>>> endpoint_builder.set_api_endpoint("localhost:9000)
>>> # Setting up a custom header. In reality this isn't going to do anything, but you may want to lock your Snowstorm API behind a JWT.
>>> endpoint_builder.set_headers(
....{
....    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
....})
>>> get_concept_children("363908000", endpoint_builder=endpoint_builder)
{
    ...
}
```

## Bug reporting and feature suggestions

Please report all bugs or feature suggestions to the [issues tracker](https://www.github.com/AberystwythSystemsBiology/SCTTSRApy/issues). Please do not email me directly as I'm struggling to keep track of what needs to be fixed.

We welcome all sorts of contribution, so please be as candid as you want.

## Terms & conditions

### Server endpoint

By default, `SCTTSRApy` queries the public SNOMED CT terminology endpoint hosted by SNOMED International.

This server has no service level agreement and **MUST NOT be used as part of production systems in healthcare settings**, even if you hold a SNOMED CT licence.

Please refer to the [Snowstorm documentation](https://github.com/IHTSDO/snowstorm/blob/master/docs/getting-started.md) for instructions on how to build a dedicated SNOMED endpoint for production.

### SNOMED CT Terminology

In order to use SNOMED CT terminology, a licence is required which depends both on the country you are based in, and the purpose of your work.

SNOMED International maintains a public SNOMED CT terminology server for strict ‘reference purposes’ under the [SNOMED International SNOMED CT Browser License Agreement](https://browser.ihtsdotools.org/).

Use of SNOMED CT terminology for data analysis or health care production systems is subject to other licences. Some users are eligible for free licences:

- UK-based users can obtain a licence free of charge on the [NHS TRUD website](https://isd.digital.nhs.uk/trud/users/guest/filters/0/home).
- residents of other Member Countries and low-income countries are also eligible. More information can be found on the [SNOMED International website](https://www.snomed.org/snomed-ct/get-snomed).

## License

This project is proudly licensed under the [GNU General Public License v3.0](https://raw.githubusercontent.com/AberystwythSystemsBiology/SCTTSRApy/main/LICENSE).
