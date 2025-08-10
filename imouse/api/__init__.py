import json
from typing import Union

from .event_dispatcher import *
from .payload import *
import time
from .client import Client
from .config import Config
from .device import Device
from .mouse_key import MouseKey
from imouse.utils import logger
from .pic import Pic
from .shortcut import Shortcut
from .user import User


class API(Client, Device, Config, User, MouseKey, Pic, Shortcut):
    def __init__(self, host: str, imouse_call_back=None, timeout: int = 15):
        super().__init__(host, timeout)
        self._imouse_call_back = imouse_call_back
        self._payload = Payload()
        self._start()

    def _start(self):
        super().start()
        time.sleep(1)
        while not self.is_connected():
            logger.debug(f'连接失败,延时1秒等待')
            time.sleep(1)

    def _handle_message(self, message: str):
        try:
            event.emit(json.loads(message))
        except Exception as e:
            logger.error(f'_handle_message发生异常: {e}')

    def _call_api(self, request_dict: dict, timeout: int = 0, is_async: bool = False) -> Union[dict, bytes, None]:
        ret = self._network_request(json.dumps(request_dict), timeout, is_async)
        if ret is not None:
            if isinstance(ret, str):
                return json.loads(ret)
            else:
                return ret
        return ret

    def _get_payload(self) -> Payload:
        pass
