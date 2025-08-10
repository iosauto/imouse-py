from abc import abstractmethod
from typing import Optional, Union

from imouse.models import UsbListResponse, ImServerConfigResponse, ImServerConfigData, CommonResponse
from imouse.api import Payload
from imouse.utils.utils import parse_model


class Config():
    def __init__(self):
        super().__init__()
        self._payload = self._get_payload()

    @abstractmethod
    def _call_api(self, request_dict: dict, timeout: int = 0, is_async: bool = False)->Union[dict, bytes, None]:
        pass

    @abstractmethod
    def _get_payload(self) -> Payload:
        pass


    def config_usb_get(self) -> Optional[UsbListResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E9%85%8D%E7%BD%AE%E7%9B%B8%E5%85%B3/%E8%8E%B7%E5%8F%96%E5%B7%B2%E8%BF%9E%E6%8E%A5%E7%A1%AC%E4%BB%B6%E5%88%97%E8%A1%A8"""
        ret = self._call_api(
            self._payload.config_usb_get()
        )
        return parse_model(UsbListResponse, ret) if ret is not None else None

    def config_imserver_get(self) -> Optional[ImServerConfigResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E9%85%8D%E7%BD%AE%E7%9B%B8%E5%85%B3/%E8%8E%B7%E5%8F%96%E5%86%85%E6%A0%B8%E9%85%8D%E7%BD%AE"""
        ret = self._call_api(
            self._payload.config_imserver_get()
        )
        return parse_model(ImServerConfigResponse, ret) if ret is not None else None

    def config_imserver_set(self,params: ImServerConfigData) -> Optional[ImServerConfigResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E9%85%8D%E7%BD%AE%E7%9B%B8%E5%85%B3/%E8%AE%BE%E7%BD%AE%E5%86%85%E6%A0%B8%E9%85%8D%E7%BD%AE"""
        ret = self._call_api(
            self._payload.config_imserver_set(params)
        )
        return parse_model(ImServerConfigResponse, ret) if ret is not None else None

    def imserver_regmdns(self) -> Optional[CommonResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E9%85%8D%E7%BD%AE%E7%9B%B8%E5%85%B3/%E9%87%8D%E6%96%B0%E5%B9%BF%E6%92%AD%E6%8A%95%E5%B1%8F"""
        ret = self._call_api(
            self._payload.imserver_regmdns()
        )
        return parse_model(CommonResponse, ret) if ret is not None else None

    def imserver_restart(self) -> Optional[CommonResponse]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E9%85%8D%E7%BD%AE%E7%9B%B8%E5%85%B3/%E9%87%8D%E5%90%AF%E5%86%85%E6%A0%B8"""
        ret = self._call_api(
            self._payload.imserver_restart()
        )
        return parse_model(CommonResponse, ret) if ret is not None else None