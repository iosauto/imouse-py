from typing import TYPE_CHECKING, List, Optional

from ...models import UsbInfo

if TYPE_CHECKING:
    from . import Console
    from imouse import API


class Usb():
    def __init__(self, console: "Console"):
        self._console = console
        self._api: "API" = console._helper._api

    def get(self) -> List[UsbInfo]:
        """获取硬件列表"""
        ret = self._api.config_usb_get()
        if not self._console.successful(ret):
            return []
        result_list = ret.data.usb_list if ret.data and ret.data.usb_list else []
        return result_list

    def restart(self, vpids: str) -> bool:
        """重启硬件"""
        return self._console.successful(self._api.device_usb_restart(vpids))
