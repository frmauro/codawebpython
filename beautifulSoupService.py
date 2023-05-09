from bs4 import BeautifulSoup
import requests
import json

class SoupService:
    # init method or constructor
    def __init__(self, url):
        self.url = url

    # function to extract html document from given url
    def getSoupDocument(self):
        # request for HTML document of given url
        response = requests.get(self.url)
        # response will be provided in JSON format

        # create soap object
        soup = BeautifulSoup(response.text, 'html.parser')

        return soup    