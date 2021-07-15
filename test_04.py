import bs4

import requests

# 추가 입력됨. B : google.com, A : www.naver.com
res = requests.get('www.naver.com') # A

if res.status_code == 300: # A
    pass
    first = 2