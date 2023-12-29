import requests
from bs4 import BeautifulSoup
import re

def extract_email_and_name(url):
    # Send an HTTP request to the URL and get the HTML content
    response = requests.get(url)
    html_content = response.text

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Define patterns for different contact types
    patterns = [
    r'Primary Contact :',
    r'Secondary Contact:',
    r'Tertiary Contact:',
    r'Quatemary Contact:',
    r'Quinary Contact Person:'
    ]

    # Extract names using regular expressions
    names = []

    for pattern in patterns:
        matches = re.findall(f'{pattern}\s*(.+)', soup)
        names.extend(matches)

   


    # Use regular expressions to find email addresses and names
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    

    # Find all email addresses and names in the HTML
    emails = re.findall(email_pattern, html_content)
    

    return emails, names

# Example usage
url = "https://fastcashconsulting.com/company/180-degrees-inc-6128135010"
emails, names = extract_email_and_name(url)

print("Emails:", emails)
print("Names:", names)