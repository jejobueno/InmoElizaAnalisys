import pandas as pd

from utils.DataAnalyser import DataAnalyser

housing = pd.read_csv('assets/housing-data.csv', index_col=0)

dataAnalyser = DataAnalyser(housing)
dataAnalyser.clean()
dataAnalyser.analyze()
