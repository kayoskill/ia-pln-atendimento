import re

import pandas as pd


def tratamento(arquivo):
    dataframe = pd.read_csv(arquivo, sep=';', header=1)
    return dataframe

if __name__ == '__main__':
    dados = tratamento('base/basehub.csv')
    print(dados)
