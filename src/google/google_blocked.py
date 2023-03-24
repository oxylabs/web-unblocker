import requests
import bs4

keyword = "shoes"
url = f"https://google.com/search?q={keyword}"


request_result = requests.get(url)
soup = bs4.BeautifulSoup(request_result.text, "lxml")
search_headings = soup.find_all("h3")
for info in search_headings:
    print(info.getText())
