from api.github import get_all_content, get_avatar_url, get_blog, get_login, get_url
from tests.conftest import _get_content_mocked


def test_all_content(mocked_responses) -> None:
    """Function that checks the return of the simulated data in
       the conftest file are the same as the return of the API.
    
    Arguments:
        mocked_responses {Dict} -- If equal to "Https.Ok" returns simulated data.
    """
    user = "alisonamerico"
    assert get_all_content(user) == _get_content_mocked


def test_login(mocked_responses) -> None:
    """Function that checks if the informed user is the same as the one in the github API.
    
    Arguments:
        mocked_responses {str} -- Return user
    """
    assert get_login("alisonamerico") == "alisonamerico"


def test_get_avatar_url(mocked_responses) -> None:
    """Function that checks if the informed avatar_url is the same as the one in the github API.
    
    Arguments:
        mocked_responses {str} -- Return avatar_url
    """
    assert (
        get_avatar_url("alisonamerico")
        == "https://avatars0.githubusercontent.com/u/13425415?v=4"
    )


def test_get_url(mocked_responses) -> None:
    """Function that checks if the informed url is the same as the one in the github API.
    
    Arguments:
        mocked_responses {str} -- Return url
    """
    assert get_url("alisonamerico") == "https://api.github.com/users/alisonamerico"


def test_get_blog(mocked_responses) -> None:
    """Function that checks if the informed blog is the same as the one in the github API.
    
    Arguments:
        mocked_responses {str} -- Return blog
    """
    assert get_blog("alisonamerico") == "https://alisonamerico.github.io/"
