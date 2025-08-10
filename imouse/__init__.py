from imouse.api import API
from imouse.helper import Helper


def api(host: str = "localhost"):
    return API(host)


def helper(api: API):
    return Helper(api)


__all__ = ["api", "helper"]
