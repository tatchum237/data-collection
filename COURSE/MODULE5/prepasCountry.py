
from country import Countries

from libraries.utils import Utils

import pandas as pd


class PrepasCountry(object):
    @classmethod
    def openCountries(cls, data):
        return pd.DataFrame(data)


    @classmethod
    def addDeviseToCountry(cls, data):
        START = 1
        FINAL = 8
        data['devise'] = 0
        data['devise'] = data['devise'] \
            .apply(lambda x: Utils.randomize(START, FINAL))
        return data


    @classmethod
    def main(cls):
        data = cls.openCountries(Countries.main())
        data = cls.addDeviseToCountry(data)
        data = data \
            .T \
            .to_dict() \
            .values()
        return list(data)




if __name__ == '__main__':
    print(PrepasCountry.main())
