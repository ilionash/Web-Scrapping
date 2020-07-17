"""
requirements.txt 파일 참조
  requests == 2.24.0
"""

import requests

# 스크래핑 하려는 url 저장
url = "https://www.indeed.com/jobs?q=python&limit=50"

# url에 저장된 웹사이트를 requestsdml get Function을 사용하여 가져오기
indeed_result = requests.get(url)

# html을 text로 가져오기
print(indeed_result.text)