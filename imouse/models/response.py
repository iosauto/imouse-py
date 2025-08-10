from pydantic import BaseModel, Field
from typing import List, Optional


class CommonResponseBase(BaseModel):
    status: int
    message: str
    msgid: int
    fun: str


class CommonResData(BaseModel):
    code: int
    id: str
    message: str


class DeviceInfo(BaseModel):
    rotate: int
    state: int
    imgw: int
    imgh: int
    gid: int
    air_ratio: int
    air_fps: int
    air_refresh: int
    air_img_fps: int
    air_audio: int
    name: str
    srv_name: str
    width: str
    height: str
    ip: str
    mac: str
    user_name: str
    version: str
    model: str
    device_id: str = Field(..., alias="deviceid")
    device_name: str
    location: str
    location_crc: str
    vid: str
    pid: str
    uid: str
    gname: str
    uver: str


class GroupInfo(BaseModel):
    id: str
    name: str


class UsbInfo(BaseModel):
    vid: str
    pid: str
    uid: str
    ver: str
    state: int


class UserInfo(BaseModel):
    total_license: int
    create_time: int
    overdue_time: int
    user_state: int
    dev_num: int
    dev_online_num: int
    utag: int
    phone: str


class DeviceListData(CommonResData):
    device_list: Optional[List[DeviceInfo]] = Field(default=None, alias='list')


class DeviceListResponse(CommonResponseBase):
    data: DeviceListData


class GroupListData(CommonResData):
    group_list: Optional[List[GroupInfo]] = Field(default=None, alias='list')


class GroupListResponse(CommonResponseBase):
    data: GroupListData


class IdListData(CommonResData):
    id_list: Optional[List[str]] = Field(default=None, alias='list')


class IdListResponse(CommonResponseBase):
    data: IdListData


class CommonResponse(CommonResponseBase):
    data: CommonResData


class DeviceSortData(CommonResData):
    sort_index: Optional[int] = Field(default=None)
    sort_value: Optional[int] = Field(default=None)


class DeviceSortResponse(CommonResponseBase):
    data: DeviceSortData


class UsbListData(CommonResData):
    usb_list: Optional[List[UsbInfo]] = Field(default=None, alias='list')


class UsbListResponse(CommonResponseBase):
    data: UsbListData


class ImServerConfigData(CommonResData):
    air_play_name: Optional[str] = None
    lang: Optional[str] = None
    mdns_type: Optional[int] = None
    connect_failed_retry: Optional[int] = None
    air_play_ratio: Optional[int] = None
    opencv_num: Optional[int] = None
    ocr_num: Optional[int] = None
    allow_ip_list: Optional[List[str]] = Field(default=None)
    lang_list: Optional[List[str]] = Field(default=None)
    air_play_fps: Optional[int] = None
    air_play_img_fps: Optional[int] = None
    air_play_refresh_rate: Optional[int] = None
    air_play_port: Optional[int] = None
    air_play_audio: Optional[bool] = None
    auto_connect: Optional[bool] = None
    auto_updata: Optional[bool] = None
    thread_mode: Optional[bool] = None
    mouse_mode: Optional[bool] = None
    flip_right: Optional[bool] = None
    enable_hardware_acceleration: Optional[bool] = None


class ImServerConfigResponse(CommonResponseBase):
    data: ImServerConfigData


class UserData(CommonResData, UserInfo):
    pass


class UserResponse(CommonResponseBase):
    data: UserData


class FindImageResult(BaseModel):
    index: int
    centre: List[int]
    rect: List[int]


class FindImageResultListData(CommonResData):
    result_list: Optional[List[FindImageResult]] = Field(default=None, alias='list')


class FindImageResultResponse(CommonResponseBase):
    data: FindImageResultListData


class FindImageCvResult(FindImageResult):
    similarity: float


class FindImageCvResultListData(CommonResData):
    result_list: Optional[List[FindImageCvResult]] = Field(default=None, alias='list')


class FindImageCvResultResponse(CommonResponseBase):
    data: FindImageCvResultListData


class OcrResult(BaseModel):
    text: str
    centre: List[int]
    rect: List[int]
    similarity: float


class OcrResultListData(CommonResData):
    result_list: Optional[List[OcrResult]] = Field(default=None, alias='list')


class OcrResultResponse(CommonResponseBase):
    data: OcrResultListData


class FindMultiColorResult(BaseModel):
    index: int
    centre: List[int]


class FindMultiColorResultListData(CommonResData):
    result_list: Optional[List[FindMultiColorResult]] = Field(default=None, alias='list')


class FindMultiColorResponse(CommonResponseBase):
    data: FindMultiColorResultListData


class FileResult(BaseModel):
    name: str
    ext: str
    size: str
    create_time: str


class AlbumFileResult(FileResult):
    album_name: str


class AlbumFileResultListData(CommonResData):
    result_list: Optional[List[AlbumFileResult]] = Field(default=None, alias='list')


class AlbumFileResponse(CommonResponseBase):
    data: AlbumFileResultListData


class PhoneFileResultListData(CommonResData):
    result_list: Optional[List[FileResult]] = Field(default=None, alias='list')


class PhoneFileResponse(CommonResponseBase):
    data: PhoneFileResultListData


class ResultTextData(CommonResData):
    text: Optional[str] = None


class ResultTextResponse(CommonResponseBase):
    data: ResultTextData
