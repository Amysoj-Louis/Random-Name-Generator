# Random Name Generator

A Python script that scrapes random names from a website and removes all the numbers and dashes from the name.

## Requirements

- `requests` library
- `bs4` library
- `re` library

## Steps of Code

- Makes GET request to specified URL
- Parses response with BeautifulSoup
- Extracts first and last name from links containing "/name/"
- Concatenates names to form full name, stored in name variable
- Removes numbers and dashes from name using re.sub method
- Prints final result to console

## Notes

This script is for educational purposes only and should not be used for scraping websites without permission.The website's terms of use may prohibit scraping and using the data obtained from the website for commercial purposes.
