import requests

proxies = {
    "http": "http://USERNAME:PASSWORD@unblock.oxylabs.io:60000",
    "https": "http://USERNAME:PASSWORD@unblock.oxylabs.io:60000",
}
keyword = "shoes"
url = f"https://google.com/search?q={keyword}"

headers = {"X-Oxylabs-Render": "png"}  # change to html to get the HTML response

response = requests.get(
    url,
    verify=False,
    proxies=proxies,
    headers=headers,
)

# Save screenshot as PNG file
with open("google_rendered.png", "wb") as f:
    f.write(response.content)
