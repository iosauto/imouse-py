from typing import TYPE_CHECKING, List
from ...types import FunctionKeys

if TYPE_CHECKING:
    from . import Device
    from imouse import API


class KeyBoard:
    def __init__(self, device: "Device"):
        self._device = device
        self._api: "API" = device._helper._api
        self._device_id = device.device_id

    def send_keys(self, keys: str) -> bool:
        """发送字符键"""
        return self._device.successful(self._api.key_sendkey(self._device_id, keys, ""))

    def send_fn_key(self, fn_key: FunctionKeys) -> bool:
        """发送功能键"""
        return self._device.successful(self._api.key_sendkey(self._device_id, "", fn_key.value))

    def send_hid(self, command_list: List[str]) -> bool:
        """键盘高级操作"""
        return self._device.successful(self._api.key_sendhid(self._device_id, command_list))
