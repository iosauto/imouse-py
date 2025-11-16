# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="imouse-py",  # 包名
    version="0.0.4",  # 版本号
    author="iMouse",
    author_email="your_email@example.com",
    description="iMouse设备自动化控制库一个基于客户端-服务端架构的Python库,用于自动化控制iOS设备",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/iosauto/imouse-py",  # 你的 GitHub 地址
    packages=find_packages(),  # 自动查找 `iMouse` 目录下的 Python 包
    install_requires=[
        "annotated-types>=0.7.0",
        "certifi>=2025.7.9",
        "charset-normalizer>=3.4.2",
        "colorlog>=6.9.0",
        "idna>=3.10",
        "pydantic>=2.10.6",
        "pydantic_core>=2.27.2",
        "requests>=2.32.4",
        "typing_extensions>=4.13.2",
        "urllib3>=2.2.3",
        "websocket-client>=1.8.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
