# 🖱️ iMouse - iOS 设备自动化控制库

> 一个基于客户端-服务端架构的 Python 库，用于自动化控制 iOS 设备。  
> **只适用于 iMouse XP 版，需配套专用硬件使用。**

---

## ⚠️ 使用说明（请务必阅读）

- 本项目仅适用于 **iMouse XP 版**，支持标准 iOS 无越狱环境直接控制,无需安装第三方插件和APP。
- 必须使用配套的iMouse硬件才能完成控制操作。

**官网地址** 👉 [https://www.imouse.cc](https://www.imouse.cc)  
**淘宝购买硬件** 👉 [https://imouse.taobao.com](https://imouse.taobao.com)

- **GitHub** https://github.com/iosauto/imouse-py
- **Gitee** https://gitee.com/iosusb/imouse-py

---

## 🚀 快速开始

- 使用前先使用pip安装imouse-py包
- pip install imouse-py

## 使用api类基础接口调用

```python
import imouse
from imouse.types import MouseSwipeParams

# 连接到 iMouse 服务端（默认地址为 localhost）
api = imouse.api(host="localhost")  # 获取api实例,所有iMouse提供的接口都在api实例里面调用

# 通过api类里面的方法执行鼠标操作
api.mouse_click("FA:9E:10:3A:FE:E8", "", 100, 100)  # 左键点击屏幕坐标 (100, 100)
api.mouse_swipe("FA:9E:10:3A:FE:E8", params=MouseSwipeParams(  # 向上滑动屏幕,从屏幕下百分之10滑动到屏幕的百分之90
    direction='up',  # 
    len=0.9
))

```

## 通过helper类更简单的调用(推荐使用)

### console 提供的 API

提供对设备管理和全局操作的访问:

- **Device**: 设备管理
- **AirPlay**: 投屏连接和配置
- **USB**: imouse硬件管理
- **Group**: 分组管理
- **ImConfig**: iMouse全局配置管理
- **User**: iMouse账户管理

```python
import imouse

# 连接到 iMouse 服务端（默认地址为 localhost）
api = imouse.api(host="localhost")  # 获取api实例

helper = imouse.helper(api)  # 获取helper类实例

console = helper.console  # 获取控制台实例
ret = console.device.list_by_id()  # 获取所有设备列表
print(ret)
# 投屏指定设备
ret = console.airplay.connect('FA:9E:10:3A:FE:E8,FD:9E:10:3A:FE:E0')
if ret:
    print('成功')
else:
    print(f'失败:{console.error_msg}')

# 断开指定设备投屏
ret = console.airplay.disconnect('FA:9E:10:3A:FE:E8,FD:9E:10:3A:FE:E0')
if ret:
    print('成功')
else:
    print(f'失败:{console.error_msg}')

# 投屏所有离线设备
ret = console.airplay.connect_all()
if ret:
    print('成功')
else:
    print(f'失败:{console.error_msg}')
```

### device 提供的 API

提供对单个设备的控制:

- **Image**: 设备图像操作,比如截图、找图、文字识别等
- **KeyBoard**: 键盘操作
- **Mouse**: 鼠标操作
- **Shortcut**: 快捷指令操作

```python
import imouse
from imouse.utils import file_to_base64
from imouse.types import MouseSwipeParams

# 连接到 iMouse 服务端（默认地址为 localhost）
api = imouse.api(host="localhost")  # 获取api实例

helper = imouse.helper(api)  # 获取helper类实例

device = helper.device('FA:9E:10:3A:FE:E8')  # 通过设备id获取设备实例

# 也可以通过devices方法获取所有实例列表
# device_list = helper.devices()
# device = device_list[0]

# 截图
ret = device.image.screenshot()
if ret:
    print('截图成功')
    with open('test.bmp', "wb") as f:
        f.write(ret)
else:
    print(f'截图失败:{device.error_msg}')

# 通过opencv找图
img_str = file_to_base64("test1.bmp")
ret = device.image.find_image_cv([img_str])
if len(ret) > 0:
    print(f"找图成功[{ret[0].centre[0]},{ret[0].centre[1]}]")
else:
    print(f'找图失败:{device.error_msg}')

# 向上滑动屏幕
ret = device.mouse.swipe(MouseSwipeParams(direction='up', len=0.9))  # 从屏幕下百分之10滑动到屏幕的百分之90
if ret:
    print('滑动成功')
else:
    print(f'滑动失败:{device.error_msg}')

```

### iMouse事件处理

```python
from typing import List
import imouse
from imouse.api import event
from imouse.models import DeviceInfo, UsbInfo, UserData, ImServerConfigData


@event.on("im_connect")
def im_connect(ver: str):
    print(f"[事件]连接内核成功: {ver}")


@event.on("im_disconnect")
def im_disconnect():
    print(f"[事件]与内核断开连接")


@event.on("dev_connect")
def dev_connect(device_info: DeviceInfo):
    print("[事件]有设备连接" + device_info.device_id)


@event.on("dev_disconnect")
def dev_disconnect(device_info: DeviceInfo):
    print("[事件]有设备断开连接->" + device_info.device_id)


@event.on("dev_rotate")
def dev_rotate(device_info: DeviceInfo):
    print("[事件]有设备发生旋转->" + device_info.device_id)


@event.on("dev_change")
def dev_change(device_info: DeviceInfo):
    print("[事件]有设备改变->" + device_info.device_id)


@event.on("dev_delete")
def dev_delete(deviceid_list: List[str]):
    print(f"[事件]有设备删除->{deviceid_list}")


@event.on("group_change")
def group_change(gid: str, name: str):
    print(f"[事件]有分组改变->{gid},{name}")


@event.on("group_change")
def group_change(gid: str, name: str):
    print(f"[事件]有分组改变->{gid},{name}")


@event.on("group_delete")
def group_delete(gid_list: List[str]):
    print(f"[事件]有分组删除->{gid_list}")


@event.on("usb_change")
def usb_change(usb_info: UsbInfo):
    print(f"[事件]有usb设备改变->{usb_info}")


@event.on("airplay_connect_log")
def airplay_connect_log(message: str):
    print(f"[事件]自动投屏日志->{message}")


@event.on("user_info")
def user_info(data: UserData):
    print(f"[事件]用户信息状态->{data}")


@event.on("im_log")
def im_log(message: str):
    print(f"[事件]iMouse事件->{message}")


@event.on("error_push")
def error_push(message: str, call_fun: str):
    print(f"[事件]iMouse错误日志->{message},{call_fun}")


@event.on("im_config_change")
def im_config_change(config: ImServerConfigData):
    print(f"[事件]iMouse内核配置改变->{config}")


@event.on("logout")
def logout():
    print(f"[事件]iMouse账号退出-")


@event.on("dev_sort_change")
def dev_sort_change(sort_index: int, sort_value: int):
    print(f"[事件]iMouse设备列表排序改变->{sort_index},{sort_value}")


api = imouse.api(host='192.168.9.9')

```

### 配置iMouse日志输出

```python
import logging
from imouse.utils import logger

logger.configure(
    is_debug=True,  # 是否启用调试日志（False 时 info/debug 不输出）
    name='imouse',  # 日志名称（会影响 logger 名称和日志文件名）
    log_dir='logs',  # 日志目录（默认 logs 文件夹）
    log_level=logging.DEBUG,  # 日志等级
    log_show_thread_id=False,  # 是否显示线程 ID
    log_show_file_and_line=False  # 是否显示文件和行号
)
```

