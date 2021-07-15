import bs4

import requests

# 추가 입력됨.
res = requests.get('www.google.com')

if res.status_code == 200:
    pass