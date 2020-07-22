#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/7/22 10:54
# file: test_department.py
import json
from datetime import datetime

import pytest
import requests

from weixin.contact.token import Weixin
import logging

class TestDepartment:
    @classmethod
    def setup_class(cls):
        print('setup class')
        Weixin.get_token()
        print(Weixin._token)

    def setup(self):
        print('setup')


    def test_create_depth(self):
        parentid = 1
        for i in range(5):
            data = {
                'name': 'nupt' + str(parentid) + str(datetime.now().timestamp()),
                'parentid': parentid
            }
            r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/department/create',
                              params={'access_token':Weixin.get_token()},
                              json = data
                              ).json()
            logging.debug(json.dumps(r, indent=2, ensure_ascii=False))
            parentid = r['id']
            assert r['errcode'] == 0

    def test_create_name(self):
        data = {
            "name": "南京邮电大学",
            "parentid": 1

        }
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/department/create',
                      params={'access_token':Weixin.get_token()},
                      json= data
                      ).json()

        logging.debug(r)

    @pytest.mark.parametrize('name', [
        "广州研发中心",
        "東京アニメーション研究所",
        "도쿄 애니메이션 연구소",
        "معهد طوكيو للرسوم المتحركة",
        "東京動漫研究所"
    ])
    def test_create_order(self, name):
        data = {
            "name": name,
            "parentid": 1,
            'order':1

        }
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/department/create',
                          params={'access_token': Weixin.get_token()},
                          json=data
                          ).json()

        assert r['errcode'] == 0


    def test_get(self):
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/department/list',
                         params={'access_token':Weixin.get_token()}
                         ).json()
        logging.debug(json.dumps(r, indent=2,ensure_ascii=False))