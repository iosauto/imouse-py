from typing import Dict, List, Callable, Any, Set, Optional
from threading import RLock

from imouse.models import DeviceListResponse, DeviceListData, GroupListData, UsbListData, UserData, \
    ImServerConfigResponse, ImServerConfigData
from imouse.types import EventConstant
from imouse.utils.utils import parse_model


class EventDispatcher:
    def __init__(self):
        self._events = {}

    def on(self, event_name):
        """装饰器：绑定事件"""

        def decorator(func):
            self._events.setdefault(event_name, []).append(func)
            return func

        return decorator

    def _emit(self, event_name, *args, **kwargs):
        """触发事件"""
        for handler in self._events.get(event_name, []):
            handler(*args, **kwargs)

    def emit(self, event_message: dict):
        fun = event_message.get('fun')
        if not fun:
            return False
        data = event_message.get('data', {})

        if fun == EventConstant.IM_CONNECT:
            self._emit(fun, data.get("ver"))
        elif fun == EventConstant.IM_DISCONNECT or fun == EventConstant.LOGOUT:
            self._emit(fun, )
        elif fun == EventConstant.DEV_CONNECT or fun == EventConstant.DEV_DISCONNECT or fun == EventConstant.DEV_ROTATE or fun == EventConstant.DEV_CHANGE:
            ret = parse_model(DeviceListData, data)
            self._emit(fun, ret.device_list[0])
        elif fun == EventConstant.DEV_DELETE or fun == EventConstant.GROUP_DELETE:
            self._emit(fun, data.get("list"))
        elif fun == EventConstant.GROUP_CHANGE:
            ret = parse_model(GroupListData, data)
            self._emit(fun, ret.group_list[0].id, ret.group_list[0].name)
        elif fun == EventConstant.USB_CHANGE:
            ret = parse_model(UsbListData, data)
            self._emit(fun, ret.usb_list[0])
        elif fun == EventConstant.AIRPLAY_CONNECT_LOG or fun == EventConstant.IM_LOG:
            self._emit(fun, data.get("message"))
        elif fun == EventConstant.USER_INFO:
            ret = parse_model(UserData, data)
            self._emit(fun, ret)
        elif fun == EventConstant.ERROR_PUSH:
            self._emit(fun, data.get("message"), data.get("call_fun"))
        elif fun == EventConstant.IM_CONFIG_CHANGE:
            self._emit(fun, parse_model(ImServerConfigData, data))
        elif fun == EventConstant.DEV_SORT_CHANGE:
            self._emit(fun, data.get("sort_index"), data.get("sort_value"))


event = EventDispatcher()
