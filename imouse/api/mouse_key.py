from abc import abstractmethod
from typing import Optional, List, Union

from imouse.models import CommonResponse
from imouse.api import Payload
from imouse.types import MouseSwipeParams, SendHidParams
from imouse.utils.utils import parse_model


class MouseKey():
    def __init__(self):
        super().__init__()
        self._payload = self._get_payload()

    @abstractmethod
    def _call_api(self, request_dict: dict, timeout: int = 0, is_async: bool = False)->Union[dict, bytes, None]:
        pass

    @abstractmethod
    def _get_payload(self) -> Payload:
        pass

    def mouse_click(self, device_id, button: str, x, y, time: int = 0) -> Optional[CommonResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E9%BC%A0%E6%A0%87%E9%94%AE%E7%9B%98/%E9%BC%A0%E6%A0%87%E7%82%B9%E5%87%BB"""
        ret = self._call_api(
            self._payload.mouse_click(device_id, button, x, y, time)
        )
        return parse_model(CommonResponse, ret) if ret is not None else None

    def mouse_swipe(self, device_id, params: MouseSwipeParams) -> Optional[CommonResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E9%BC%A0%E6%A0%87%E9%94%AE%E7%9B%98/%E9%BC%A0%E6%A0%87%E6%BB%91%E5%8A%A8"""
        ret = self._call_api(
            self._payload.mouse_swipe(device_id, params=params)
        )
        return parse_model(CommonResponse, ret) if ret is not None else None

    def mouse_up(self, device_id, button: str) -> Optional[CommonResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E9%BC%A0%E6%A0%87%E9%94%AE%E7%9B%98/%E9%BC%A0%E6%A0%87%E5%BC%B9%E8%B5%B7"""
        ret = self._call_api(
            self._payload.mouse_up(device_id, button)
        )
        return parse_model(CommonResponse, ret) if ret is not None else None

    def mouse_down(self, device_id, button: str) -> Optional[CommonResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E9%BC%A0%E6%A0%87%E9%94%AE%E7%9B%98/%E9%BC%A0%E6%A0%87%E6%8C%89%E4%B8%8B"""
        ret = self._call_api(
            self._payload.mouse_down(device_id, button)
        )
        return parse_model(CommonResponse, ret) if ret is not None else None

    def mouse_move(self, device_id: str, x, y: int) -> Optional[CommonResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E9%BC%A0%E6%A0%87%E9%94%AE%E7%9B%98/%E9%BC%A0%E6%A0%87%E7%A7%BB%E5%8A%A8"""
        ret = self._call_api(
            self._payload.mouse_move(device_id, x, y)
        )
        return parse_model(CommonResponse, ret) if ret is not None else None

    def mouse_reset(self, device_id: str) -> Optional[CommonResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E9%BC%A0%E6%A0%87%E9%94%AE%E7%9B%98/%E9%BC%A0%E6%A0%87%E5%A4%8D%E4%BD%8D"""
        ret = self._call_api(
            self._payload.mouse_reset(device_id)
        )
        return parse_model(CommonResponse, ret) if ret is not None else None

    def mouse_wheel(self, device_id, direction: str, len, number: int) -> Optional[CommonResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E9%BC%A0%E6%A0%87%E9%94%AE%E7%9B%98/%E9%BC%A0%E6%A0%87%E6%BB%9A%E8%BD%AE"""
        ret = self._call_api(
            self._payload.mouse_wheel(device_id, direction, len, number)
        )
        return parse_model(CommonResponse, ret) if ret is not None else None

    def key_sendkey(self, device_id, key, fn_key: str) -> Optional[CommonResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E9%BC%A0%E6%A0%87%E9%94%AE%E7%9B%98/%E9%94%AE%E7%9B%98%E8%BE%93%E5%85%A5"""
        ret = self._call_api(
            self._payload.key_sendkey(device_id, key, fn_key)
        )
        return parse_model(CommonResponse, ret) if ret is not None else None

    def key_sendhid(self, device_id, command_list: List[SendHidParams]) -> Optional[CommonResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E9%BC%A0%E6%A0%87%E9%94%AE%E7%9B%98/%E9%94%AE%E7%9B%98%E9%AB%98%E7%BA%A7%E6%93%8D%E4%BD%9C"""
        ret = self._call_api(
            self._payload.key_sendhid(device_id, command_list)
        )
        return parse_model(CommonResponse, ret) if ret is not None else None





