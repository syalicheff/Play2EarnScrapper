import requests
from bs4 import BeautifulSoup
import json

def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find table headers
    headers = [th.text.strip() for th in soup.select('thead th')]

    # Find table rows
    rows = []
    for row in soup.select('tbody tr'):
        data = [td.text.strip() for td in row.find_all('td')]
        rows.append(dict(zip(headers, data)))

    return rows

def scrape_all_pages():
    base_url = 'https://playtoearn.com/blockchaingames?page='
    all_data = []
    
    for page in range(1, 58):  # Loop through all 57 pages
        url = f"{base_url}{page}"
        print(f"Scraping page {page}")
        page_data = scrape_page(url)
        all_data.extend(page_data)

    return all_data

# Run the scraper and collect data
all_games = scrape_all_pages()

# Save the scraped data to a JSON file
with open('blockchain_games.json', 'w') as f:
    json.dump(all_games, f)

print(f"Scraping completed. Data saved to blockchain_games.json")
