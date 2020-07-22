#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/7/22 10:56
# file: test_weixin.py
from unittest import TestCase

from weixin.contact.token import Weixin


class TestWeixin(TestCase):
    def test_get_token(self):
        print(Weixin.get_token())
        assert Weixin.get_token() != ''