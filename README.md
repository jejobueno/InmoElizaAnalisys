# InmoElizaAnalisys
Preliminary analysis to gather some information for Machine Learning ALgorithm for the prediction of the house prices in Belgium.

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
