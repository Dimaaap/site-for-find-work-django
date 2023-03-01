import requests
from pathlib import Path
from bs4 import BeautifulSoup


class City:
    url = 'https://population-hub.com/ua/ua/list-of-cities-in-ukraine-by-population.html'


class CityParser(City):

    def get_request(self):
        cities = requests.get(self.url).text
        return cities

    def parse_request(self):
        cities = self.get_request()
        cities_parse = BeautifulSoup(cities, 'lxml')
        cities_table = cities_parse.find('tbody')
        cities_title = cities_table.find_all('tr')
        list_cities = []
        for title in cities_title:
            list_cities.append(title.find('td').text)
        return list_cities


class DBSaver:

    def __init__(self, dbname):
        self.dbname = dbname

    def save_data(self):
        new_parser = CityParser()
        for city in new_parser.parse_request():
            new_city = self.dbname(title=city)
            new_city.save()


