

from typing import List


from libraries.csv import CsvFactory
from libraries.json import JsonFactory
from html_ import HtmlFactory

import pandas as pd

class ConcatFactory(object):

    @classmethod
    def concatData(cls, html:List, csv: List, json:List):
        data = []
        for ht in html:
            data.append(ht)

        for ht in csv:
             data.append(ht)

        for ht in json:
             data.append(ht)


        return data

    
    @classmethod
    def main(cls):
        data = cls.concatData(HtmlFactory.main(), CsvFactory.main(), JsonFactory.main())
        return data




    



if __name__ == '__main__':
    

    print(ConcatFactory.main())