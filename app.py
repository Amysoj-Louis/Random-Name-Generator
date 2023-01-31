# Import the required libraries
import requests
from bs4 import BeautifulSoup
import re

# URL to scrape random names from
url = 'https://www.behindthename.com/random/random.php?number=2&sets=1&gender=both&surname=&usage_ind=1'

# Initialize variables for first name and last name
First_name = ''
last_name = ''

# Make a GET request to the URL
r = requests.get(url)

# Get the content of the response
data = r.content

# Create a BeautifulSoup object to parse the content
soup = BeautifulSoup(data, "html.parser")

# Loop through all the links in the content
for link in soup.findAll('a'):

    # Get the raw link
    rawlink = link.get('href')

    # Check if the link contains "/name/"
    if ("/name/" in rawlink):

        # If First_name is empty, assign the first name
        if (First_name == ''):
            First_name = rawlink.split("/")[2]

        # If First_name is not empty, assign the last name
        else:
            last_name = rawlink.split("/")[2]

# Create a name by concatenating first and last name
name = f'{First_name.capitalize()} {last_name.capitalize()}'
name = re.sub("[-\d]", '', name)

# Print the name
print(f'Name: {name}')
