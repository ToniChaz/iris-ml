# Load dataset

import pandas


def load_data():
    url = "data/iris.data"
    names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
    return pandas.read_csv(url, names=names)
