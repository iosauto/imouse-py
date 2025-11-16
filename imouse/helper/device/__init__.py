import time
from typing import Optional, TYPE_CHECKING
from .image import Image
from .keyboard import KeyBoard
from .mouse import Mouse
from .shortcut import Shortcut
from ...models import DeviceInfo

if TYPE_CHECKING:
    from . import Helper


class Device:
    def __init__(self, helper: "Helper", device_id: str, device_info: DeviceInfo = None):
        self._helper = helper
        self._api = helper._api
        self._device_info = device_info
        if self._device_info:
            self.device_id = self._device_info.device_id
        else:
            self.device_id = device_id
        self._error_code: Optional[int] = None
        self._error_msg: Optional[str] = None

    def _set_error(self, code: int, message: str):
        self._error_code = code
        self._error_msg = message

    def _clear_error(self):
        self._error_code = None
        self._error_msg = None

    def successful(self, common_response, delay: float = 0):
        try:
            if common_response.status != 200:
                self._set_error(common_response.status, common_response.message)
                return False

            if common_response.data.code != 0:
                self._set_error(common_response.data.code, common_response.data.message)
                return False
            self._clear_error()
            time.sleep(delay)
            return True
        except Exception as e:
            self._set_error(-1, f"解析响应失败: {e}")
            return False

    @property
    def error_code(self) -> Optional[int]:
        ret = self._error_code
        self._error_code = None
        return ret

    @property
    def error_msg(self) -> Optional[str]:
        ret = self._error_msg
        self._error_msg = None
        return ret

    @property
    def mouse(self) -> Mouse:
        """
        获取鼠标控制接口。

        Returns:
            Mouse: 当前设备的鼠标控制对象，可用于执行点击、滑动等操作。
        """
        return Mouse(self)

    @property
    def key_board(self) -> KeyBoard:
        """
        获取键盘控制接口。

        Returns:
            KeyBoard: 当前设备的键盘控制对象，可用于执行键盘输入、热键等操作。
        """
        return KeyBoard(self)

    @property
    def image(self) -> Image:
        """
        获取图像接口。

        Returns:
            Image: 当前设备的图像对象，可用于执行截图、找色、找图、ocr等操作。
        """
        return Image(self)

    @property
    def shortcut(self) -> Shortcut:
        """
        获取快捷指令接口。

        Returns:
            Shortcut: 当前设备的快捷指令对象，可用于执行快捷指令里面传输照片、剪切板共享等操作。
        """
        return Shortcut(self)

    def refresh(self):
        """
        从服务器重新获取设备信息，并更新内部缓存。
        当设备状态发生变化时（如分辨率、名称等），可调用此方法同步最新信息。
        """
        ret = self._api.device_get(self.device_id)
        if self.successful(ret) and len(ret.data.device_list) > 0:
            self._device_info = ret.data.device_list[0]

    @property
    def info(self) -> DeviceInfo:
        """
        获取设备信息。

        Returns:
            DeviceInfo: 当前设备的信息对象（如名称、IP、分辨率等）。
            - 若首次访问，自动调用 refresh() 拉取信息。
        """
        if self._device_info is None:
            self.refresh()
        return self._device_info
