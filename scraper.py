# scraper.py
import requests
from bs4 import BeautifulSoup
import re

def get_contact_info(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None

    # Parse the webpage content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find emails (simple regex for email addresses)
    emails = set(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', soup.text))
    
    # Find phone numbers (basic pattern, this can be adjusted for better matching)
    phone_numbers = set(re.findall(r'\(?\+?[0-9]*\)?[0-9_\- \(\)]{7,}', soup.text))
    
    # Find addresses (basic pattern for street addresses, can be adjusted)
    addresses = set(re.findall(r'\d{1,5}\s\w+\s\w+', soup.text))

    # Output found contact information
    print("Found Emails:", emails)
    print("Found Phone Numbers:", phone_numbers)
    print("Found Addresses:", addresses)

# User input for URL
url = input("Enter the URL of the local business page to scrape: ")
get_contact_info(url)
