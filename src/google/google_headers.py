import requests
import bs4
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


keyword = "shoes"
url = f"https://google.com/search?q={keyword}"

proxies = {
    "http": "http://USERNAME:PASSWORD@unblock.oxylabs.io:60000",
    "https": "http://USERNAME:PASSWORD@unblock.oxylabs.io:60000",
}

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Mobile/15E148 Safari/604.1",
    "Accept-Language": "en-US",
}

response = requests.get(url, proxies=proxies, verify=False, headers=headers)

soup = bs4.BeautifulSoup(response.text, "lxml")
search_headings = soup.find_all("h3")
for info in search_headings:
    print(info.getText())
