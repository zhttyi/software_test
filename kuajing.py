import requests

# 打印HTTP响应消息的函数
def printResponse(response):
    print('\n\n-------- HTTP response * begin -------')
    print(response.status_code)

    for k, v in response.headers.items():
        print(f'{k}: {v}')

    print('')

    print(response.content.decode('utf8'))
    print('-------- HTTP response * end -------\n\n')

import requests, json
data = {"params":param}
response = requests.post("http://118.192.69.103:8069/web/login",
                         data={
                             'login': 'admin',
                             'password': 'yatinova0827'
                         }
                         )

printResponse(response)