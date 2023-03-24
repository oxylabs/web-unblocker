import requests
import bs4
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


url = "https://www.google.com/search?q={}&start={}"

proxies = {
    "http": "http://USERNAME:PASSWORD@unblock.oxylabs.io:60000",
    "https": "http://USERNAME:PASSWORD@unblock.oxylabs.io:60000",
}

headers = {"x-oxylabs-geo-location": "New York,New York,United States"}


def parse(page_url):
    response = requests.get(page_url, proxies=proxies, verify=False, headers=headers)
    soup = bs4.BeautifulSoup(response.text, "lxml")
    header = soup.find("div", {"id": "result-stats"})
    search_headings = soup.find_all("h3")
    print(header.getText())
    print("-" * 50)
    for info in search_headings:
        print(info.getText())


keyword = "shoes"
for i in range(0, 6):
    parse(url.format(keyword, i * 10))
