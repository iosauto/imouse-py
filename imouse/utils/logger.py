import codecs
import logging
import re
import sys
import threading
import os
import inspect
from typing import Optional
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
import colorlog


# 单例日志类
class Logger:
    def __init__(self):
        self.logger = None
        self._is_debug = True
        self._log_show_thread_id = False
        self._log_show_file_and_line = False

    def init(self,
             is_debug=True,
             name='imouse',
             log_dir='logs',
             log_level=logging.INFO,
             log_show_thread_id=False,
             log_show_file_and_line=False):
        self._is_debug = is_debug
        self._log_show_thread_id = log_show_thread_id
        self._log_show_file_and_line = log_show_file_and_line

        logger = logging.getLogger(name)
        logger.setLevel(log_level)

        formatter = logging.Formatter(
            '%(asctime)s.%(msecs)03d [%(levelname)-7s] %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        color_formatter = colorlog.ColoredFormatter(
            '%(log_color)s%(asctime)s.%(msecs)03d [%(levelname)-7s] %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            log_colors={
                'DEBUG': 'cyan', 'INFO': 'green',
                'WARNING': 'yellow', 'ERROR': 'red',
                'CRITICAL': 'bold_red',
            }
        )
        # 控制台
        ch = logging.StreamHandler()
        ch.setFormatter(color_formatter)
        logger.addHandler(ch)

        if log_dir:
            os.makedirs(log_dir, exist_ok=True)
            path = os.path.join(log_dir, f"{name}.log")
            fh = RotatingFileHandler(path, maxBytes=10 * 1024 * 1024, backupCount=5,encoding='utf-8')
            fh.setFormatter(formatter)
            logger.addHandler(fh)

        self.logger = logger

    def _build_msg(self, message):
        frame = inspect.stack()[3]
        filename = inspect.getframeinfo(frame[0]).filename
        lineno = inspect.getframeinfo(frame[0]).lineno
        tid = threading.get_ident()

        prefix = ""
        if self._log_show_thread_id:
            prefix += f"[{tid}]"
        if self._log_show_file_and_line:
            prefix += f"[{os.path.basename(filename)}:{lineno}]"

        return prefix, str(message)

    def info(self, msg):
        if not self._is_debug:
            return
        prefix, msg_str = self._build_msg(msg)
        self.logger.info("%s %s", prefix, msg_str)

    def debug(self, msg):
        if not self._is_debug:
            return
        prefix, msg_str = self._build_msg(msg)
        self.logger.debug("%s %s", prefix, msg_str)

    def warning(self, msg):
        if not self._is_debug:
            return
        prefix, msg_str = self._build_msg(msg)
        self.logger.warning("%s %s", prefix, msg_str)

    def error(self, msg):
        prefix, msg_str = self._build_msg(msg)
        self.logger.error("%s %s", prefix, msg_str)

    def critical(self, msg):
        prefix, msg_str = self._build_msg(msg)
        self.logger.critical("%s %s", prefix, msg_str)


# ================= 全局管理 =================

_logger_instance: Optional[Logger] = None


def configure(**kwargs):
    """初始化并配置全局日志"""
    global _logger_instance
    if _logger_instance is None:
        _logger_instance = Logger()
    _logger_instance.init(**kwargs)


def get_logger() -> Logger:
    global _logger_instance
    if _logger_instance is None:
        _logger_instance = Logger()
        _logger_instance.init()
    return _logger_instance


# ================= 快捷调用 =================

def info(msg): get_logger().info(msg)


def debug(msg): get_logger().debug(msg)


def warning(msg): get_logger().warning(msg)


def error(msg): get_logger().error(msg)


def critical(msg): get_logger().critical(msg)
