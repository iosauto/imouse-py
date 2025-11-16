from imouse.models.response import ImServerConfigData
from imouse.types import SetDeviceParams, SetDeviceAirplayParams, MouseSwipeParams, MultiColorParams, \
    AlbumFileParams, PhoneFileParams, SendHidParams

from typing import Optional, List


class Payload:
    def _build_payload(self, fun: str, base_data: dict, extra_data: Optional[dict] = None) -> dict:
        payload = {
            "fun": fun,
            "data": base_data or {}
        }
        if extra_data:
            payload["data"].update(extra_data)
        return payload

    def device_get(self, device_id: str = '', data: dict = None) -> dict:
        return self._build_payload("/device/get", {"id": device_id}, data)

    def device_group_get(self, group_id: str = '', data: dict = None) -> dict:
        return self._build_payload("/device/group/get", {"id": group_id}, data)

    def device_group_getdev(self, group_id: str, data: dict = None) -> dict:
        return self._build_payload("/device/group/get-dev", {"id": group_id}, data)

    def device_set(self, device_id: str, params: SetDeviceParams, data: dict = None) -> dict:
        return self._build_payload("/device/set", {"id": device_id, **dict(params)}, data)

    def device_del(self, device_id: str, data: dict = None) -> dict:
        return self._build_payload("/device/del", {"id": device_id}, data)

    def device_group_set(self, group_id: str, group_name: str, data: dict = None) -> dict:
        return self._build_payload("/device/group/set", {"id": group_id, "name": group_name}, data)

    def device_group_del(self, group_id: str, data: dict = None) -> dict:
        return self._build_payload("/device/group/del", {"id": group_id}, data)

    def device_airplay_set(self, device_id: str, params: SetDeviceAirplayParams, data: dict = None) -> dict:
        return self._build_payload("/device/airplay/set", {"id": device_id, **dict(params)}, data)

    def device_airplay_connect(self, device_id: str, data: dict = None) -> dict:
        return self._build_payload("/device/airplay/connect", {"id": device_id}, data)

    def device_airplay_connect_all(self) -> dict:
        return self._build_payload("/device/airplay/connect/all", {})

    def device_airplay_disconnect(self, device_id: str, data: dict = None) -> dict:
        return self._build_payload("/device/airplay/disconnect", {"id": device_id}, data)

    def device_restart(self, device_id: str, data: dict = None) -> dict:
        return self._build_payload("/device/restart", {"id": device_id}, data)

    def device_usb_restart(self, vid_pid: str, data: dict = None) -> dict:
        return self._build_payload("/device/usb/restart", {"id": vid_pid}, data)

    def device_sort_set(self, sort_index, sort_value: int, data: dict = None) -> dict:
        return self._build_payload("/device/sort/set", {"sort_index": sort_index, "sort_value": sort_value}, data)

    def device_sort_get(self) -> dict:
        return self._build_payload("/device/sort/get", {})

    def config_usb_get(self) -> dict:
        return self._build_payload("/config/usb/get", {})

    def config_imserver_get(self) -> dict:
        return self._build_payload("/config/imserver/get", {})

    def config_imserver_set(self, params: ImServerConfigData, data: dict = None) -> dict:
        return self._build_payload("/config/imserver/set", {**dict(params)}, data)

    def imserver_regmdns(self) -> dict:
        return self._build_payload("/imserver/regmdns", {})

    def imserver_restart(self) -> dict:
        return self._build_payload("/imserver/restart", {})

    def config_user_login(self, account_number, password: str, utag: int = 1, data: dict = None) -> dict:
        return self._build_payload("/config/user/login", {"phone": account_number, "password": password, "utag": utag},
                                   data)

    def config_user_logout(self) -> dict:
        return self._build_payload("/config/user/logout", {})

    def config_user_info(self) -> dict:
        return self._build_payload("/config/user/info", {})

    def config_user_switch(self, utag: int, data: dict = None) -> dict:
        return self._build_payload("/config/user/switch", {"id": utag}, data)

    def mouse_click(self, device_id, button: str, x, y, time: int, data: dict = None) -> dict:
        return self._build_payload('/mouse/click', {"id": device_id, "button": button, "x": x, "y": y, "time": time},
                                   data)

    def mouse_swipe(self, device_id: str, params: MouseSwipeParams, data: dict = None) -> dict:
        return self._build_payload('/mouse/swipe', {"id": device_id, **dict(params)}, data)

    def mouse_up(self, device_id, button: str, data: dict = None) -> dict:
        return self._build_payload('/mouse/up', {"id": device_id, "button": button}, data)

    def mouse_down(self, device_id, button: str, data: dict = None) -> dict:
        return self._build_payload('/mouse/down', {"id": device_id, "button": button}, data)

    def mouse_move(self, device_id: str, x, y: int, data: dict = None) -> dict:
        return self._build_payload('/mouse/move', {"id": device_id, "x": x, "y": y}, data)

    def mouse_reset(self, device_id: str) -> dict:
        return self._build_payload('/mouse/reset', {"id": device_id})

    def mouse_wheel(self, device_id, direction: str, len, number: int, data: dict = None) -> dict:
        return self._build_payload('/mouse/wheel',
                                   {"id": device_id, "direction": direction, "len": len, "number": number}, data)

    def key_sendkey(self, device_id, key, fn_key: str, data: dict = None) -> dict:
        return self._build_payload('/key/sendkey',
                                   {"id": device_id, "key": key, "fn_key": fn_key}, data)

    def key_sendhid(self, device_id: str, command_list: List[SendHidParams], data: dict = None) -> dict:
        return self._build_payload('/key/sendhid',
                                   {"id": device_id, "list": command_list}, data)

    def pic_screenshot(self, device_id: str, is_jpg: bool, rect: List[int], data: dict = None) -> dict:
        return self._build_payload('/pic/screenshot',
                                   {"id": device_id, "jpg": is_jpg, "rect": rect, "binary": True}, data)

    def pic_find_image(self, device_id: str, img_list: List[str], similarity: float, all: bool, rect: List[int],
                       delta_color: str, direction: str,
                       data: dict = None) -> dict:
        return self._build_payload('/pic/find-image',
                                   {"id": device_id, "img_list": img_list, "similarity": similarity, "all": all,
                                    "rect": rect, "delta_color": delta_color, "direction": direction}, data)

    def pic_find_image_cv(self, device_id: str, img_list: List[str], similarity: float, all, same: bool,
                          rect: List[int],
                          data: dict = None) -> dict:
        return self._build_payload('/pic/find-image-cv',
                                   {"id": device_id, "img_list": img_list, "similarity": similarity, "all": all,
                                    "rect": rect, "same": same}, data)

    def pic_ocr(self, device_id: str, rect: List[int], is_ex: bool,
                data: dict = None) -> dict:
        fun_str = "/pic/ocr-ex" if is_ex else "/pic/ocr"
        return self._build_payload(fun_str, {"id": device_id, "rect": rect}, data)

    def pic_find_text(self, device_id: str, text_list: List[str], similarity: float, contain: bool, rect: List[int],
                      is_ex: bool,
                      data: dict = None) -> dict:
        fun_str = "/pic/find-text-ex" if is_ex else "/pic/find-text"
        return self._build_payload(fun_str,
                                   {"id": device_id, "text": text_list, "similarity": similarity, "contain": contain,
                                    "rect": rect}, data)

    def pic_find_multi_color(self, device_id: str, params: List[MultiColorParams], all, same: bool,
                             data: dict = None) -> dict:
        return self._build_payload("/pic/find-multi-color",
                                   {"id": device_id, "all": all, "same": same, "list": params}, data)

    def shortcut_album_get(self, device_id, album_name: str, num: int, outtime: int,
                           data: dict = None) -> dict:
        return self._build_payload("/shortcut/album/get",
                                   {"id": device_id, "album_name": album_name, "num": num, "outtime": outtime}, data)

    def shortcut_album_upload(self, device_id, album_name: str, files: List[str], is_zip: bool, outtime: int,
                              data: dict = None) -> dict:
        return self._build_payload("/shortcut/album/upload",
                                   {"id": device_id, "album_name": album_name, "zip": int(is_zip), "files": files,
                                    "outtime": outtime}, data)

    def shortcut_album_down(self, device_id: str, files: List[AlbumFileParams], is_zip: bool, outtime: int,
                            data: dict = None) -> dict:
        return self._build_payload("/shortcut/album/down",
                                   {"id": device_id, "zip": int(is_zip), "list": files,
                                    "outtime": outtime}, data)

    def shortcut_album_del(self, device_id: str, files: List[AlbumFileParams], outtime: int,
                           data: dict = None) -> dict:
        return self._build_payload("/shortcut/album/del",
                                   {"id": device_id, "list": files,
                                    "outtime": outtime}, data)

    def shortcut_album_clear(self, device_id, album_name: str, outtime: int,
                             data: dict = None) -> dict:
        return self._build_payload("/shortcut/album/clear",
                                   {"id": device_id, "album_name": album_name,
                                    "outtime": outtime}, data)

    def shortcut_file_get(self, device_id, path: str, outtime: int,
                          data: dict = None) -> dict:
        return self._build_payload("/shortcut/file/get",
                                   {"id": device_id, "path": path, "outtime": outtime}, data)

    def shortcut_file_upload(self, device_id, path: str, is_zip: bool, files: List[str], outtime: int,
                             data: dict = None) -> dict:
        return self._build_payload("/shortcut/file/upload",
                                   {"id": device_id, "path": path, "zip": int(is_zip), "files": files,
                                    "outtime": outtime}, data)

    def shortcut_file_down(self, device_id, path: str, is_zip: bool, files: List[PhoneFileParams], outtime: int,
                           data: dict = None) -> dict:
        return self._build_payload("/shortcut/file/down",
                                   {"id": device_id, "zip": int(is_zip), "path": path, "list": files,
                                    "outtime": outtime}, data)

    def shortcut_file_del(self, device_id, path: str, files: List[PhoneFileParams], outtime: int,
                          data: dict = None) -> dict:
        return self._build_payload("/shortcut/file/del",
                                   {"id": device_id, "path": path, "list": files,
                                    "outtime": outtime}, data)

    def shortcut_clipboard_set(self, device_id, text: str, sleep: int, outtime: int,
                               data: dict = None) -> dict:
        return self._build_payload("/shortcut/clipboard/set",
                                   {"id": device_id, "text": text, "sleep": sleep,
                                    "outtime": outtime}, data)

    def shortcut_clipboard_get(self, device_id: str, outtime: int,
                               data: dict = None) -> dict:
        return self._build_payload("/shortcut/clipboard/get",
                                   {"id": device_id,
                                    "outtime": outtime}, data)

    def shortcut_exec_url(self, device_id, url: str, outtime: int,
                          data: dict = None) -> dict:
        return self._build_payload("/shortcut/exec/url",
                                   {"id": device_id, "url": url,
                                    "outtime": outtime}, data)

    def shortcut_switch_device(self, device_id, state: int, outtime: int,
                               data: dict = None) -> dict:
        return self._build_payload("/shortcut/switch/device",
                                   {"id": device_id, "state": state,
                                    "outtime": outtime}, data)

    def shortcut_switch_bril(self, device_id, state: float, outtime: int,
                             data: dict = None) -> dict:
        return self._build_payload("/shortcut/switch/bril",
                                   {"id": device_id, "state": state,
                                    "outtime": outtime}, data)

    def shortcut_switch_torch(self, device_id, state: int, outtime: int,
                              data: dict = None) -> dict:
        return self._build_payload("/shortcut/switch/torch",
                                   {"id": device_id, "state": state,
                                    "outtime": outtime}, data)

    def shortcut_switch_flight(self, device_id, state: int, outtime: int,
                               data: dict = None) -> dict:
        return self._build_payload("/shortcut/switch/flight",
                                   {"id": device_id, "state": state,
                                    "outtime": outtime}, data)

    def shortcut_switch_cdpd(self, device_id, state: int, outtime: int,
                             data: dict = None) -> dict:
        return self._build_payload("/shortcut/switch/cdpd",
                                   {"id": device_id, "state": state,
                                    "outtime": outtime}, data)

    def shortcut_switch_wlan(self, device_id, state: int, outtime: int,
                             data: dict = None) -> dict:
        return self._build_payload("/shortcut/switch/wlan",
                                   {"id": device_id, "state": state,
                                    "outtime": outtime}, data)

    def shortcut_device_ip(self, device_id, state: int, outtime: int,
                           data: dict = None) -> dict:
        return self._build_payload("/shortcut/device/ip",
                                   {"id": device_id, "state": state,
                                    "outtime": outtime}, data)
