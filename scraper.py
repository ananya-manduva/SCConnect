import requests
from bs4 import BeautifulSoup
import re

# Function to clean and refine extracted email addresses
def clean_emails(emails):
    cleaned_emails = set()
    unwanted_prefixes = ['page', 'house']

    for email in emails:
        email = email.lower()  # Normalize email to lowercase
        if re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', email):
            for prefix in unwanted_prefixes:
                if email.startswith(prefix):
                    email = email[len(prefix):]  # Remove the unwanted prefix
            cleaned_emails.add(email)
    return cleaned_emails

# Function to clean and refine extracted phone numbers
def clean_phone_numbers(phone_numbers):
    cleaned_numbers = set()
    for number in phone_numbers:
        number = number.strip()  # Clean up any leading/trailing spaces or unwanted characters
        # Remove unwanted characters (like parentheses or extra spaces)
        number = re.sub(r'[^\d\+\-\(\) ]', '', number)  # Keep only digits, +, -, parentheses, and spaces
        if re.match(r'^(\+?\d{1,2})?[\(\)\-\s]?\d{3}[\)\-\s]?\d{3}[\-\s]?\d{4}$', number):
            cleaned_numbers.add(number)
    return cleaned_numbers

def extract_contact_info(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Will raise HTTPError if the response code is not 200
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract emails using a refined regex pattern
        emails = set(re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', soup.get_text()))
        emails = clean_emails(emails)

        # Extract phone numbers using more inclusive pattern (includes tel: links)
        phone_numbers = set(re.findall(r'\(?\+?[0-9]*\)?[0-9_\- \(\)]{7,20}', soup.get_text()))
        phone_numbers = clean_phone_numbers(phone_numbers)

        # Look for tel: links explicitly in the HTML
        tel_links = soup.find_all('a', href=re.compile('^tel:'))
        for tel in tel_links:
            phone_numbers.add(tel.get('href').replace('tel:', '').strip())

        # Filter contact information for Santa Cruz stores
        # Check if "Santa Cruz" is mentioned in any part of the page text
        page_text = soup.get_text().lower()
        if "santa cruz" in page_text:
            # Formatting the response
            formatted_response = ""
            if emails:
                formatted_response += "Emails: " + ", ".join(emails) + "\n"
            
            if phone_numbers:
                formatted_response += "Phone Numbers: " + ", ".join(phone_numbers) + "\n"
            
            return formatted_response.strip()

        # If "Santa Cruz" isn't found, return an empty response or message
        return "No contact information found for Santa Cruz locations."

    except requests.exceptions.RequestException as e:
        return f"Error fetching URL: {e}"

    except Exception as e:
        return f"An error occurred: {e}"
