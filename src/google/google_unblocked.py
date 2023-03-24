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


response = requests.get(url, proxies=proxies, verify=False)

soup = bs4.BeautifulSoup(response.text, "lxml")
search_headings = soup.find_all("h3")
for info in search_headings:
    print(info.getText())
