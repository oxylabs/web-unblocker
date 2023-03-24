import requests
import bs4
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = "https://www.amazon.com/Bose-QuietComfort-45-Bluetooth-Canceling-Headphones/dp/B098FKXT8L"


custom_headers = {
    "x-oxylabs-geo-location": "11001",
}
proxies = {
    "http": "http://USERNAME:PASSWORD@unblock.oxylabs.io:60000",
    "https": "http://USERNAME:PASSWORD@unblock.oxylabs.io:60000",
}


response = requests.get(url, proxies=proxies, verify=False, headers=custom_headers)
if response.status_code != 200:
    print("Error: ", response.status_code)
    print(response.text)
    exit(-1)
soup = bs4.BeautifulSoup(response.text, "lxml")
product_title = soup.find("span", id="productTitle")
print(product_title.getText())
price_element = soup.select_one("div[role='radio'] [class='a-price-whole']")
if price_element:
    print(price_element.getText())
