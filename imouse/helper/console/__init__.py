from typing import TYPE_CHECKING, Optional

from ...models import ImServerConfigData

if TYPE_CHECKING:
    from . import Helper

from .device import Device
from .group import Group
from .airplay import AirPlay
from .usb import Usb
from .im_config import ImConfig
from .user import User


class Console:
    def __init__(self, helper: "Helper"):
        self._helper = helper
        self._imserver_config = self.get_imserver_config
        self._error_code: Optional[int] = None
        self._error_msg: Optional[str] = None

    def _set_error(self, code: int, message: str):
        self._error_code = code
        self._error_msg = message

    def _clear_error(self):
        self._error_code = None
        self._error_msg = None

    def successful(self, common_response):
        try:
            if common_response.status != 200:
                self._set_error(common_response.status, common_response.message)
                return False

            if common_response.data.code != 0:
                self._set_error(common_response.data.code, common_response.data.message)
                return False

            self._clear_error()
            return True
        except Exception as e:
            self._set_error(-1, f"解析响应失败: {e}")
            return False

    def restart_core(self) -> bool:
        return self.successful(self._helper._api.imserver_restart())

    @property
    def get_imserver_config(self) -> ImServerConfigData:
        ret = self._helper._api.config_imserver_get()
        if self.successful(ret):
            self._imserver_config = ret.data
        else:
            self._imserver_config = None
        return self._imserver_config

    @property
    def device(self):
        return Device(self)

    @property
    def group(self):
        return Group(self)

    @property
    def airplay(self):
        return AirPlay(self)

    @property
    def usb(self):
        return Usb(self)

    @property
    def user(self):
        return User(self)

    @property
    def im_config(self):
        return ImConfig(self)

    @property
    def error_code(self) -> Optional[int]:
        ret = self._error_code
        self._error_code = None
        return ret

    @property
    def error_msg(self) -> Optional[str]:
        ret = self._error_msg
        self._error_msg = None
        return ret

