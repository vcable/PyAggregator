import requests
from bs4 import BeautifulSoup
import praw
import os

REDDIT_APP_KEY = os.environ["R_APP_KEY"]
REDDIT_SECRET_KEY = os.environ["R_SECRET"]

class Aggregator():
    
    def __init__(self):
        self.planet_python()
        self.real_python()
        self.r_python()
        self.import_python()
        self.stack_overflow()
        self.python_guru()

    def planet_python(self):
        data = requests.get("https://planetpython.org/titles_only.html").content
        soup = BeautifulSoup(data, "html.parser")
        
        self.pp_articles = {}
        titles = soup.find_all("h4")
        for title in titles:
            if len(self.pp_articles) < 10:
                self.pp_articles[title.text] = title.find("a")["href"]
        
            
    def real_python(self):
        data = requests.get("https://realpython.com/").content
        soup = BeautifulSoup(data, "html.parser")
        
        self.rp_articles = {}
        titles = soup.find_all("div", {"class": "card-body"})
        for title in titles:
            if len(self.rp_articles) < 10:
                self.rp_articles[title.find("h2").text] = title.find("a")["href"]
    
    
    def r_python(self):
        reddit = praw.Reddit(client_id=REDDIT_APP_KEY,
                             client_secret=REDDIT_SECRET_KEY,
                             user_agent="PyAggregator")
        
        r_python = reddit.subreddit("Python").top("day", limit=10)
        
        self.r_python_posts = {}
        
        for post in r_python:
            self.r_python_posts[post.title] = post.url
    
    def import_python(self):
        data = requests.get("https://importpython.com/newsletter/", verify=False).content
        soup = BeautifulSoup(data, "html.parser")
        
        self.import_articles = {}
        articles = soup.find_all("div", {"class": "subtitle"})
        for article in articles:
            if len(self.import_articles) < 10:
                self.import_articles[article.text] = article.find("a")["href"]

    def stack_overflow(self):
        data = requests.get("https://stackoverflow.com/questions/tagged/python?tab=Active").content
        soup = BeautifulSoup(data, "html.parser")
        
        self.stack_questions = {}
        questions = soup.find_all("div", {"class": "question-summary"})
        for question in questions:
            if len(self.stack_questions) < 10:
                self.stack_questions[question.find("h3").text] = question.find("a")["href"]
                
    def python_guru(self):
        data = requests.get("https://thepythonguru.com/blog/").content
        soup = BeautifulSoup(data, "html.parser")
        
        self.guru_articles = {}
        posts = soup.find_all("h2")
        for post in posts:
            if len(self.guru_articles) < 10:
                self.guru_articles[post.text] = post.find("a")["href"]

