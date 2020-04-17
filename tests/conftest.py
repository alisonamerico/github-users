"""
Fixtures - are functions, which will run before each test function to which it is applied. 
Fixtures are used to feed some data to the tests such as database connections, 
URLs to test and some sort of input data. Therefore, instead of running the same code for
every test, we can attach fixture function to the tests and it will run and return the data
to the test before executing each test.

However, the approach comes with its own limitation. A fixture function defined inside atest
file has a scope within the test file only. We cannot use that fixture in another test file.
To make a fixture available to multiple test files, we have to define the fixture function in
a file called conftest.py.

Conftest - Provides a fixture available to multiple test files.
"""

import json
from http import HTTPStatus

import pytest
import requests
import responses

_get_content_mocked = json.loads(
    """{
  "login": "alisonamerico",
  "id": 13425415,
  "node_id": "MDQ6VXNlcjEzNDI1NDE1",
  "avatar_url": "https://avatars0.githubusercontent.com/u/13425415?v=4",
  "gravatar_id": "",
  "url": "https://api.github.com/users/alisonamerico",
  "html_url": "https://github.com/alisonamerico",
  "followers_url": "https://api.github.com/users/alisonamerico/followers",
  "following_url": "https://api.github.com/users/alisonamerico/following{/other_user}",
  "gists_url": "https://api.github.com/users/alisonamerico/gists{/gist_id}",
  "starred_url": "https://api.github.com/users/alisonamerico/starred{/owner}{/repo}",
  "subscriptions_url": "https://api.github.com/users/alisonamerico/subscriptions",
  "organizations_url": "https://api.github.com/users/alisonamerico/orgs",
  "repos_url": "https://api.github.com/users/alisonamerico/repos",
  "events_url": "https://api.github.com/users/alisonamerico/events{/privacy}",
  "received_events_url": "https://api.github.com/users/alisonamerico/received_events",
  "type": "User",
  "site_admin": false,
  "name": "Alison Américo",
  "company": null,
  "blog": "https://alisonamerico.github.io/",
  "location": "Recife, Brasil",
  "email": null,
  "hireable": null,
  "bio": "Python Developer.\\r\\nSmall steps to a development with quality. ",
  "public_repos": 59,
  "public_gists": 23,
  "followers": 15,
  "following": 2,
  "created_at": "2015-07-20T22:29:30Z",
  "updated_at": "2020-04-10T15:44:58Z"
}"""
)


@pytest.fixture
def mocked_responses():
    """simulates the return of requests, using lib responses.
       This avoids repeatedly accessing the API.
    
    Yields:
        [type] -- Returns simulated data from json "_get_content_mocked".
    """
    with responses.RequestsMock() as rsps:
        rsps.add(
            responses.GET,
            "https://api.github.com/users/alisonamerico",
            json=_get_content_mocked,
        )
        resp = requests.get("https://api.github.com/users/alisonamerico")
        assert resp.status_code == HTTPStatus.OK
        yield rsps

    # outside the context manager requests will hit the remote server
    resp = requests.get("https://api.github.com/users/alisonamerico")
    resp.status_code == HTTPStatus.OK
