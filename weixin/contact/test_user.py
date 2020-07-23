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
        uid = 'nupt' + str(time.time())
        data = self.get_user({'name':uid, 'title':'六代目火影', 'email':'111@qq.com'})
        data = data.encode('utf-8')
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/user/create',
                          params={'access_token': Weixin.get_token()},
                          data=data,
                          headers={'content-type':'application/json;charset=UTF-8'}
                          ).json()
        logging.debug(json.dumps(r, indent=2, ensure_ascii=False))
        assert r['errcode'] == 0


    def test_list(self):
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/user/simplelist',
                         params={'access_token':Weixin.get_token(),'department_id':14}
                         ).json()

        logging.debug(json.dumps(r, indent=2, ensure_ascii=False))


    def get_user(self,dct):
        template = ''.join(open('user_create.json', encoding='utf-8').readlines())
        # logging.debug(template)
        return pystache.render(template, dct)

    def test_get_user(self):
        logging.debug(self.get_user({'name':'naruto', 'title':'火影', 'email':'111@qq.com'}))



    

