from bs4 import BeautifulSoup
import requests


class Scraper:

    def lastNews(self):
        url = "https://ria.ru/world/"
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        news = []
        time = []
        result = []
        news = soup.findAll('a', class_='list-item__title')
        time = soup.findAll('div', class_='list-item__date')
        for i in range(len(news)):
            temp = [news[i].text, time[i].text]
            result.append(temp)
        return result

    def weather(self, url):
        url = url
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        temperature = soup.find('span', class_='temp__value')
        if temperature.text is None:
            return "Не правильно введен город"
        else:
            return temperature.text
