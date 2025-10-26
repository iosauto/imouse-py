from typing import TYPE_CHECKING, List, Optional

from ...models import UserData

if TYPE_CHECKING:
    from . import Console
    from imouse import API


class User():
    def __init__(self, console: "Console"):
        self._console = console
        self._api: "API" = console._helper._api

    def get(self) -> Optional[UserData]:
        """获取imouse账号信息"""
        ret = self._api.config_user_info()
        if not self._console.successful(ret):
            return None
        return ret

    def login(self, user_name: str, password: str, utag: int) -> Optional[UserData]:
        """登录imouse账号"""
        ret = self._api.config_user_login(user_name, password, utag)
        if not self._console.successful(ret):
            return None
        return ret.data

    def logout(self) -> bool:
        """退出imouse账号"""
        return self._console.successful(self._api.config_user_logout())

    def switch_utag(self, utag: int) -> bool:
        """切换imouse子账号"""
        return self._console.successful(self._api.config_user_switch(utag))
