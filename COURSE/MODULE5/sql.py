import requests
import json
import csv
import sqlite3 
import pandas as pd 


from concatenation import ConcatFactory

from bceao import CurrencyScrapper
from prepasCountry import PrepasCountry
from prepasPersonne import PrepasPersonne

url = 'COURSE\DATABASES\data.db'
  
conn = sqlite3.connect(r'COURSE\DATABASES\data.db') 


class SqlFactory(object):
    @classmethod
    def createTable(cls):
        conn.execute('CREATE TABLE IF NOT EXISTS Devise'
                  '(id        INTEGER PRIMARY KEY AUTOINCREMENT,'
                  'devise  TEXT,'
                  'valeur    DOUBLE,'
                  'en_xof  DOUBLE)'
                )
        
        conn.execute('CREATE TABLE IF NOT EXISTS Country'
                  '(id        INTEGER PRIMARY KEY AUTOINCREMENT,'
                  'name  TEXT,'
                  'flag  TEXT,'
                  'devise  INTEGER NULL,'
                  'foreign key(devise) references Devise(id))'
                  )

        conn.execute('CREATE TABLE IF NOT EXISTS Personne'
                  '(id           INTEGER PRIMARY KEY AUTOINCREMENT,'
                  'name          TEXT,'
                  'phone         TEXT,'
                  'email  TEXT,'
                  'address     TEXT,'
                  'latlng    TEXT,'
                  'salaire    DOUBLE,'
                  'age    INTEGER,'
                  'country       INTEGER NULL,'
                  'foreign key(country) references Country(id))')

    @classmethod
    def insertCountry(cls, country: list):
        for dat in country:
            conn.execute('INSERT INTO Country(name, flag, devise) values(?, ?, ?)',
                (dat.get('name'), dat.get('flag'), dat.get('devise')))



    @classmethod
    def insertPersonne(cls, country: list):
        for dat in country:
            conn.execute('INSERT INTO Personne(name, phone, email, address, latlng, salaire, age, country) values(?, ?, ?, ?, ?, ?, ?, ?)',
                (dat.get('name'), dat.get('phone'), dat.get('email'), dat.get('address'), dat.get('latlng'), dat.get('salaire'), dat.get('age'), dat.get('country')))



    @classmethod
    def insertDevise(cls, devise: list):
        for dat in devise:
            conn.execute('INSERT INTO Devise(devise, valeur, en_xof) values(?, ?, ?)',
                (dat.get('devise'), dat.get('valeur'), dat.get('enXOF')))




    @classmethod
    def main(cls):
        cls.createTable()
        cls.insertDevise(CurrencyScrapper.main())
        cls.insertCountry(PrepasCountry.main())
        cls.insertPersonne(PrepasPersonne.main())

        return 'Donéees Insérées avec succés  >-----<'


    
if __name__ == '__main__':
    print(SqlFactory.main())

    print('\n')

    print('GET DES DEVISES')

    print('\n')
    
    for row in conn.execute("select * from devise"):
        print(row)