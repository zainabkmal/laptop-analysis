from bs4 import BeautifulSoup
import requests
import pandas as pd

# Load the Excel file
urls_df = pd.read_excel( '/Users/zainab/Desktop/J.URLS.xlsx' , sheet_name='Sheet1')

# Extract URLs from the DataFrame
urls = urls_df['URL'].tolist()  


# Headers to mimic a browser visit
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Create a list to hold the scraped data
data = []

# Scrape elements and print results
for url in urls:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    product_name = soup.select_one('.product-title__title')
    name = product_name.text.strip() if product_name else 'N/A'

    product_brand = soup.select_one('.product-title__logo img')
    brand = product_brand.attrs['title'] if product_brand else 'N/A'

    product_specs_arr = ""
    product_specs = soup.select('.product-title__info--box')
    for i in product_specs:
        product_specs_arr = product_specs_arr + i.text.strip() + "\n"
    
    
  
    #Append the result to the data list
    data.append({
        'URL': url,
        'Name': name,
        'Brand': brand,
        ' product_specs' :  product_specs_arr
      })
        
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('jarir_p.csv', index=False, encoding='utf-8')

print("Data has been written to jarir_data.csv")
