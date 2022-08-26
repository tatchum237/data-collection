import json
import requests
from bs4 import BeautifulSoup
from typing import List

from libraries.utils import Utils
from libraries.csv import CsvFactory
from libraries.json import JsonFactory
import pandas as pd

BASE_URL = 'COURSE/DATABASES/data-zIybdmYZoV4QSwgZkFtaB.html'

class HtmlFactory(object):
    @classmethod
    def openFile(cls):
        with open(BASE_URL) as file:
            data = file.read()
            data = BeautifulSoup(
                data,
                'html.parser')
            file.close()
        return data

    @classmethod
    def getResult(cls, data: list):
        result = []
        for i in range(0, len(data), 6) :
            result.append(
           {
            'name':cls.constructName(data[i].getText()),
            'phone':data[i + 1].getText(),
            'email':data[i + 2].getText(),
            'latlng':cls.constructLatlon(data[i + 3].getText()),
            'salary':float(data[i + 4].getText()),
            'age':int(data[i + 5].getText())
           }
        )
        
        return result
    
    def constructName(item:dict):
         wrd = item.split(' ')
         return wrd[0] + ' ' + wrd[1].upper()

    def constructLatlon(item:dict):
         wrd = item.split(',')
         return wrd[0] + ', ' + wrd[1]

    @classmethod
    def main(cls):
        data = cls.openFile()
        data = cls.getResult(data.find_all("td"))
        return list(data)



if __name__ == '__main__':
    

    print(HtmlFactory.main())