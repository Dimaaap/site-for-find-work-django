import requests
from pathlib import Path
from bs4 import BeautifulSoup

from .models import Country


class Countries:
    url = "https://merkator.org.ua/dovidnyk/spysok-krajin-svitu-za-alfavitom/"


class CountryFile(Countries):
    def __init__(self):
        self.filename = 'countries.html'

    def check_file_exists(self):
        path = Path(self.filename)
        return path.is_file()

    def create_file(self):
        if not self.check_file_exists():
            with open(self.filename, 'w') as file:
                request = requests.get(self.url)
                file.write(request.text)

    def open_file(self):
        if not self.check_file_exists():
            self.create_file()
        else:
            with open(self.filename) as file:
                return file.read()


class CountryFileInterface:

    def get_soup(self):
        raise NotImplemented

    def parse_soup(self):
        raise NotImplemented


class CountryFileParser(CountryFile, CountryFileInterface):

    def __init__(self):
        super().__init__()
        self.soup = BeautifulSoup(self.open_file(), 'lxml')

    def get_soup(self):
        return self.soup.prettify()

    def parse_soup(self):
        table_body = self.soup.find('tbody')
        country_titles = table_body.find_all(class_='column-2')
        country_title_list = []
        for title in country_titles:
            country_title_list.append(title.text)
        return country_title_list


class SaverInterface:

    def save_data(self):
        raise NotImplemented


class DBSaver(SaverInterface):

    def __init__(self, dbname):
        self.dbname = dbname

    def save_data(self):
        new_parser = CountryFileParser()
        for country in new_parser.parse_soup():
            new_country = self.dbname(title=country)
            new_country.save()



