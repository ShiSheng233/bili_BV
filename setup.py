# -*- coding: UTF-8 -*-
import setuptools

with open("README.md","r",encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="biliBV",
    version="1.0.0",
    author="ShiSheng",
    author_email="shisheng233@dingtalk.com",
    description="A Python Lirary that you can encode av-number to BV-string or decode BV-string.",
    license = "WTFPL",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ShiSheng233/bili_BV",
    packages=setuptools.find_packages(),
    python_requires='>=3.5',
)