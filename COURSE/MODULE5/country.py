
import requests


import secrets


BASE_URL = 'https://restcountries.com/v2/all'

class Countries(object):
    @classmethod
    def fetchAll(cls, url: str):
        with requests.Session() as session:
            data = session.get(url)
        return  data.json()
    
    @classmethod
    def modifyData(cls, data):
        def construct(item):
            val = {}
            val['name'] = item.get('name')
            val['flag'] = item.get('flag')
            return val
        return list(map(construct, data))
    

    @classmethod
    def value(cls, data):
        val = []
        for item in data:
            val.append(cls.selectRandom(data))
        return val

    def selectRandom(names):
        return secrets.choice(names)


    @classmethod
    def main(cls):
        data = cls.fetchAll(BASE_URL)
        data = cls.value(data)
        data = cls.modifyData(data)
        return data

 
 
 
if __name__ == '__main__':
    print(Countries.main())