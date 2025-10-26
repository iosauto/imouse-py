from typing import TYPE_CHECKING, List, Optional

from ...models import DeviceSortData

if TYPE_CHECKING:
    from . import Console
    from imouse import API


class ImConfig():
    def __init__(self, console: "Console"):
        self._console = console
        self._api: "API" = console._helper._api

    @property
    def device_sort(self) -> Optional[DeviceSortData]:
        """获取设备列表排序"""
        ret = self._api.device_sort_get()
        if not self._console.successful(ret):
            return None
        return ret.data

    def set_device_sort(self, index, value: int) -> Optional[DeviceSortData]:
        """设置设备列表排序"""
        ret = self._api.device_sort_set(index, value)
        if not self._console.successful(ret):
            return None
        return ret.data


    @property
    def language(self) -> Optional[str]:
        """获取控制台显示语言"""
        config = self._console.get_imserver_config
        if config is None:
            return None
        return config.lang

    @language.setter
    def language(self, value: str):
        """设置控制台语言"""
        config = self._console.get_imserver_config
        config.lang = value
        if not self._console.successful(self._api.config_imserver_set(config)):
            raise ValueError("语言设置失败")

    @property
    def language_list(self) -> List[str]:
        """获取控制台支持语言列表"""
        config = self._console.get_imserver_config
        return config.lang_list

    def auto_updata(self,state: bool)->bool:
        """设置是否自动升级"""
        config = self._console.get_imserver_config
        config.auto_updata = state
        return self._console.successful(self._api.config_imserver_set(config))


    def thread_mode(self,state: bool)->bool:
        """设置启用线程模式批量控制"""
        config = self._console.get_imserver_config
        config.thread_mode = state
        return self._console.successful(self._api.config_imserver_set(config))

    def mouse_mode(self,state: bool)->bool:
        """设置是否使用快准狠鼠标模式"""
        config = self._console.get_imserver_config
        config.mouse_mode = state
        return self._console.successful(self._api.config_imserver_set(config))

    def flip_right(self,state: bool)->bool:
        """设置横屏向右翻转"""
        config = self._console.get_imserver_config
        config.flip_right = state
        return self._console.successful(self._api.config_imserver_set(config))

