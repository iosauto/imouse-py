from typing import TYPE_CHECKING, List, Union

from ...models import FindImageResult, FindImageCvResult, OcrResult, FindMultiColorResult
from ...types import MultiColorParams

if TYPE_CHECKING:
    from . import Device
    from imouse import API


class Image:
    def __init__(self, device: "Device"):
        self._device = device
        self._api: "API" = device._helper._api
        self._device_id = device.device_id

    def screenshot(self, rect: List[int] = None,delay:float = 0) -> Union[
        None, bytes]:
        """截取设备屏幕"""
        ret = self._api.pic_screenshot(self._device_id, False, rect)
        if isinstance(ret, bytes):
            return ret
        self._device.successful(ret,delay)
        return None

    def find_image(self, img_list: List[str], similarity: float = 0.85, all: bool = False,
                   rect: List[int] = None,
                   delta_color: str = "", direction: str = "", delay:float = 0) -> List[FindImageResult]:
        """普通找图"""
        ret = self._api.pic_find_image(self._device_id, img_list, similarity, all, rect, delta_color, direction)
        self._device.successful(ret,delay)
        return ret.data.result_list

    def find_image_cv(self, img_list: List[str], similarity: float = 0.85, all: bool = False,
                      same: bool = False,
                      rect: List[int] = None,delay:float = 0) -> List[FindImageCvResult]:
        """OpenCV找图"""
        ret = self._api.pic_find_image_cv(self._device_id, img_list, similarity, all, same, rect)
        self._device.successful(ret,delay)
        return ret.data.result_list

    def ocr(self, rect: List[int] = None, is_ex: bool = False,delay:float = 0) -> List[OcrResult]:
        """OCR文字识别"""
        ret = self._api.pic_ocr(self._device_id, rect, is_ex)
        self._device.successful(ret,delay)
        return ret.data.result_list

    def find_text(self, text_list: List[str], similarity: float, contain: bool = False,
                  rect: List[int] = None,
                  is_ex: bool = False, delay:float = 0) -> List[OcrResult]:
        """查找文字"""
        ret = self._api.pic_find_text(self._device_id, text_list, similarity, contain, rect, is_ex)
        self._device.successful(ret,delay)
        return ret.data.result_list

    def find_multi_color(self, params: List[MultiColorParams], all: bool = False,
                         same: bool = False,delay:float = 0) -> List[FindMultiColorResult]:
        """多点找色"""
        ret = self._api.pic_find_multi_color(self._device_id, params, all, same)
        self._device.successful(ret,delay)
        return ret.data.result_list


