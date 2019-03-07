def graph1(data1, data2): #creates a function for plotting two bar charts 
    fig , ((ax1), (ax2)) = plt.subplots(1,2, figsize=(18,6)) #sets the figure size and creates two subplots
 
    ax1.hist(priceinth, bins='auto', color = '#7663b0', edgecolor='k', alpha = 0.5, label = 'Prices')
    #plots a histogram for prices given in $1000
    #sets bins, the edgecolor to black, the label, the color, and the transparency
    ax2.hist(sqft_living, bins='auto', color = '#86bf91', edgecolor='k', alpha = 0.75, label = 'Areas of living')
    #plots a histogram for areas of living given in sq.ft.
    #sets bins, the edgecolor to black, the label, the color, and the transparency
         
    ax1.plot([data1.mean()/1000, data1.mean()/1000],[0.0,1100.0],'--',color='black',label="Mean of house prices")
    #creates a vertical line for the mean of the data
    ax1.plot([np.median(priceinth), np.median(priceinth)],[0.0,1100.0], '-.', color='red', 
             label="Median of house prices")
    #creates a vertical line for the median of the data
    ax2.plot([data2.mean(), data2.mean()],[0.0,900.0], '--',color='black',label="Mean of areas of living")
    #creates a vertical line for the mean of the data
    ax2.plot([data2.median(), data2.median()],[0.0,900.0],'-.', color='red', label="Median of areas of living")
    #creates a vertical line for the median of the data
    
    ax1.set_ylabel('Frequency') #sets ylabel for first figure
    ax1.set_xlabel('Prices ($1000)') #sets xlabel for first figure
    ax1.set_title('Distrbution of house prices') #sets title name for first figure
    ax1.legend(loc = 'upper right') #shows the legend that is located in the upper right corner for first figure
        
    ax2.set_ylabel('Frequency') #sets ylabel for second figure
    ax2.set_xlabel('Areas of living (sq.ft.)') #sets xlabel for second figure
    ax2.set_title('Distrbution of areas of living') #sets title name for second figure
    ax2.legend(loc = 'upper right') #shows the legend that is located in the upper right corner for second figure

    ax1.grid() #creates a grid for first figure
    ax2.grid() #creates a grid for second figure
    
graph1(house['price'],house['sqft_living']) #calls the function to plot two histograms


with sns.plotting_context("talk",font_scale=2.5): 
    #returns a parameter dictionary to scale elements of the figure
    g = sns.pairplot(house[['sqft_lot','sqft_above','bathrooms','sqft_living',
                            'bedrooms']], palette='blue',size=7) 
    #plots pairwise relationships between the independent variables in the list
g.set(xticklabels=[]) #deletes the ticks on the x-axis not to distract the viewer

X = house['sqft_living'] #assigns the dataframe with values of areas of living to a variable 'X'
X = statsmodels.add_constant(X) #defaults an intercept to 0
y = house['price'] #assigns the dataframe with values of prices to a variable 'Y'

model = statsmodels.OLS(y, X).fit() 
#makes a simple ordinary least squares (OLS) model for the given predictor and response variables

model.summary() #shows the summary of the OLS analysis

import warnings #imports a library that will help to get rid of the warnings 
warnings.simplefilter(action='ignore') #ignores the warnings 

def regression_model(column_x, column_y):
    #creates a function that uses libraries to make a scatter plot
    #plots the residuals, computes the R-squared, and displays the regression equation

    X = statsmodels.add_constant(house[column_x]) #defaults an intercept to 0 using house['column_x'] dataframe
    Y = house[column_y] #assigns the dataframe with values of column_y to a variable 'Y'
    regressionmodel = statsmodels.OLS(Y,X).fit() 
    #makes a simple ordinary least squares (OLS) model for the given predictor and response variables

    #extracts regression parameters from model, rounded to 3 decimal places
    Rsquared = round(regressionmodel.rsquared,3)
    slope = round(regressionmodel.params[1],3)
    intercept = round(regressionmodel.params[0],3)

    #plots
    sns.set_style("whitegrid") #sets the aesthetics of the graph  
    fig, (ax1, ax2) = plt.subplots(ncols=2, sharex=True, figsize=(16,5)) 
    #creates 2 subplots, sets number of columns, and defines the figure size
    sns.regplot(x=column_x, y=column_y, data=house, marker="+", ax=ax1) #plots data and a linear regression model fit 
    #uses "+" instead of dots on the first figure within subplots
    ax1.set(ylabel='Price ($)', xlabel='Living square footage (sq.ft.)') #sets the axis labels
    sns.residplot(x=column_x, y=column_y, data=house, ax=ax2) #plots residuals within second figure using the same data
    ax2.set(ylabel='Residuals', xlabel='Living square footage  (sq.ft.)') #sets label for y-axis on second figure
    ax2.set_ylim(min(regressionmodel.resid)-1,max(regressionmodel.resid)+1) #sets limit for y-axis
    plt.figure(figsize=(7,5)) #creates a figure and sets its size
    sns.distplot(regressionmodel.resid, kde=True, axlabel='Residuals', color='purple') 
    #plots a distribution of observations for the residuals and sets a color and label
    plt.ylabel('Frequency') #sets the label for y-axis 
    
    qqplot = statsmodels.qqplot(regressionmodel.resid,fit=True,line='45')
    qqplot.suptitle("Normal Probability (\"QQ\") Plot for Residuals",fontweight='bold',fontsize=14)

    #print the results:
    print("R-squared = ",Rsquared) #prints the r-squared value 
    print("Regression equation: "+column_y+" = ",slope,"* "+column_x+" + ",intercept) #prints the regression equation
    
regression_model('sqft_living','price')

sns.set(style="white", font_scale=1.45)  #sets aesthetic parameters
features = ['price','bedrooms','bathrooms','sqft_living','sqft_lot',
            'sqft_above','sqft_basement'] 
#creates a list containing all names of columns from house dataset

mask = np.zeros_like(house[features].corr(), dtype=np.bool) 
#returns an array of zeros with the same shape and type as a given array 
mask[np.triu_indices_from(mask)] = True 
#returns the indices for the upper-triangle of arrays 

f, ax = plt.subplots(figsize=(16, 12)) #creates a figure and sets a size
plt.title('Pearson Correlation Matrix',fontsize=25) 
#sets a title and the size of the font


sns.heatmap(house[features].corr(),linewidths=0.25,vmax=1.0,square=True,cmap="rainbow", 
            linecolor='w',annot=True,mask=mask,cbar_kws={"shrink": .85}) 
#plots a heatmap with the correlation coefficients using the dataset

f, ax = plt.subplots(figsize=(16, 12)) #creates a figure and sets a size
plt.title('R-Squared Matrix',fontsize=25) #sets a title and the size of the font

sns.heatmap(house[features].corr()*house[features].corr(),linewidths=0.25,vmax=1.0,
            square=True,cmap="rainbow", linecolor='w',
            annot=True,mask=mask,cbar_kws={"shrink": .85})
#plots a heatmap with the r-squared using the dataset
