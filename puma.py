from bs4 import BeautifulSoup
import requests, json

url = "https://us.puma.com/us/en/pd/future-7-ultimate-firm-ground-arificial-ground-mens-soccer-cleats/107599?swatch=03&referrer=carousel"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")


# Get product name
def get_name(soup):
    product_name = (
        soup.find("section", {"class": "order-1 h-full md:col-span-4"}).find("h1")
    ).text

    return product_name


#  Get product rate
def get_rate(soup):
    product_rate = (
        soup.find("section", {"class": "order-1 h-full md:col-span-4"})
        .find("div", {"class": "flex relative"})
        .find("a")
    ).text

    return product_rate


#  Get product price
def get_price(soup):
    product_price = (
        soup.find("section", {"class": "order-1 h-full md:col-span-4"})
        .find("div", {"class": "tw-10m612d tw-1igwn51 tw-1dz92zg tw-l8cie8"})
        .find("span")
    ).text

    return product_price


# Get product color
def get_color(soup):
    product_color = (
        soup.find("section", {"class": "order-1 h-full md:col-span-4"})
        .find("div", {"class": "tw-1g8z7fz tw-1igwn51 tw-dynr3h tw-l8cie8"})
        .find("h4")
    ).text

    return product_color


# Get product sizes
def get_size(soup):

    size_spans = soup.find("div", {"class": "space-y-4 relative"}).find_all(
        "span", {"data-content": "size-value"}
    )

    sizes = [float(item.text.strip()) for item in size_spans]

    return sizes


def get_description(soup):

    product_description = (
        soup.find("section", {"class": "order-1 h-full md:col-span-4"})
        .find("div", {"class": "tw-1rgvuf0 tw-1igwn51 tw-dynr3h tw-l8cie8 pb-4"})
        .find("div")
    ).text

    return product_description


print(f"\nName:\n{get_name(soup)}\n")
print(f"\nRate:\n{get_rate(soup)}\n")
print(f"\nPrice:\n{get_price(soup)}\n")
print(f"\nColor:\n{get_color(soup)}\n")
print(f"\nSizes:\n{get_size(soup)}\n")
print(f"\nDescription:\n{get_description(soup)}\n")
