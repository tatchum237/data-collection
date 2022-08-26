# Web Scrapping
# https://beautiful-soup-4.readthedocs.io/en/latest/
# https://docs.python.org/3/library/time.html




import requests
from bs4 import BeautifulSoup
from typing import List
from country import Countries



PATH_URL = 'cours/cours-des-devises-contre-Franc-CFA-appliquer-aux-transferts'
URL = f'https://www.bceao.int/fr/{PATH_URL}'


class DataSouper(object):
    @classmethod
    def httpFetcher(cls, URL):
        with requests.Session() as session:
            result = session.get(URL)
            result = result.text
            return result


class CurrencyScrapper(object):
    @classmethod
    def scrapLink(cls, URL):
        return DataSouper \
            .httpFetcher(URL)

    @classmethod
    def souper(cls, URL):
        result = cls.scrapLink(URL)
        return BeautifulSoup(
            result,
            'html.parser')

    @classmethod
    def getBoxCourse(cls, URL):
        soupering = cls.souper(URL)
        soupering = soupering \
            .find_all(attrs={
                'id': 'box_cours'})
                
        if soupering:
            table = soupering[0].table
            return table
        return None

    @classmethod
    def makeCurrencyList(cls, URL):
        soupering = cls.getBoxCourse(URL)
        if soupering:
            tr = soupering.find_all('tr')
            factory = [
                item.find_all('td')
                for item in tr
            ][1:]
            factory = [
                {
                    'devise': Countries.selectRandom(['Euro', 'Dollar', 'Yen']),
                    'valeur': float(y.string.strip().replace(',', '.')),
                    'enXOF': 0,
                }
                for (x, y, z) in factory
            ]
            return factory
        return None

    @classmethod
    def convert(cls, number: float, val: str):
        if val == 'Euro':
            return number * 656.38
        elif val == 'Dollar':
            return number * 658
        else:
            return number * 4.81

    @classmethod
    def update(cls, data:List):
        def construct(item: dict):
            if (item.get('valeur') !=None and item.get('devise') !=None): 
                item['enXOF'] = cls.convert(item.get('valeur'), item.get('devise'))
            return item
        return list(map(construct, data))

    @classmethod
    def main(cls):
        result = cls.makeCurrencyList(URL)
        result = cls.update(result)
        return result


if __name__ == '__main__':
    print(CurrencyScrapper.main())

   
  
  


   
   