from enum import Enum
from typing import TypedDict, List, Union


class SetDeviceParams(TypedDict, total=False):
    name: str
    vid: str
    pid: str
    location: str
    location_crc: str
    gid: str


class SetDeviceAirplayParams(TypedDict, total=False):
    ratio: int
    refresh: int
    fps: int
    audio: int
    img_fps: int


class MouseSwipeParams(TypedDict, total=False):
    button: str
    direction: str
    len: float
    step_sleep: int
    steping: int
    brake: bool
    sx: int
    sy: int
    ex: int
    ey: int


class MultiColorParams(TypedDict, total=False):
    first_color: str
    rect: List[int]
    similarity: float


class AlbumFileParams(TypedDict):
    album_name: str
    name: str
    ext: str


class PhoneFileParams(TypedDict):
    name: str
    ext: str

class SendHidParams(TypedDict):
    delayed: int
    key: str


class FunctionKeys(Enum):
    HOME = "WIN+h"  # 主页键
    GO_BACK = "TAB+b"  # 返回键
    APP_SWITCHER = "AppSwitch"  # app切换器
    CONTROL_CENTER = "ControlBar"  # 控制中心
    NOTIFICATION_CENTER = "NoticeBar"  # 通知中心
    LOCK_SCREEN = "TAB+l"  # 锁屏
    OPEN_ONSCREEN_KEYBOARD = "OPENKeyboard"  # 打开屏幕键盘
    SCREENSHOT = "shift+win+3"  # 截屏
    SCREENSHOT_EDIT = "shift+win+4"  # 截屏并编辑
    RESTART = "CTRL+ALT+SHIFT+WIN+r"  # 重新启动
    PASS_THROUGH_MODE = "CTRL+ALT+WIN+p"  # 直通模式
    COPY = "WIN+c"  # 复制
    PASTE = "WIN+v"  # 粘贴
    SELECT_ALL = "WIN+a"  # 全选
    CUT = "WIN+x"  # 剪切
    INPUT_METHOD = "SwitchIme"  # 输入法切换
    BACKSPACE = "BACKSPACE"  # 退格键
    SPACE = " "  # 空格键
    TAB = "TAB"  # Tab 键
    ENTER = "ENTER"  # 回车键
    UP_ARROW = "UpArrow"  # 方向键：上
    DOWN_ARROW = "DownArrow"  # 方向键：下
    LEFT_ARROW = "LeftArrow"  # 方向键：左
    RIGHT_ARROW = "RightArrow"  # 方向键：右
    MUTE_SOUND_SWITCH = "MuteSoundSwitch"  # 静音切换
    VOLUME_UP = "VolumeUp"  # 增加音量
    VOLUME_DOWN = "VolumeDown"  # 减小音量
    PLAY_PAUSE = "Play/Pause"  # 播放/暂停
    SPOT_LIGHT = "WIN+ " # 聚焦搜索


class EventConstant:
    IM_CONNECT = 'im_connect'  # 连接内核成功
    IM_DISCONNECT = 'im_disconnect'  # 连接内核断开
    DEV_CONNECT = 'dev_connect'  # 有设备连接
    DEV_DISCONNECT = 'dev_disconnect'  # 有设备断开
    DEV_ROTATE = 'dev_rotate'  # 有设备旋转
    DEV_CHANGE = 'dev_change'  # 有设备改变
    DEV_DELETE = 'dev_delete'  # 有设备删除
    GROUP_CHANGE = 'group_change'  # 有分组改变
    GROUP_DELETE = 'group_delete'  # 有分组删除
    USB_CHANGE = 'usb_change'  # 有 USB 改变
    COLLECTION_MOUSE = 'collection_mouse'  # 采集鼠标参数状态
    AIRPLAY_CONNECT_LOG = 'airplay_connect_log'  # 自动投屏日志
    RESTART_LOG = 'restart_log'  # 调用重启手机的日志
    USER_INFO = 'user_info'  # 用户信息状态30秒左右会来一次
    IM_LOG = 'im_log'  # 内核日志,比如超出授权等
    ERROR_PUSH = 'error_push'  # 错误日志推送,比如出现未知的错误
    IM_CONFIG_CHANGE = 'im_config_change'  # 内核配置改变
    LOGOUT = 'logout'  # 账号退出登录
    DEV_SORT_CHANGE = 'dev_sort_change'  # 设备列表排序改变
