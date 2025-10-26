from typing import TYPE_CHECKING, List

from ...models import AlbumFileResult, FileResult
from ...types import AlbumFileParams, PhoneFileParams

if TYPE_CHECKING:
    from . import Device
    from imouse import API


class Shortcut:
    def __init__(self, device: "Device"):
        self._device = device
        self._api: "API" = device._helper._api
        self._device_id = device.device_id

    def album_get(self, album_name: str = "", num: int = 20,
                  outtime: int = 15) -> List[AlbumFileResult]:
        """获取相册列表"""
        ret = self._api.shortcut_album_get(self._device_id, album_name, num, outtime)
        if not self._device.successful(ret):
            return []
        result_list = ret.data.result_list if ret.data and ret.data.result_list else []
        return result_list

    def album_update(self, files: List[str], album_name: str = "", is_zip: bool = False,
                     outtime: int = 30) -> List[AlbumFileResult]:
        """上传文件到相册"""
        ret = self._api.shortcut_album_upload(self._device_id, album_name, files, is_zip, outtime)
        if not self._device.successful(ret):
            return []
        result_list = ret.data.result_list if ret.data and ret.data.result_list else []
        return result_list

    def album_down(self, files: List[AlbumFileParams], is_zip: bool = False,
                   outtime: int = 30) -> bool:
        """下载相册文件"""
        return self._device.successful(self._api.shortcut_album_down(self._device_id, files, is_zip, outtime))

    def album_del(self, files: List[AlbumFileParams], outtime: int = 30) -> List[AlbumFileResult]:
        """删除相册文件"""
        ret = self._api.shortcut_album_del(self._device_id, files, outtime)
        if not self._device.successful(ret):
            return []
        result_list = ret.data.result_list if ret.data and ret.data.result_list else []
        return result_list

    def album_clear(self, album_name: str = '', outtime: int = 30) -> List[AlbumFileResult]:
        """清空相册文件"""
        ret = self._api.shortcut_album_clear(self._device_id, album_name, outtime)
        if not self._device.successful(ret):
            return []
        result_list = ret.data.result_list if ret.data and ret.data.result_list else []
        return result_list

    def file_get(self, path: str = "",
                 outtime: int = 15) -> List[FileResult]:
        """获取文件列表"""
        ret = self._api.shortcut_file_get(self._device_id, path, outtime)
        if not self._device.successful(ret):
            return []
        result_list = ret.data.result_list if ret.data and ret.data.result_list else []
        return result_list

    def file_upload(self, files: List[str], path: str, is_zip: bool = False,
                    outtime: int = 30) -> List[FileResult]:
        """上传文件到手机"""
        ret = self._api.shortcut_file_upload(self._device_id, path, files, is_zip, outtime)
        if not self._device.successful(ret):
            return []
        result_list = ret.data.result_list if ret.data and ret.data.result_list else []
        return result_list

    def file_down(self, path: str, files: List[PhoneFileParams], is_zip: bool = False,
                  outtime: int = 30) -> bool:
        """从手机下载文件"""
        return self._device.successful(self._api.shortcut_file_down(self._device_id, path, files, is_zip, outtime))

    def file_del(self, path: str, files: List[PhoneFileParams],
                 outtime: int = 30) -> List[FileResult]:
        """删除手机文件"""
        ret = self._api.shortcut_file_del(self._device_id, path, files, outtime)
        if not self._device.successful(ret):
            return []
        result_list = ret.data.result_list if ret.data and ret.data.result_list else []
        return result_list

    def clipboard_set(self, text: str, sleep: int = 0, outtime: int = 10) -> bool:
        """发送文字到手机剪切板"""
        return self._device.successful(self._api.shortcut_clipboard_set(self._device_id, text, sleep, outtime))

    def clipboard_get(self, outtime: int = 10) -> str:
        """获取手机剪切板内容"""
        ret = self._api.shortcut_clipboard_get(self._device_id, outtime)
        if not self._device.successful(ret):
            return ""
        return ret.data.text if ret.data and ret.data.text else ""

    def exec_url(self, url: str, outtime: int = 10) -> bool:
        """打开url"""
        return self._device.successful(self._api.shortcut_exec_url(self._device_id, url, outtime))

    def switch_device(self, state: int, outtime: int = 10) -> bool:
        """重启关闭手机"""
        return self._device.successful(self._api.shortcut_switch_device(self._device_id, state, outtime))

    def switch_bril(self, state: float, outtime: int = 10) -> bool:
        """设置屏幕亮度"""
        return self._device.successful(self._api.shortcut_switch_bril(self._device_id, state, outtime))

    def switch_torch(self, state: int, outtime: int = 10) -> bool:
        """开关手电筒"""
        return self._device.successful(self._api.shortcut_switch_torch(self._device_id, state, outtime))

    def switch_flight(self, state: int, outtime: int = 10) -> bool:
        """开关飞行模式"""
        return self._device.successful(self._api.shortcut_switch_flight(self._device_id, state, outtime))

    def switch_cdpd(self, state: int, outtime: int = 10) -> bool:
        """开关蜂窝数据"""
        return self._device.successful(self._api.shortcut_switch_cdpd(self._device_id, state, outtime))

    def switch_wlan(self, state: int, outtime: int = 10) -> bool:
        """开关无线局域网"""
        return self._device.successful(self._api.shortcut_switch_wlan(self._device_id, state, outtime))

    def device_ip(self, outtime: int = 10) -> str:
        """获取外网ip"""
        ret = self._api.shortcut_device_ip(self._device_id, outtime)
        if not self._device.successful(ret):
            return ""
        return ret.data.text if ret.data and ret.data.text else ""
