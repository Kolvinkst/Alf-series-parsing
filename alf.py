import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://en.wikipedia.org/wiki/List_of_ALF_episodes")

soup = BeautifulSoup(response.content, 'html.parser')

episode = soup.find_all("tr", {"class": "vevent"})

for i in episode:
    print("Number of episode: " + i.find("th", {"scope": "row"}).getText() + ", " "name of episode: " + i.find("td", {"class": "summary"}).getText())