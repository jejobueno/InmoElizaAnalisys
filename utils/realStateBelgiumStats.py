from typing import Dict

import pandas as pd


def splitByRegions(df: pd.DataFrame) -> Dict[str, pd.DataFrame]:
    # For Wallonia:
    A = ((df['postalCode']) >= 1300) & ((df['postalCode']) < 1499)
    B = ((df['postalCode']) >= 4000) & ((df['postalCode']) < 7999)

    housing_wallonia = df[A | B]

    # For Brussels:
    C = ((df['postalCode']) >= 1000) & ((df['postalCode']) < 1299)

    housing_brussels = df[C]
    # For Flanders:
    D = ((df['postalCode']) >= 1500) & ((df['postalCode']) < 3999)
    E = ((df['postalCode']) >= 8000) & ((df['postalCode']) < 9999)

    housing_flanders = df[D | E]

    return {'Wallonia': housing_wallonia, 'Brussels': housing_brussels, 'Flanders': housing_flanders}


def createDataFrameStat(original_df: pd.DataFrame, df_splited: pd.DataFrame, region: str):
    pd.set_option('display.max_columns', None)

    hosesByMeanPrice = df_splited.groupby('postalCode').mean()
    hosesByMeanPrice['priceByM2'] = hosesByMeanPrice['price'] / hosesByMeanPrice['area']
    hosesByMeanPrice = hosesByMeanPrice.sort_values('priceByM2')[['price','priceByM2']]

    houseGrouped = df_splited.groupby(['postalCode','typeProperty'])
    statsHousing = houseGrouped.mean().sort_values('price')['price'].to_frame()
    statsHousing = statsHousing.rename(columns={'price': 'meanPrice'})

    statsHousing['meanArea'] = houseGrouped.mean().sort_values('price')['area']

    statsHousing['medianPrice'] = houseGrouped.median().sort_values('price')['price']

    statsHousing['medianArea'] = houseGrouped.median().sort_values('price')['area']

    statsHousing['priceByM2'] = statsHousing['meanPrice'] / statsHousing['meanArea']

    percent_of_df = df_splited.shape[0] * 100 / original_df.shape[0]

    statsHousing = statsHousing.reindex(hosesByMeanPrice.index, level=0)

    print(f"##### percentage in {region}: #######\n"
          f"Percentage of DataFrame: {percent_of_df}\n"
          f"Mean price in {region}: {df_splited.price.mean()}\n"
          f"Median price in {region}: {df_splited.price.median()}\n"
          f"Mean price by square meter in {region}: {df_splited.pricePerSqtMeter.mean()}\n"
          f""
          f"##### The 5 least expensive Municipalities in {region} ###### \n"
          f"{statsHousing.iloc[0:10]}\n"
          f"##### The 5 most expensive Municipalities in {region} ###### \n"
          f"{statsHousing.iloc[-10:-1]}\n")

    return None
