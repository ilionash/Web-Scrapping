"""
requirements.txt 파일 참조
  requests == 2.24.0
  beautiful4 == 4.9.1
"""

import requests
from bs4 import BeautifulSoup

# 스크래핑 하려는 url 저장
url = "https://www.indeed.com/jobs?q=python&limit=50"

# url에 저장된 웹사이트를 requestsdml get Function을 사용하여 가져오기
indeed_result = requests.get(url)

# # html을 text로 가져오기
# print(indeed_result.text)

# bs4를 이용하여 "Indeed" 검색 결과를 html로 가져오기
indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')


# "div" Tag 중 Class가 "pagination"인 것 가져오기 
pagination = indeed_soup.find("div", {"class" : "pagination"})

# "pagination" 변수에 저장된 html 중에서 "anchor" Tag 인 것 모두 가져와서 리스트로 저장
pages = pagination.find_all("a")

# span을 저장할 빈 리스트 객체 생성
spans = []

# "pages" 리스트에 저장된 값을 차례대로 "page"라는 객체로 받아온 후 "span" Tag 인 것을 "spans" 리스트에 추가
for page in pages:
  spans.append(page.find("span"))

# # "spans" 리스트에 저장된 값 중 마지막에서 1번째 item
# print(spans[-1])

# "spans" 리스트에 저장된 값 중 마지막 값을 제외하고 가져온 후 다시 spans에 넣기
spans = spans[:-1]