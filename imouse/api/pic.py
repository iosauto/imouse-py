from abc import abstractmethod
from typing import List, Union

from imouse.models import CommonResponse, FindImageResultResponse, FindImageCvResultResponse, OcrResultResponse, \
    FindMultiColorResponse
from imouse.api import Payload
from imouse.types import MultiColorParams
from imouse.utils.utils import parse_model


class Pic():
    def __init__(self):
        super().__init__()
        self._payload = self._get_payload()

    @abstractmethod
    def _call_api(self, request_dict: dict, timeout: int = 0, is_async: bool = False) -> Union[dict, bytes, None]:
        pass

    @abstractmethod
    def _get_payload(self) -> Payload:
        pass

    def pic_screenshot(self, device_id: str, is_jpg: bool = False, rect: List[int] = None) -> Union[
        CommonResponse, bytes]:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E5%9B%BE%E8%89%B2%E7%9B%B8%E5%85%B3/%E6%88%AA%E5%8F%96%E5%B1%8F%E5%B9%95"""
        ret = self._call_api(
            self._payload.pic_screenshot(device_id, is_jpg, rect)
        )
        if isinstance(ret, bytes):
            return ret
        return parse_model(CommonResponse, ret)

    def pic_find_image(self, device_id: str, img_list: List[str], similarity: float = 0.85, all: bool = False,
                       rect: List[int] = None,
                       delta_color: str = "", direction: str = "", ) -> FindImageResultResponse:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E5%9B%BE%E8%89%B2%E7%9B%B8%E5%85%B3/%E6%99%AE%E9%80%9A%E6%89%BE%E5%9B%BE"""
        ret = self._call_api(
            self._payload.pic_find_image(device_id, img_list, similarity, all, rect, delta_color, direction)
        )
        return parse_model(FindImageResultResponse, ret) if ret is not None else None

    def pic_find_image_cv(self, device_id: str, img_list: List[str], similarity: float = 0.85, all: bool = False,
                          same: bool = False,
                          rect: List[int] = None) -> FindImageCvResultResponse:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E5%9B%BE%E8%89%B2%E7%9B%B8%E5%85%B3/OpenCV%E6%89%BE%E5%9B%BE"""
        ret = self._call_api(
            self._payload.pic_find_image_cv(device_id, img_list, similarity, all, same, rect)
        )
        return parse_model(FindImageCvResultResponse, ret) if ret is not None else None

    def pic_ocr(self, device_id: str, rect: List[int] = None, is_ex: bool = False,
                ) -> OcrResultResponse:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E5%9B%BE%E8%89%B2%E7%9B%B8%E5%85%B3/OCR%E6%96%87%E5%AD%97%E8%AF%86%E5%88%AB"""
        ret = self._call_api(
            self._payload.pic_ocr(device_id, rect, is_ex)
        )
        return parse_model(OcrResultResponse, ret) if ret is not None else None

    def pic_find_text(self, device_id: str, text_list: List[str], similarity: float, contain: bool = False,
                      rect: List[int] = None,
                      is_ex: bool = False,
                      ) -> OcrResultResponse:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E5%9B%BE%E8%89%B2%E7%9B%B8%E5%85%B3/%E6%9F%A5%E6%89%BE%E6%96%87%E5%AD%97"""
        ret = self._call_api(
            self._payload.pic_find_text(device_id, text_list, similarity, contain, rect, is_ex)
        )
        return parse_model(OcrResultResponse, ret) if ret is not None else None

    def pic_find_multi_color(self, device_id: str, params: List[MultiColorParams], all: bool = False,
                             same: bool = False
                             ) -> FindMultiColorResponse:
        """https://www.imouse.cc/XP%E7%89%88API%E6%96%87%E6%A1%A3/%E5%9B%BE%E8%89%B2%E7%9B%B8%E5%85%B3/%E5%A4%9A%E7%82%B9%E6%89%BE%E8%89%B2"""
        ret = self._call_api(
            self._payload.pic_find_multi_color(device_id, params, all, same)
        )
        return parse_model(FindMultiColorResponse, ret) if ret is not None else None
