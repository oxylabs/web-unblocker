import requests

proxies = {
    "http": "http://USERNAME:PASSWORD@unblock.oxylabs.io:60000",
    "https": "http://USERNAME:PASSWORD@unblock.oxylabs.io:60000",
}

url = "https://ip.oxylabs.io"
response = requests.get(url, proxies=proxies, verify=False)

print(response.text)
