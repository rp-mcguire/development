import requests
from bs4 import BeautifulSoup

def scrape_price(url):
    """Scrapes the price from a given URL."""

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes

        soup = BeautifulSoup(response.content, 'html.parser')

        # Adjust this selector based on the website's structure
        price_element = soup.find('span', {'class': 'price'}) 

        if price_element:
            return price_element.text.strip()
        else:
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    url = "https://www.example.com/product/123"  # Replace with the actual product URL
    price = scrape_price(url)

    if price:
        print(f"Price: {price}")
    else:
        print("Price not found.")