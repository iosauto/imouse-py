import base64
import json
import re
from typing import TypeVar, Optional, Type

from pydantic import BaseModel, ValidationError

from imouse.models import CommonResponse
from imouse.utils import logger

T = TypeVar('T', bound=BaseModel)


def parse_model(model_class: Type[T], data: dict, raise_on_fail: bool = False) -> Optional[T]:
    try:
        return model_class(**data)
    except ValidationError as ve:
        logger.error(
            f"[模型验证失败] 模型: {model_class.__name__}\n"
            f"[错误详情]: {ve}\n"
            f"[原始数据]:\n{json.dumps(data, indent=2, ensure_ascii=False)}"
        )
        if raise_on_fail:
            raise
    except Exception as e:
        logger.error(
            f"[模型初始化异常] 模型: {model_class.__name__}\n"
            f"[异常]: {e}\n"
            f"[原始数据]:\n{json.dumps(data, indent=2, ensure_ascii=False)}"
        )
        if raise_on_fail:
            raise
    return None


def file_to_base64(file_path: str) -> str:
    with open(file_path, 'rb') as f:
        binary_data = f.read()
        base64_str = base64.b64encode(binary_data).decode('utf-8')
        return base64_str


def clean_surrogates(text: str) -> str:
    """清理非法 surrogate 字符（如 \ud800 - \udfff）"""
    return re.sub(r'[\ud800-\udfff]', '?', text)


def safe_json_log(json_str: str, prefix: str = '') -> str:
    """
    安全格式化 JSON 字符串供日志输出
    - 自动解析 JSON 字符串
    - 格式化为缩进
    - 遇到非法内容不会报错
    - 保证控制台不崩溃
    """
    try:
        obj = json.loads(json_str)
        return f'{prefix}\n' + json.dumps(obj, ensure_ascii=False)
    except Exception:
        return f'{prefix}\n' + clean_surrogates(json_str)


