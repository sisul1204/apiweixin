#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/7/22 10:55
# file: test_user.py
import json
import logging
import time

import pystache
import requests

from weixin.contact.token import Weixin


class TestUser:
    depart_id = 14

    @classmethod
    def setup_class(cls):
        pass


    def test_create(self):
        uid = str(time.time())
        data = {
            'userid': uid,
            'name': uid,
            'department': [self.depart_id],
            'email': uid + '@qq.com'
        }

        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/user/create',
                          params={'access_token':Weixin.get_token()},
                          json= data
                          ).json()
        logging.debug(json.dumps(r, indent=2, ensure_ascii=False))
        assert r['errcode'] == 0

    def test_create_by_template(self):
        print(pystache.render('hello {{name}} {{#has}} world {{value}}  {{/has}}',
                              {'name': 'hogwarts',
                               'has': [{'value':1}, {'value':2}, {'value': 3}]
                               }))


    def test_list(self):
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/user/simplelist',
                         params={'access_token':Weixin.get_token(),'department_id':14}
                         ).json()

        logging.debug(json.dumps(r, indent=2, ensure_ascii=False))


    

