#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author:sisul
# time: 2020/7/21 17:22
# file: test_requests.py
import requests
import logging
import pytest
import json
import jsonpath

class TestRequests:
    logging.basicConfig(level=logging.INFO)
    url = 'https://testerhome.com/api/v3/topics.json?limit=2'
    def test_get(self):
        r = requests.get(self.url,proxies={'https':'http://127.0.0.1:8888',
                                           'http':'http://127.0.0.1:8888'},
                         verify=False)
        logging.info(r)
        logging.info(r.text)
        logging.info(json.dumps(r.json(), indent=2))

    def test_post(self):
        r = requests.get(self.url,
                         params={'a':1, 'b':'string content'},
                         headers={'a':'1', 'b':'b2'},
                         proxies={'https':'http://127.0.0.1:8888',
                                  'http':'http://127.0.0.1:8888'},
                         verify=False
                         )
        logging.info(r.url)
        logging.info(r.text)
        logging.info(json.dumps(r.json(), indent=2))
