import bs4

import requests

# 추가 입력됨. B : google.com, A: www.naver.com
res = requests.get('www.google.com') # B

if res.status_code == 200: # B
    pass

# 추가 입력됨.
requests.get('www.naver.com')