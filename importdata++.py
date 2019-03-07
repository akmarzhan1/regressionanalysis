import pandas as pd #imports pandas library and binds it to the name "pd"
import numpy as np #imports numpy library and binds it to the name "np"
import matplotlib.pyplot as plt #imports "matplotlib.pyplot" module and binds it to the name "plt"
from scipy import stats #imports "stats" module from scipy library
import matplotlib #import matplotlib library
%matplotlib inline
import statsmodels.api as statsmodels #useful stats package with linear regression functions
import seaborn as sns #very nice plotting package

#imports House dataset using pandas
house=pd.read_csv('/users/ohsehun/desktop/CS51-Correlation Report/house.csv') #reads the dataset into a "dataframe"
house.head(10) #shows the first 10 rows of the data

house.describe() #prints the summary of the statistics (count, mean, standard deviation, etc.)

#Bessel's correction is used by default (as explained in the documentation)
#it means that the denominator when computing the std is not n, but (n-1)
#shown here (https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.std.html)

def descriptivestats(dataset): #creates a function that computes the median, range and mode using library functions
    print("– Median is", dataset.median()) #computes and prints the median of the dataset
    print("– Mean is", dataset.mean())
    print("– Standard deviation is", dataset.std()) #computes and prints the standard deviation 
    #Bessel's correction is used by default (as explained in the documentation)
    #it means that the denominator when computing the std is not n, but (n-1)
    #shown here (https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.std.html)
    print("– Range is", dataset.max()-dataset.min()) #computes and prints the range
    print("– Minimum value is", dataset.min()) #computes and prints the minimum house price
    print("– Maximum value is", dataset.max()) #computes and prints the maximum house price
    print("– Mode is", dataset.mode()[0]) #computes and prints the mode of the dataset

print("The descriptive statistics for the price of the houses: \n") #prints the string 
descriptivestats(house['price']) #calls the function "descriptivestats" for the prices

print('\nThe descriptive statistics for the area of living:') #prints the string
descriptivestats(house['sqft_living']) #calls the function "descriptivestats" for the area of living

price=list(house['price'].values) #turns the dataframe into a list for easier analysis
priceinth=[] #creates an empty list
for i in range(21613): #creates a loop that iterates 21613 times
    priceinth.append(price[i]/1000) #makes a new list with prices given in $1000
bedrooms=list(house['bedrooms'].values) #turns the dataframe into a list for easier analysis
bathrooms=list(house['bathrooms'].values) #turns the dataframe into a list for easier analysis
sqft_living=list(house['sqft_living'].values) #turns the dataframe into a list for easier analysis
sqft_lot=list(house['sqft_lot'].values) #turns the dataframe into a list for easier analysis
sqft_above=list(house['sqft_above'].values) #turns the dataframe into a list for easier analysis
sqft_basement=list(house['sqft_basement'].values) #turns the dataframe into a list for easier analysis
lat=list(house['lat'].values) #turns the dataframe into a list for easier analysis
long=list(house['long'].values) #turns the dataframe into a list for easier analysis
