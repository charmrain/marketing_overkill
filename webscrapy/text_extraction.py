from bs4 import BeautifulSoup
import requests
import csv
import re
import pandas as pd





def scrape_company_info(url):
    source = requests.get(url).text

    # soup = BeautifulSoup(source, 'lxml')
    soup = BeautifulSoup(source, 'html.parser')

    comp_info = soup.find('div', class_='company-information')
    comp_info = comp_info.get_text()

    

    # Extract primary contact infomation
    primary_contact_match = re.search(r"Primary Contact : (.+?)Primary Email: (.+?)Secondary", comp_info)
    primary_contact_name = primary_contact_match.group(1) if primary_contact_match else None
    primary_contact_email = primary_contact_match.group(2) if primary_contact_match else None




    # Extract categories of service
    categories_of_service_match = re.search(r"Categories of Service(.+)", comp_info)

    try:
        categories_of_service = categories_of_service_match.group(1).strip() if categories_of_service_match else None
        categories_of_service = categories_of_service.split("Products")[0].strip()
    except Exception as e:
        categories_of_service = 'None'

    return [primary_contact_name, primary_contact_email, categories_of_service]




# Example usage
url_list = ["https://fastcashconsulting.com/company/180-degrees-inc-6128135010", "https://fastcashconsulting.com/company/cares-clothing-llc-6123457952"]
# url = "https://fastcashconsulting.com/company/cares-clothing-llc-6123457952"

target_df = pd.read_excel(r"C:\Users\User\Desktop\Minneapolis business_copy.xlsx")
target_url_list = list(target_df['ref link'])

# print(len(target_url_list))


results_list = [scrape_company_info(url) for url in target_url_list]

# combined_list = [r + [t] for r, t in zip(results_list, target_url_list)]

# df = pd.DataFrame(combined_list, columns=['Primary Contact Name','Primary Contact Email','Categories of Service', 'ref link'])
# df.to_excel('output.xlsx', index=False)

# Specify the file name
csv_file = 'output1.csv'

# Write the list of lists to the CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(results_list)

# print("Primary Contact Name:", primary_contact_name)
# print("Primary Contact Email:", primary_contact_email)
# print("Categories of Service:", categories_of_service)




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