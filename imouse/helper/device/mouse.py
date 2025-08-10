from typing import TYPE_CHECKING

from ...types import MouseSwipeParams

if TYPE_CHECKING:
    from . import Device
    from imouse import API


class Mouse:
    def __init__(self, device: "Device"):
        self._device = device
        self._api: "API" = device._helper._api
        self._device_id = device.device_id

    def click(self, x: int, y: int, time: int = 0, button: int = 1) -> bool:
        """点击"""
        return self._device.successful(self._api.mouse_click(self._device_id, str(button), x, y, time))

    def swipe(self, params: MouseSwipeParams) -> bool:
        """滑动"""
        return self._device.successful(self._api.mouse_swipe(self._device_id, params))

    def down(self, button: int = 1) -> bool:
        """按下"""
        return self._device.successful(self._api.mouse_down(self._device_id, str(button)))

    def up(self, button: int = 1) -> bool:
        """弹起"""
        return self._device.successful(self._api.mouse_up(self._device_id, str(button)))

    def move(self, x: int, y: int) -> bool:
        """移动"""
        return self._device.successful(self._api.mouse_move(self._device_id, x, y))

    def reset(self) -> bool:
        """复位"""
        return self._device.successful(self._api.mouse_reset(self._device_id))

    def wheel(self, direction: str, len, number: int) -> bool:
        """滚轮"""
        return self._device.successful(self._api.mouse_wheel(self._device_id, direction, len, number))
