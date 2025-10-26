from abc import abstractmethod
from typing import Union, List

from imouse.models import CommonResponse, AlbumFileResponse, PhoneFileResponse, ResultTextResponse
from imouse.api import Payload
from imouse.types import AlbumFileParams, PhoneFileParams
from imouse.utils.utils import parse_model


class Shortcut():
    def __init__(self):
        super().__init__()
        self._payload = self._get_payload()

    @abstractmethod
    def _call_api(self, request_dict: dict, timeout: int = 0, is_async: bool = False) -> Union[dict, bytes, None]:
        pass

    @abstractmethod
    def _get_payload(self) -> Payload:
        pass

    def shortcut_album_get(self, device_id: str, album_name: str = "", num: int = 20,
                           outtime: int = 15) -> AlbumFileResponse:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E5%BF%AB%E6%8D%B7%E6%8C%87%E4%BB%A4/%E8%8E%B7%E5%8F%96%E7%9B%B8%E5%86%8C%E5%88%97%E8%A1%A8"""
        ret = self._call_api(
            self._payload.shortcut_album_get(device_id, album_name, num, outtime * 1000), timeout=outtime + 1
        )
        return parse_model(AlbumFileResponse, ret) if ret is not None else None

    def shortcut_album_upload(self, device_id: str, album_name: str, files: List[str], is_zip: bool = False,
                              outtime: int = 30) -> AlbumFileResponse:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E5%BF%AB%E6%8D%B7%E6%8C%87%E4%BB%A4/%E4%B8%8A%E4%BC%A0%E7%85%A7%E7%89%87%E8%A7%86%E9%A2%91"""
        ret = self._call_api(
            self._payload.shortcut_album_upload(device_id, album_name, files, is_zip, outtime * 1000),
            timeout=outtime + 1
        )
        return parse_model(AlbumFileResponse, ret) if ret is not None else None

    def shortcut_album_down(self, device_id: str, files: List[AlbumFileParams], is_zip: bool = False,
                            outtime: int = 30) -> CommonResponse:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E5%BF%AB%E6%8D%B7%E6%8C%87%E4%BB%A4/%E4%B8%8B%E8%BD%BD%E7%85%A7%E7%89%87%E8%A7%86%E9%A2%91"""
        ret = self._call_api(
            self._payload.shortcut_album_down(device_id, files, is_zip, outtime * 1000), timeout=outtime + 1
        )
        return parse_model(CommonResponse, ret) if ret is not None else None

    def shortcut_album_del(self, device_id: str, files: List[AlbumFileParams], outtime: int = 30) -> AlbumFileResponse:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E5%BF%AB%E6%8D%B7%E6%8C%87%E4%BB%A4/%E5%88%A0%E9%99%A4%E7%85%A7%E7%89%87%E8%A7%86%E9%A2%91"""
        ret = self._call_api(
            self._payload.shortcut_album_del(device_id, files, outtime * 1000), timeout=outtime + 1
        )
        return parse_model(AlbumFileResponse, ret) if ret is not None else None

    def shortcut_album_clear(self, device_id: str, album_name: str = '', outtime: int = 30) -> AlbumFileResponse:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E5%BF%AB%E6%8D%B7%E6%8C%87%E4%BB%A4/%E6%B8%85%E7%A9%BA%E7%85%A7%E7%89%87%E8%A7%86%E9%A2%91"""
        ret = self._call_api(
            self._payload.shortcut_album_clear(device_id, album_name, outtime * 1000), timeout=outtime + 1
        )
        return parse_model(AlbumFileResponse, ret) if ret is not None else None

    def shortcut_file_get(self, device_id: str, path: str = "",
                          outtime: int = 15) -> PhoneFileResponse:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E5%BF%AB%E6%8D%B7%E6%8C%87%E4%BB%A4/%E8%8E%B7%E5%8F%96%E6%96%87%E4%BB%B6%E5%88%97%E8%A1%A8"""
        ret = self._call_api(
            self._payload.shortcut_file_get(device_id, path, outtime * 1000), timeout=outtime + 1
        )
        return parse_model(PhoneFileResponse, ret) if ret is not None else None

    def shortcut_file_upload(self, device_id: str, path: str, files: List[str], is_zip: bool = False,
                             outtime: int = 30) -> PhoneFileResponse:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E5%BF%AB%E6%8D%B7%E6%8C%87%E4%BB%A4/%E4%B8%8A%E4%BC%A0%E6%96%87%E4%BB%B6"""
        ret = self._call_api(
            self._payload.shortcut_file_upload(device_id, path, is_zip, files, outtime * 1000),
            timeout=outtime + 1
        )
        return parse_model(PhoneFileResponse, ret) if ret is not None else None

    def shortcut_file_down(self, device_id: str, path: str, files: List[PhoneFileParams], is_zip: bool = False,
                           outtime: int = 30) -> CommonResponse:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E5%BF%AB%E6%8D%B7%E6%8C%87%E4%BB%A4/%E4%B8%8B%E8%BD%BD%E6%96%87%E4%BB%B6"""
        ret = self._call_api(
            self._payload.shortcut_file_down(device_id, path, is_zip, files, outtime * 1000), timeout=outtime + 1
        )
        return parse_model(CommonResponse, ret) if ret is not None else None

    def shortcut_file_del(self, device_id: str, path: str, files: List[PhoneFileParams],
                          outtime: int = 30) -> PhoneFileResponse:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E5%BF%AB%E6%8D%B7%E6%8C%87%E4%BB%A4/%E5%88%A0%E9%99%A4%E6%96%87%E4%BB%B6/"""
        ret = self._call_api(
            self._payload.shortcut_file_del(device_id, path, files, outtime * 1000), timeout=outtime + 1
        )
        return parse_model(PhoneFileResponse, ret) if ret is not None else None

    def shortcut_clipboard_set(self, device_id: str, text: str, sleep: int = 0, outtime: int = 10) -> CommonResponse:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E5%BF%AB%E6%8D%B7%E6%8C%87%E4%BB%A4/%E5%88%B0%E6%89%8B%E6%9C%BA%E5%89%AA%E5%88%87%E6%9D%BF"""
        ret = self._call_api(
            self._payload.shortcut_clipboard_set(device_id, text, sleep, outtime * 1000), timeout=outtime + 1
        )
        return parse_model(CommonResponse, ret) if ret is not None else None

    def shortcut_clipboard_get(self, device_id: str, outtime: int = 10) -> ResultTextResponse:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E5%BF%AB%E6%8D%B7%E6%8C%87%E4%BB%A4/%E5%8F%96%E6%89%8B%E6%9C%BA%E5%89%AA%E5%88%87%E6%9D%BF"""
        ret = self._call_api(
            self._payload.shortcut_clipboard_get(device_id, outtime * 1000), timeout=outtime + 1
        )
        return parse_model(ResultTextResponse, ret) if ret is not None else None

    def shortcut_exec_url(self, device_id: str, url: str, outtime: int = 10) -> CommonResponse:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E5%BF%AB%E6%8D%B7%E6%8C%87%E4%BB%A4/%E6%89%93%E5%BC%80url"""
        ret = self._call_api(
            self._payload.shortcut_exec_url(device_id, url, outtime * 1000), timeout=outtime + 1
        )
        return parse_model(CommonResponse, ret) if ret is not None else None

    def shortcut_switch_device(self, device_id: str, state: int, outtime: int = 10) -> CommonResponse:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E5%BF%AB%E6%8D%B7%E6%8C%87%E4%BB%A4/%E5%85%B3%E9%97%AD%E9%87%8D%E5%90%AF%E8%AE%BE%E5%A4%87"""
        ret = self._call_api(
            self._payload.shortcut_switch_device(device_id, state, outtime * 1000), timeout=outtime + 1
        )
        return parse_model(CommonResponse, ret) if ret is not None else None

    def shortcut_switch_bril(self, device_id: str, state: float, outtime: int = 10) -> CommonResponse:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E5%BF%AB%E6%8D%B7%E6%8C%87%E4%BB%A4/%E4%BA%AE%E5%BA%A6%E8%B0%83%E8%8A%82"""
        ret = self._call_api(
            self._payload.shortcut_switch_bril(device_id, state, outtime * 1000), timeout=outtime + 1
        )
        return parse_model(CommonResponse, ret) if ret is not None else None

    def shortcut_switch_torch(self, device_id: str, state: int, outtime: int = 10) -> CommonResponse:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E5%BF%AB%E6%8D%B7%E6%8C%87%E4%BB%A4/%E5%BC%80%E5%85%B3%E6%89%8B%E7%94%B5%E7%AD%92"""
        ret = self._call_api(
            self._payload.shortcut_switch_torch(device_id, state, outtime * 1000), timeout=outtime + 1
        )
        return parse_model(CommonResponse, ret) if ret is not None else None

    def shortcut_switch_flight(self, device_id: str, state: int, outtime: int = 10) -> CommonResponse:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E5%BF%AB%E6%8D%B7%E6%8C%87%E4%BB%A4/%E5%BC%80%E5%85%B3%E9%A3%9E%E8%A1%8C%E6%A8%A1%E5%BC%8F"""
        ret = self._call_api(
            self._payload.shortcut_switch_flight(device_id, state, outtime * 1000), timeout=outtime + 1
        )
        return parse_model(CommonResponse, ret) if ret is not None else None

    def shortcut_switch_cdpd(self, device_id: str, state: int, outtime: int = 10) -> CommonResponse:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E5%BF%AB%E6%8D%B7%E6%8C%87%E4%BB%A4/%E5%BC%80%E5%85%B3%E8%9C%82%E7%AA%9D%E6%95%B0%E6%8D%AE"""
        ret = self._call_api(
            self._payload.shortcut_switch_cdpd(device_id, state, outtime * 1000), timeout=outtime + 1
        )
        return parse_model(CommonResponse, ret) if ret is not None else None

    def shortcut_switch_wlan(self, device_id: str, state: int, outtime: int = 10) -> CommonResponse:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E5%BF%AB%E6%8D%B7%E6%8C%87%E4%BB%A4/%E5%BC%80%E5%85%B3%E6%97%A0%E7%BA%BF%E5%B1%80%E5%9F%9F%E7%BD%91"""
        ret = self._call_api(
            self._payload.shortcut_switch_wlan(device_id, state, outtime * 1000), timeout=outtime + 1
        )
        return parse_model(CommonResponse, ret) if ret is not None else None

    def shortcut_device_ip(self, device_id: str, outtime: int = 10) -> ResultTextResponse:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E5%BF%AB%E6%8D%B7%E6%8C%87%E4%BB%A4/%E5%8F%96%E6%89%8B%E6%9C%BAIP"""
        ret = self._call_api(
            self._payload.shortcut_device_ip(device_id, 1, outtime * 1000), timeout=outtime + 1
        )
        return parse_model(ResultTextResponse, ret) if ret is not None else None
