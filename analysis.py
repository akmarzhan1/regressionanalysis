X = statsmodels.add_constant(house['sqft_living']) #defaults an intercept to 0 using house['column_x'] dataframe
Y = house['price'] #assigns the dataframe with values of column_y to a variable 'Y'
regressionmodel = statsmodels.OLS(Y,X).fit() 
#makes a simple ordinary least squares (OLS) model for the given predictor and response variables

#extracts regression parameters from model, rounded to 3 decimal places
Rsquared = round(regressionmodel.rsquared,3)

def confidence_interval(n): #creates a function that computes a confidence interval
    
    stdx=house['sqft_living'].std() #calculates standard deviation of the areas of living
    stdy=house['price'].std() #calculates standard deviation of the prices
    
    slope=(stdy/stdx)*(Rsquared**(1/2)) #calculates the mean of the list
    
    SE=(((1-Rsquared)/(n-2))**(1/2))*(stdy/stdx) #calculates the standard error
    tscore=stats.t.ppf(0.975, n-2) #calculates the tscore using the degrees of freedom and the confidence level 
    #0.975, since 95% confidence interval would leave two tails with 2.5% in each of them
    
    lowbound = slope - abs(tscore*SE) #calculates the lower bound 
    highbound = slope + abs(tscore*SE) #calculates the upper bound 
    
    return lowbound,highbound #returns the upper and the lower bounds

#calculates the standard deviation of the list using Bessel's correction
#it corrects the downward bias and uses n-1 as a denominator 

n=len(price) #sets n as a length of the list 'price'

print("95% confidence interval:", confidence_interval(n)) 
#calls and prints the function "confidence_interval" for the slope of the least squares line

def corrsign(tails): 
    
    #creates a function that conducts the statistical significance test on correlation coefficient
    n = len(price) #sets the sample size of data
    global pvalue, tscore #make local variables global to be able to print them
 
    tscore = ((Rsquared**(1/2))*(((n-2)/(1-Rsquared))**(1/2))) #computes the tscore
    df = n-2 #uses the n - 2 as degrees of freedom
    
    pvalue = tails*stats.t.cdf(-tscore,df) #computes the pvalue using the tscore and degrees of freedom

    return pvalue, tscore #returns values of these variables

corrsign(2) #calls the function "corrsign" 
print('t =',tscore) #prints the tscore
print('p =',pvalue) #prints the pvalue
