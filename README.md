# Web Unblocker

[![Web unblocker](https://user-images.githubusercontent.com/129506779/249698988-62f810bb-fe99-4c46-be3d-d4f7e4bc27f8.png)](https://oxylabs.go2cloud.org/aff_c?offer_id=7&aff_id=877&url_id=14)


- [Introduction](#introduction)
- [Getting started](#getting-started)
  - [InsecureRequestWarning](#insecurerequestwarning)
- [Scraping Google Search Results](#scraping-google-search-results)
  - [Sample Python Script](#sample-python-script)
  - [Using Web Unblocker](#using-web-unblocker-1)
    - [Using the Same IP](#using-the-same-ip)
    - [Using the Same Location](#using-the-same-location)
    - [Sending Custom Headers](#sending-custom-headers)
    - [Rendering and Screenshots](#rendering-and-screenshots)
- [Scraping Amazon](#scraping-amazon)
    - [Sample Python Script](#sample-python-script-1)
  - [Using Web Unblocker](#using-web-unblocker-2)
    - [Sending Custom Headers](#sending-custom-headers-1)
    - [Rendering](#rendering)
    - [Setting the ZIP code or the location](#setting-the-zip-code-or-the-location)
- [Conclusion](#conclusion)

## Introduction

[Web Unblocker](https://oxylabs.io/products/web-unblocker) is an AI-powered proxy solution capable of bypassing sophisticated anti-bot systems.

Web Unblocker has the following features:

- ML-driven proxy management 
- Dynamic browser fingerprinting 
- ML-powered response recognition
- Auto-retry functionality
- JavaScript rendering 


## Getting started

Execute the following `curl` command from your terminal:

```shellW
curl --insecure --proxy unblock.oxylabs.io:60000 --proxy-user "USERNAME:PASSWORD" https://ip.oxylabs.io
```

The output should be a random IP.

Notice a few things here:

- `--proxy` or `x` is used for proxy. Here, we use it for the URL of Web Unblocker
- `--insecure` or the equivalent `-k` is required for Web Unblocker to work
- `--proxy-user` or `-U` is used for the proxy user and password. If you don't have one, sign up for a [free trial](https://oxylabs.io/products/web-unblocker).

If you are observing low success rates or retrieve empty content, please try adding additional `"x-oxylabs-render: html"` header with your request.

You can find the equivalent python code in [getting_started.py](src/gettting_started.py):

```python
import requests

proxies = {
    'http': 'http://USERNAME:PASSWORD@unblock.oxylabs.io:60000',
    'https': 'http://USERNAME:PASSWORD@unblock.oxylabs.io:60000'
}

url = 'https://ip.oxylabs.io'
response = requests.get(url,
        proxies=proxies,
        verify=False) # disable SSL certificate verification

print(response.text)
```

### InsecureRequestWarning

One side effect of using `verify=False` is that you may receive warnings for `InsecureRequestWarning`.

Add these two lines to suppress these warnings:

```python
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
```

## Scraping Google Search Results

### Sample Python Script

The following is a [sample script](src/google_blocked.py) that scrapes Google search engine results.

```python
import requests
import bs4

keyword = "shoes"
url = f'https://google.com/search?q={keyword}'


request_result = requests.get(url)
soup = bs4.BeautifulSoup(request_result.text, "lxml")
search_headings = soup.find_all('h3')
for info in search_headings:
    print(info.getText())
```

If you run this code with Python a few times, you’ll be blocked by Google.

### Using Web Unblocker

The easiest solution to bypass all possible bans is to use Web Unblocker. Add the following lines to use Web Unblocker, just like you would use proxies.

```python
proxies = {
    'http': 'http://USERNAME:PASSWORD@unblock.oxylabs.io:60000',
    'https': 'http://USERNAME:PASSWORD@unblock.oxylabs.io:60000'
}

# Sending the proxy information
response = requests.get(url,
    proxies=proxies,
    verify=False)
```

For the complete code, see [google_unblocked.py](src/google_unblocked.py).

#### Using the Same IP

If you use Web Unblocker to scrape multiple pages, you may want to maintain the same IP or geographical region.

To use the same IP, send a header `X-Oxylabs-Session-Id`  and use any random string its value.

```python
headers = {
    "X-Oxylabs-Session-Id": "aRandomString"
}

response = requests.get(
    'https://www.google.com/search?q=shoes',
    verify=False, 
    proxies=proxies,
    headers=headers,
)
```

#### Using the Same Location

Instead of using the same IP, you can also rotate the IP from a specific location. To do that, send the header `x-oxylabs-geo-location` and set its value as a country, state, city, coordinates, or radius.

```python
headers = {
    "x-oxylabs-geo-location": "New York,New York,United States"
}

response = requests.get(
    'https://www.google.com/search?q=shoes',
    verify=False, 
    proxies=proxies,
    headers=headers,
)
```

For a complete example, see [google_location.py](src/google_location.py)

See [documentation](https://developers.oxylabs.io/advanced-proxy-solutions/web-unblocker/making-requests/geo-location#google) for more details.

#### Sending Custom Headers

You can add standard or custom headers to the request. 

One of the possible use cases is getting device-specific search results.

```python
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Mobile/15E148 Safari/604.1",
    "Accept-Language": "en-US",
}

response = requests.get(url, 
    proxies=proxies, 
    verify=False, 
    headers=headers)
```

#### Rendering and Screenshots

Web Unblockers fully supports rendering. If you want to render a page, add the customer header as shown below:

```python
headers = {
    "X-Oxylabs-Render": "html"
}
```

In this particular example, Google doesn't need rendering. However, this can be used to take a screenshot. Send the same header, but change the value to `png`.

```python
headers = {
    "X-Oxylabs-Render": "png"
}

response = requests.get(
    url, verify=False, proxies=proxies, headers=headers,
)

# Save screenshot as PNG file
with open("google_rendered.png", 'wb') as f:
    f.write(response.content)
```

See [google_screenshots.py](src/google_screenshots.py) for the complete source code.

## Scraping Amazon

This section shows you how to scrape Amazon with Web Unblocker.

We start with a simple script and will add more features.

#### Sample Python Script

Examine the code in  [basic_script.py](src/amazon/basic_script.py). First, you will notice that Amazon will not even return a response without a valid user agent. 

Second, upon executing the following script a few times, Amazon will block you.

```python
import requests
url = 'https://www.amazon.com/Bose-QuietComfort-45-Bluetooth-Canceling-Headphones/dp/B098FKXT8L'
custom_headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
}

response = requests.get(url, headers=custom_headers)

print(response.text)
```

### Using Web Unblocker

The easiest solution to bypass all the bans is to use the Web Unblocker.

Add the following lines to use the Web Unlcoker, just like you would use proxies.

```python
proxies = {
    'http': 'http://USERNAME:PASSWORD@unblock.oxylabs.io:60000',
    'https': 'http://USERNAME:PASSWORD@unblock.oxylabs.io:60000'
}

response = requests.get(url,
    proxies=proxies,
    verify=False,
    headers=custom_headers
)
```

Once you have the response, you can use BeautifulSoup to extract the product title and price as follows:

```python
soup = bs4.BeautifulSoup(response.text, "lxml")

product_title = soup.find('span', id="productTitle")
price_element = soup.select_one("div[role='radio'] [class='a-price-whole']")

print(product_title.getText())
if price_element:
    print(price_element.getText())

```

For the complete code, see [amazon_unblocked.py](src/amazon/amazon_unblocked.py).

#### Sending Custom Headers

As shown in the Sample Python Script, you cannot scrape Amazon without at least one header—user agent.

Similarly, you can send any other custom header, which will be forwarded to Amazon by Web Unblocker.

```python
url = 'https://www.amazon.com/Bose-QuietComfort-45-Bluetooth-Canceling-Headphones/dp/B098FKXT8L'

custom_headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
}
proxies = {
    'http': 'http://USERNAME:PASSWORD@unblock.oxylabs.io:60000',
    'https': 'http://USERNAME:PASSWORD@unblock.oxylabs.io:60000'
}


response = requests.get(url,
                        proxies=proxies,
                        verify=False,
                        headers=custom_headers
                        )
```

For the complete code, see [amazon_unblocked.py](src/amazon/amazon_unblocked.py).

#### Rendering

Usually, sending the user agent is enough for web scraping Amazon, as shown in the previous example. If you are still facing problems, you can render the page by sending the header `X-Oxylabs-Render`:

```python
custom_headers = {
    "X-Oxylabs-Render": "html"
}
#...
response = requests.get(url,
                        proxies=proxies,
                        verify=False,
                        headers=custom_headers
                        )
```

The rest of the code remains the same. 

See [amazon_rendering.py](src/amazon/amazon_rendering.py) for the complete code.

#### Setting the ZIP code or the location

Using the `x-oxylabs-geo-location` parameter value for Amazon pages will yield a result with a corresponding delivery preference setting.

You can use this parameter to get correctly-localized Amazon results in a few ways. For most Amazon domains, you can send a zip/postcode or a [2-letter ISO 3166-1 alpha-2 country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).

Note that this is different from scraping Google, where you cannot specify zip but instead can send a City. See [documentation](https://developers.oxylabs.io/advanced-proxy-solutions/web-unblocker/making-requests/geo-location#amazon) for more details.

```python
headers = {
    "x-oxylabs-geo-location": "11001" #New York ZIP
}

response = requests.get(
    url,
    verify=False, 
    proxies=proxies,
    headers=headers,
)
```

## Conclusion

You should now be able to scrape Google and Amazon with Web Unblocker. We have provided many examples in the [amazon](src/amazon) and [google](src/google) folders. 

Learn more about [Web Unblocker](https://oxylabs.io/products/web-unblocker).

Also, check this tutorial on [pypi](https://pypi.org/project/web-unblocker/)

If you face any problems, reach out to support.
