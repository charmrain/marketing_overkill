from bs4 import BeautifulSoup
import requests
import csv
import re


# Example usage
# url = "https://fastcashconsulting.com/company/180-degrees-inc-6128135010"
url = "https://fastcashconsulting.com/company/cares-clothing-llc-6123457952"

source = requests.get(url).text

# soup = BeautifulSoup(source, 'lxml')
soup = BeautifulSoup(source, 'html.parser')

comp_info = soup.find('div', class_='company-information')
comp_info = comp_info.get_text()

print("comp info: ", comp_info)

# Extract primary contact infomation

primary_contact_match = re.search(r"Primary Contact : (.+?)Primary Email: (.+?)Secondary", comp_info)
primary_contact_name = primary_contact_match.group(1) if primary_contact_match else None
primary_contact_email = primary_contact_match.group(2) if primary_contact_match else None




# Extract categories of service
categories_of_service_match = re.search(r"Categories of Service(.+)", comp_info)
categories_of_service = categories_of_service_match.group(1).strip() if categories_of_service_match else None

print("Primary Contact Name:", primary_contact_name)
print("Primary Contact Email:", primary_contact_email)
print("Categories of Service:", categories_of_service)




# Extract categories of service

# Print the extracted information

# break into lines and remove leading and 
# lines = (line.strip() for line in comp_info.splitlines())
# chunks = (phrase.strip() for line in lines for phrase in line.split(" "))
# text = '\n'.join(chunk for chunk in chunks if chunk)

# print(text)



# for script in soup(["script", "style"]):
#     script.extract()

# text = soup.get_text()
# print(text)

# Extract primary contact name and email