from typing import Union

import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from scipy import stats

from utils.realStateBelgiumStats import splitByRegions, createDataFrameStat


class DataAnalyser:

    def __init__(self, df):
        self.df = df
        self.housing_data = dict()
    def clean(self) -> pd.DataFrame:
        # We clean first all the entirely empty rows
        self.df.dropna(how='all', inplace=True)

        # We delete the blank spaces at the beginning and end of each string
        self.df.apply(lambda x: x.strip() if type(x) == str else x)

        # Fixing errors
        # Fixing variable hasFullyEquippedKitchen
        has_hyperEquipped = self.df['kitchenType'].apply(lambda x: 1 if x == 'HYPER_EQUIPPED' else 0)
        has_USHyperEquipped = self.df['kitchenType'].apply(lambda x: 1 if x == 'USA_HYPER_EQUIPPED' else 0)
        self.df.hasFullyEquippedKitchen = has_hyperEquipped | has_USHyperEquipped

        # Dropping rows with price as NaN values
        self.df = self.df[self.df['price'].notna()]
        self.df = self.df[self.df['area'].notna()]

        # Dropping duplicated values
        self.df = self.df.drop_duplicates(subset=['area', 'price'], keep='last')

        # Deleting constant variable 'typeSale'
        del self.df['typeSale']

        # Filling up empty values with np.NaN
        self.df.replace(r'^\s*$', np.nan, regex=True)

    def analyze(self):
        # Target value is price
        sns.set_theme()

        # Let's see if there is strong correlations between our values,
        # we drop postalCode because it is a qualitative option
        plt.figure()
        features = self.df.drop('postalCode', axis=1)
        sns.heatmap(features.corr(), center=0, cmap="YlGnBu")
        plt.xticks(rotation=40)

        # Most correlated features
        print('###### Most correlated features ######')
        greatestInfluence = abs(features.corr())[:]['price'].drop('price').sort_values(ascending=False)
        print(greatestInfluence.head())

        # Least correlated features
        print('\n ##### Least correlated features ######')
        worstInfluence = abs(features.corr())[:]['price'].drop('price').sort_values(ascending=True)
        print(worstInfluence.head())

        # Normalizing price variable
        self.df["logPrice"] = np.log(self.df.price)
        self.df["sqtArea"] = np.sqrt(self.df.area)
        sns.displot(self.df.logPrice, kde=True)

        self.df['pricePerSqtMeter'] = (self.df['price'].div(self.df['area']))

        # Plot to observe the linear relationship between price and area
        plot = sns.jointplot(x='area', y='price', data=self.df, kind='reg')
        plot.ax_joint.scatter(x='area', y='price', data=self.df)

        # Eliminate the price outliers representing less than 3% of the df
        self.df = self.df[(np.abs(stats.zscore(self.df.price)) < 3)]
        # plt.title('Area vs Price (Normalized)')
        # plot.ax_marg_x.set_xlim(-10, 1000)
        print(self.df.shape)

        plot = sns.jointplot(x='sqtArea', y='price', data=self.df, kind='reg')
        plot.ax_joint.scatter(x='sqtArea', y='price', data=self.df, c='g')

        # Plot to observe the linear relationship between price and area
        plot = sns.jointplot(x='terraceSurface', y='price', data=self.df, kind='reg')
        plot.ax_joint.scatter(x='terraceSurface', y='price', data=self.df, c='r')

        percent_missing = self.df.isnull().sum() * 100 / len(self.df)
        print(percent_missing)

        # qualitative values

        # Separating the data set by regions
        self.housing_data = splitByRegions(self.df)

        # Look for mean price, median price and mean price by square meter
        # for the most and least expensive municipalities of each region
        for key, df in self.housing_data.items():
            createDataFrameStat(self.df, df, key)

        # Now the data for the whole belgium
        createDataFrameStat(self.df, self.df, 'Belgium')

        qualitative = ['typeProperty', 'subtypeProperty', 'subtypeSale', 'kitchenType',
                       'buildingCondition', 'hasSwimmingPool', 'hasGarden', 'hasTerrace', 'BedroomsCount']
        for variable in qualitative:
            plt.figure()
            sns.boxplot(x=variable, y='price', data=self.df)
            plt.xticks(rotation=40)
            plt.show()





