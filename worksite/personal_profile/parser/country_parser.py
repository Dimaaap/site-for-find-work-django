import requests
from pathlib import Path
from bs4 import BeautifulSoup


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


class CountryFileParser(CountryFile):

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



