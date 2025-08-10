from typing import TYPE_CHECKING, List

from ...models import DeviceInfo

if TYPE_CHECKING:
    from . import Console
    from imouse import API


class Device():
    def __init__(self, console: "Console"):
        self._console = console
        self._api: "API" = console._helper._api

    def list_by_id(self, device_ids: str = "") -> List[DeviceInfo]:
        """通过设备id获取设备列表"""
        ret = self._api.device_get(device_ids)
        if not self._console.successful(ret):
            return []
        result_list = ret.data.device_list if ret.data and ret.data.device_list else []
        return result_list

    def list_by_group(self, gid: str = "0") -> List[DeviceInfo]:
        """通过分组id获取设备列表"""
        ret = self._api.device_group_getdev(gid)
        if not self._console.successful(ret):
            return []
        result_list = ret.data.device_list if ret.data and ret.data.device_list else []
        return result_list

    def set_name(self, device_ids: str, name: str) -> List[str]:
        """设置设备名称"""
        ret = self._api.device_set_name(device_ids, name)

        if not self._console.successful(ret):
            return []
        result_list = ret.data.id_list if ret.data and ret.data.id_list else []
        return result_list

    def bind_hardware(self, device_id: str, vid, pid: str) -> List[str]:
        """绑定硬件"""
        ret = self._api.device_bind_hardware(device_id, vid, pid)
        if not self._console.successful(ret):
            return []
        result_list = ret.data.id_list if ret.data and ret.data.id_list else []
        return result_list

    def set_mouse_location(self, device_ids: str, location_crc: str) -> List[str]:
        """设置鼠标参数"""
        ret = self._api.device_set_mouse_location(device_ids, location_crc)
        if not self._console.successful(ret):
            return []
        result_list = ret.data.id_list if ret.data and ret.data.id_list else []
        return result_list

    def set_group(self, device_ids: str, group_id: str) -> List[str]:
        """设置设备分组"""
        ret = self._api.device_set_group(device_ids, group_id)
        if not self._console.successful(ret):
            return []
        result_list = ret.data.id_list if ret.data and ret.data.id_list else []
        return result_list

    def delete(self, device_ids: str) -> List[str]:
        """删除设备"""
        ret = self._api.device_del(device_ids)
        if not self._console.successful(ret):
            return []
        result_list = ret.data.id_list if ret.data and ret.data.id_list else []
        return result_list

    def restart(self, device_ids: str) -> List[str]:
        """重启设备"""
        return self._console.successful(self._api.device_restart(device_ids))
