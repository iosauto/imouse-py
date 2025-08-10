from abc import abstractmethod
from typing import Optional, Union

from imouse.models import DeviceListResponse, IdListResponse, GroupListResponse, CommonResponse, \
    DeviceSortResponse
from imouse.api import Payload
from imouse.types import SetDeviceParams, SetDeviceAirplayParams
from imouse.utils.utils import parse_model


class Device():
    def __init__(self):
        super().__init__()
        self._payload = self._get_payload()

    @abstractmethod
    def _call_api(self, request_dict: dict, timeout: int = 0, is_async: bool = False)->Union[dict, bytes, None]:
        pass

    @abstractmethod
    def _get_payload(self) -> Payload:
        pass

    def device_get(self, device_id: str = '') -> Optional[DeviceListResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E8%AE%BE%E5%A4%87%E7%9B%B8%E5%85%B3/%E8%8E%B7%E5%8F%96%E8%AE%BE%E5%A4%87%E5%88%97%E8%A1%A8"""
        ret = self._call_api(
            self._payload.device_get(device_id)
        )
        return parse_model(DeviceListResponse, ret) if ret is not None else None

    def device_group_get(self, group_id: str = '') -> Optional[GroupListResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E8%AE%BE%E5%A4%87%E7%9B%B8%E5%85%B3/%E8%8E%B7%E5%8F%96%E5%88%86%E7%BB%84%E5%88%97%E8%A1%A8"""
        ret = self._call_api(
            self._payload.device_group_get(group_id)
        )
        return parse_model(GroupListResponse, ret) if ret is not None else None

    def device_group_getdev(self, group_id: str) -> Optional[DeviceListResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E8%AE%BE%E5%A4%87%E7%9B%B8%E5%85%B3/%E8%8E%B7%E5%8F%96%E5%88%86%E7%BB%84%E5%86%85%E8%AE%BE%E5%A4%87"""
        ret = self._call_api(
            self._payload.device_group_getdev(group_id)
        )
        return parse_model(DeviceListResponse, ret) if ret is not None else None

    def device_set_name(self, device_id, name: str) -> Optional[IdListResponse]:
        ret = self._call_api(
            self._payload.device_set(device_id, SetDeviceParams(
                name=name,
            ))
        )
        return parse_model(IdListResponse, ret) if ret is not None else None

    def device_bind_hardware(self, device_id, vid, pid: str) -> Optional[IdListResponse]:
        ret = self._call_api(
            self._payload.device_set(device_id, SetDeviceParams(
                vid=vid,
                pid=pid,
            ))
        )
        return parse_model(IdListResponse, ret) if ret is not None else None

    def device_set_mouse_location(self, device_id, location_crc: str) -> Optional[IdListResponse]:
        ret = self._call_api(
            self._payload.device_set(device_id, SetDeviceParams(
                location_crc=location_crc
            ))
        )
        return parse_model(IdListResponse, ret) if ret is not None else None

    def device_set_group(self, device_id, group_id: str) -> Optional[IdListResponse]:
        ret = self._call_api(
            self._payload.device_set(device_id, SetDeviceParams(
                gid=group_id
            ))
        )
        return parse_model(IdListResponse, ret) if ret is not None else None

    def device_del(self, device_id: str) -> Optional[IdListResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E8%AE%BE%E5%A4%87%E7%9B%B8%E5%85%B3/%E5%88%A0%E9%99%A4%E8%AE%BE%E5%A4%87"""
        ret = self._call_api(
            self._payload.device_del(device_id)
        )
        return parse_model(IdListResponse, ret) if ret is not None else None

    def device_group_set(self, group_id: str, group_name: str) -> Optional[GroupListResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E8%AE%BE%E5%A4%87%E7%9B%B8%E5%85%B3/%E8%AE%BE%E7%BD%AE%E5%88%86%E7%BB%84"""
        ret = self._call_api(
            self._payload.device_group_set(group_id, group_name)
        )
        return parse_model(GroupListResponse, ret) if ret is not None else None

    def device_group_del(self, group_id: str) -> Optional[IdListResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E8%AE%BE%E5%A4%87%E7%9B%B8%E5%85%B3/%E5%88%A0%E9%99%A4%E5%88%86%E7%BB%84"""
        ret = self._call_api(
            self._payload.device_group_del(group_id)
        )
        return parse_model(IdListResponse, ret) if ret is not None else None

    def device_airplay_set(self, device_id: str, params: SetDeviceAirplayParams) -> Optional[CommonResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E8%AE%BE%E5%A4%87%E7%9B%B8%E5%85%B3/%E8%AE%BE%E7%BD%AE%E8%AE%BE%E5%A4%87%E6%8A%95%E5%B1%8F%E9%85%8D%E7%BD%AE"""
        ret = self._call_api(
            self._payload.device_airplay_set(device_id, params)
        )
        return parse_model(CommonResponse, ret) if ret is not None else None

    def device_airplay_connect(self, device_id: str) -> Optional[CommonResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E8%AE%BE%E5%A4%87%E7%9B%B8%E5%85%B3/%E8%BF%9E%E6%8E%A5%E6%8A%95%E5%B1%8F"""
        ret = self._call_api(
            self._payload.device_airplay_connect(device_id)
        )
        return parse_model(CommonResponse, ret) if ret is not None else None

    def device_airplay_connect_all(self) -> Optional[CommonResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E8%AE%BE%E5%A4%87%E7%9B%B8%E5%85%B3/%E6%8A%95%E5%B1%8F%E6%89%80%E6%9C%89"""
        ret = self._call_api(
            self._payload.device_airplay_connect_all()
        )
        return parse_model(CommonResponse, ret) if ret is not None else None

    def device_airplay_disconnect(self, device_id: str) -> Optional[CommonResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E8%AE%BE%E5%A4%87%E7%9B%B8%E5%85%B3/%E6%96%AD%E5%BC%80%E6%8A%95%E5%B1%8F"""
        ret = self._call_api(
            self._payload.device_airplay_disconnect(device_id)
        )
        return parse_model(CommonResponse, ret) if ret is not None else None

    def device_restart(self, device_id: str) -> Optional[CommonResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E8%AE%BE%E5%A4%87%E7%9B%B8%E5%85%B3/%E9%87%8D%E5%90%AF%E8%AE%BE%E5%A4%87"""
        ret = self._call_api(
            self._payload.device_restart(device_id)
        )
        return parse_model(CommonResponse, ret) if ret is not None else None

    def device_usb_restart(self, vpids: str) -> Optional[CommonResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E8%AE%BE%E5%A4%87%E7%9B%B8%E5%85%B3/%E9%87%8D%E5%90%AFusb"""
        ret = self._call_api(
            self._payload.device_usb_restart(vpids)
        )
        return parse_model(CommonResponse, ret) if ret is not None else None

    def device_sort_set(self, sort_index, sort_value: int) -> Optional[DeviceSortResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E8%AE%BE%E5%A4%87%E7%9B%B8%E5%85%B3/%E8%AE%BE%E7%BD%AE%E8%AE%BE%E5%A4%87%E5%88%97%E8%A1%A8%E6%8E%92%E5%BA%8F"""
        ret = self._call_api(
            self._payload.device_sort_set(sort_index, sort_value)
        )
        return parse_model(DeviceSortResponse, ret) if ret is not None else None

    def device_sort_get(self) -> Optional[DeviceSortResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E8%AE%BE%E5%A4%87%E7%9B%B8%E5%85%B3/%E8%8E%B7%E5%8F%96%E8%AE%BE%E5%A4%87%E5%88%97%E8%A1%A8%E6%8E%92%E5%BA%8F"""
        ret = self._call_api(
            self._payload.device_sort_get()
        )
        return parse_model(DeviceSortResponse, ret) if ret is not None else None
