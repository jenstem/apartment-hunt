import requests
from bs4 import BeautifulSoup


url = "https://www.theblueground.com/furnished-apartments-dubai-uae"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
print(soup)