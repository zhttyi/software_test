# -*- coding: utf-8 -*-
import requests
import pprint
import json

proxies = {
  'http': 'http://127.0.0.1:8888',
  'https': 'http://127.0.0.1:8888',
}
#
# response = requests.get('http://mirrors.sohu.com/',
#         proxies=proxies)
# response = requests.get('http://httpbin.org/post',
#         proxies=proxies)
response = requests.post("http://httpbin.org/post", data={1:1,2:2})

obj = json.loads(response.content.decode('utf8'))
print(obj)
# print(type(response.headers))

# pprint.pprint(dict(response.headers))
# # print(response.text)