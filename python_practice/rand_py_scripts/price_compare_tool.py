# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 15:05:24 2024

@author: raypm

First Draft webscraper for price comparison tool
"""

import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    """Scrapes data from a given website."""

    # Send a GET request to the URL
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract data (customize this part based on the website structure)
    data = {}
    # Example: Extract all titles
    titles = soup.find_all('h2', class_='title')
    data['titles'] = [title.text.strip() for title in titles]

    return data

if __name__ == '__main__':
    url = "https://www.example.com"  # Replace with the URL you want to scrape
    data = scrape_website(url)
    print(data)