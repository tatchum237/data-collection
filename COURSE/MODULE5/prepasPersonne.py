from concatenation import ConcatFactory
from libraries.utils import Utils

import pandas as pd


class PrepasPersonne(object):
    @classmethod
    def open(cls, data):
        return pd.DataFrame(data)

    @classmethod
    def addCountryToPersonne(cls, data):
        START = 1
        FINAL = 249
        data['country'] = 0
        data['country'] = data['country'] \
            .apply(lambda x: Utils.randomize(START, FINAL))
        return data


    @classmethod
    def main(cls):
        data = cls.open(ConcatFactory.main())
        data = cls.addCountryToPersonne(data)
        data = data \
            .T \
            .to_dict() \
            .values()
        return data




if __name__ == '__main__':
    print(PrepasPersonne.main())
