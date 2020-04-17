from typing import Any, Dict
import requests
from http import HTTPStatus


def get_all_content(user: str) -> Any:
    """Function that makes request in the github API.
    
    Arguments:
        user {str} -- Specifies the name of the user who should return the data.
    
    Returns:
        Any -- returns API data.
    """
    try:
        if HTTPStatus.OK:
            resp = requests.get(f"https://api.github.com/users/{user}")
            js = resp.json()
            return js
    except ValueError as e:
        print(e)


def get_login(user: str) -> str:
    """Function requests login
    
    Arguments:
        user {str} -- Specifies the name of the user who should return the data.
    
    Returns:
        str -- Return login
    """
    return get_all_content(user)["login"]


def get_avatar_url(user: str) -> str:
    """Function requests avatar_url
    
    Arguments:
        user {str} -- Specifies the name of the user who should return the data.
    
    Returns:
        str -- Return avatar_url
    """
    return get_all_content(user)["avatar_url"]


def get_url(user: str) -> str:
    """Function requests url
    
    Arguments:
        user {str} -- Specifies the name of the user who should return the data.
    
    Returns:
        str -- Return url
    """
    return get_all_content(user)["url"]


def get_blog(user: str) -> str:
    """Function requests blog
    
    Arguments:
        user {str} -- Specifies the name of the user who should return the data.
    
    Returns:
        str -- Return blog
    """
    return get_all_content(user)["blog"]


if __name__ == "__main__":
    user = input("Enter the username: ")
    print(get_all_content(user))
