import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm 

import numpy as np

def extract_webpage(city):
    # Replace spaces with hyphens in the city name
    city_url_component = city.replace(' ', '-')
    
    # Construct the URL with the city name
    # need to change the state name according to which state to be extracted
    url = f"https://fastcashconsulting.com/city/{city_url_component}-tx"
    
    # Send a GET request
    response = requests.get(url)
    
    # If the GET request is successful, the status code will be 200
    if response.status_code == 200:
        # Get the content of the response
        webpage_content = response.content
        
        # Create a BeautifulSoup object and specify the parser
        soup = BeautifulSoup(webpage_content, 'html.parser')
        
        # Extract content within the <div class="listings"> tag
        listings_div = soup.find('div', class_='listings')
        
        
        # If <div class="listings"> tag is found, extract its text preserving line breaks
        if listings_div:
            text_lines = [line.strip() for line in listings_div.stripped_strings]
            
            # Join lines where ':' starts a new line with the preceding line
            joined_lines = []
            for i in range(len(text_lines)):
                if i > 0 and text_lines[i].startswith(':'):
                    joined_lines[-1] += ' ' + text_lines[i]
                else:
                    joined_lines.append(text_lines[i])
                    
            text = '\n'.join(joined_lines)
        else:
            text = "No listings found."
        
        # Extract hyperlinks within the <div class="listings"> tag
        if listings_div:
            hyperlinks = [a['href'] for a in listings_div.find_all('a', href=True) if a['href'].startswith("https://fastcashconsulting.com/")]
        else:
            hyperlinks = []
        








        return text, hyperlinks
    else:
        # If the request was not successful, return None
        return None, None
    

# Create empty lists to store city names and hyperlinks
city_list = []
hyperlink_list = []


# city_names = ['Abbott','Abernathy','Abilene','Addison','Agua Dulce']
with open(r'C:\Project\7. New tech\webcrawlers\all states\texas.txt', 'r') as file:
    # Read lines from the file and strip whitespace
    # cities = [line.strip() for line in file]
    cities = [line.strip() for line in file if line.strip()]


# Iterate over each city name and extract webpage content and hyperlinks
for city in tqdm(cities, desc="Processing cities"):
    text, hyperlinks = extract_webpage(city)
    if text is not None and hyperlinks is not None:
        # Append city name and hyperlinks to lists
        for link in hyperlinks:
            city_list.append(city)
            hyperlink_list.append(link)
    else:
        print(f"Failed to fetch data for city: {city}")

# Create a DataFrame
df = pd.DataFrame({'City': city_list, 'Hyperlink': hyperlink_list})

# Display the DataFrame
print(df)

df.to_csv('texas.csv')



def scrape_company_info(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'html.parser')

    comp_info = soup.find('div', class_='company-information')

    if comp_info is None:
        print(f"Unable to find company information for URL: {url}")
        return None, None  # Return None for both primary contact name and email

    comp_info_text = comp_info.get_text()

    # Extract primary contact information
    primary_contact_match = re.search(r"Primary Contact : (.+?)Primary Email: (.+?)Secondary", comp_info_text)
    primary_contact_name = primary_contact_match.group(1) if primary_contact_match else None
    primary_contact_email = primary_contact_match.group(2) if primary_contact_match else None

    return primary_contact_name, primary_contact_email


results_new = []
# Define batch size
batch_size = 100  # You can adjust this based on your system's capabilities and the size of your data

# Calculate the number of batches
num_batches = int(np.ceil(len(df) / batch_size))

# Iterate over batches
for i in tqdm(range(num_batches), desc="Scraping company info"):
    start_idx = i * batch_size
    end_idx = min((i + 1) * batch_size, len(df))
    
    # Get URLs for the current batch
    batch_urls = df['Hyperlink'][start_idx:end_idx]
    
    # Process URLs in the current batch
    for url in batch_urls:
        try:
            results_new.append(scrape_company_info(url))
        except Exception as e:
            print(f"Error processing URL {url}: {e}")
            


        
            # You can choose to log errors or handle them as required


# Convert results_list to DataFrame
results_df = pd.DataFrame(results_new, columns=['primary_contact_name', 'primary_contact_email'])

# Concatenate df and results_df along columns axis
df_comb = pd.concat([df, results_df], axis=1)

df_comb.to_excel("texas_contact.xlsx")