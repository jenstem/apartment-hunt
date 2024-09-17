import requests
from bs4 import BeautifulSoup


url = "https://www.theblueground.com/furnished-apartments-dubai-uae"

response = requests.get(url)
print(response)