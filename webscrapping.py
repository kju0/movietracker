import requests
from bs4 import BeautifulSoup


'''1. 웹스크래핑'''
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#cgv 영화 가져오기
url = 'http://www.cgv.co.kr/movies/?lt=1&ft=0'
data = requests.get(url,headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 데이터로 파싱
soup = BeautifulSoup(data.text, 'html.parser')
#print(soup)

results = soup.select('div.sect-movie-chart > ol > li')

for re in results:
    img = re.select_one('div.box-image > a > span.thumb-image > img')
    title = re.select_one('div.box-contents > a > strong.title')
    detail = re.select_one('div.box-contents > a')

    #nonetype 예외처리
    if img is not None and title is not None and detail is not None:
        img_url = img['src']
        movie_title = title.text
        detail_url = detail['href']

        print("title:", movie_title)
        print("img url:", img_url)
        print("detail url:", detail_url)
        print(" ")