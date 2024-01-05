
import requests
from bs4 import BeautifulSoup
import re


url = "https://aswy-zgpvh.campaign-view.com/ua/viewinbrowser?od=3zb2550a760b654ae4af11247436b4655d5a4791658f6060876768aa92067a41d0&rd=1755e77020216b9b&sd=1755e77020210a91&n=11699e4bf74b342&mrd=1755e77020210a7f&m=1"


response = requests.get(url)
html_content = response.text

    # Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

text = soup.get_text()

# Remove extra blank lines
cleaned_text = "\n".join(line for line in text.splitlines() if line.strip())

print(cleaned_text)

# with open('output.txt', 'w') as file:
#     # Write text to the file
#     file.write(cleaned_text)
