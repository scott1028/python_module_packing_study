# coding:utf-8

#!/usr/bin/env python

from distutils.core import setup

setup(name='MyTestModule',  # 通常會跟 packages 的內容命名類似
      version='1.0',
      description='Python Distribution Utilities',
      author='Greg Ward',
      author_email='gward@python.net',
      url='http://www.python.org/sigs/distutils-sig/',
      packages=['my_module'],		# 將會把 my_module 的資料夾 copy 到 site-packages/* 下。並且更新 Distutils-1.0-py2.7.egg-info 文件
      								# 資料夾內記得要放 __init__.py 否則無法讀取到
     )
