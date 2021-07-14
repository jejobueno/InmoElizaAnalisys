# InmoElizaAnalisys
Preliminary analysis to gather some information for Machine Learning ALgorithm for the prediction of the house prices in Belgium.

## DATA

We are working with a dataset created from scrapping the website inmoweb.be by looking for queries to get the prices of appartements and houses around Belgium. This dataset was cleaned applying the following criterias:

1. Drop all the entirely empty rows
2. Delete the blank spaces at the beginning and end of each string
3. Fixing errors:
    Fixing variable hasFullyEquippedKitchen setting value '1' if the appartement has 'HYPER_EQUIPPED' or 'USA_HYPER_EQUIPPED' and '0' in the opposite case
 4. Dropping rows with price as NaN values
 5. Dropping duplicated values
 6. Deleting constant variable 'typeSale'
 7. Filling up empty values with np.NaN

![image](https://user-images.githubusercontent.com/34608190/125642974-9c452792-5bbf-4c76-82f3-b4d1196d448c.png)

## VISUALIZATION

We first visualiza the relationship between the vairables and the target (price) in a heatmap:

![image](https://user-images.githubusercontent.com/34608190/125638935-403bc716-3d60-403c-a5ac-d9978d8cd006.png)


1. The three variables with the highest correlation are:

  | Variable         | Correlation |
  |---------------:|------:|
  |area            | 0.58  |
  |BedroomsCount   | 0.40  |
  |hasSwimmingPool | 0.35  |


2. The three variables with the highest correlation are:
 
  | Variable         | Correlation |
  |---------------:|------:|
  |hasSwimmingPool | 0.11  |
  |hasGarden       | 0.07  |
  |isFurnished     | 0.01  |


Then we explore the behavior of the house prices in relation to the area. The data was standarize the data taking the logarithm of the price and the square root of the area 

![image](https://user-images.githubusercontent.com/34608190/125641869-6ae6e182-c8d2-4f9e-879f-40f982aa2f33.png)


## Some questions to answerd:

We also looked at the average price per square meter in different regions of belgium (Brussels, Wallonia, Flanders) and in the whole Belgium.

### Brussels

![image](https://user-images.githubusercontent.com/34608190/125643999-3f9be88a-d43a-4bc1-9875-51fae5dd876f.png)![image](https://user-images.githubusercontent.com/34608190/125644086-8e6f117c-af22-4510-b756-0657fd70e9f6.png)



