import requests
from bs4 import BeautifulSoup


class Aggregator():
    
    def __init__(self):
        self.planet_python()

    def planet_python(self):
        data = requests.get("https://planetpython.org/titles_only.html").content
        soup = BeautifulSoup(data, "html.parser")
        
        self.pp_articles = {}
        titles = soup.find_all("h4")
        for title in titles:
            if len(self.pp_articles) < 5:
                self.pp_articles[title.text] = title.find("a")["href"]
            else: 
                break
            

