import requests
import json
import csv
import sqlite3 
import pandas as pd 


from html_ import HtmlFactory
from concatenation import ConcatFactory
from bceao import CurrencyScrapper
from country import Countries
from sql import SqlFactory

def divider(n=40):
    return '-' * n


if __name__ == '__main__':

    print('\n')
    print('MON PROGRAMME\n')
    print(divider())
    print('\n')
   
    print('1-2-3 SCRAPPING\n')

    print(divider())
    print('\n')
    print(HtmlFactory.main())

    print('\n')

    print('4 concatenenation des listes d\'objet\n')
   
    print('\n')
    print(ConcatFactory.main())
    print(divider())
    print('\n')

    print('5 SCRAPPING\n')
    
    print('\n')
    print(CurrencyScrapper.main())
    print(divider())
    print('\n')

    print('6 COUNTRIE\n')
  
    print('\n')
    print(Countries.main())

    print(divider())

    print('\n')

    print('7 INSERTION DANS UNE BASE DE DONNEES SQLITE\n')
   
    print('\n')
    print(SqlFactory.main())

    print(divider())

    print('\n')
    print('FIN DU PROGRAMME\n')