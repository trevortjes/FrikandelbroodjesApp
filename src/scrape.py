import requests
from bs4 import BeautifulSoup

url = "https://www.jumbo.com/producten/jumbo-frikandelbroodjes-2-stuks-608473PAK"


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

def fetch_jumbo() -> float:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Fetch the price which is given as 2 tags seperated by decimal point
    fetch_price = soup.find_all("div", {"class": "jum-price prominent product-price"})
    pre = fetch_price[0].contents[1].contents[1].contents[0]
    post = fetch_price[0].contents[1].contents[2].contents[0]

    # combine the fetched data
    fetched_price = round((float(pre + "." + post) / 3),2)
    print(fetched_price)

    return fetched_price

