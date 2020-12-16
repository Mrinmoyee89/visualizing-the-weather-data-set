# --------------
# Import the required Libraries
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import calendar
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# Generate a line chart that visualizes the readings in the months

def line_chart(df,period,col):
    """ A line chart that visualizes the readings in the months
    
    This function accepts the dataframe df ,period(day/month/year) and col(feature), which plots the aggregated value of the feature based on the periods. Ensure the period labels are properly named.
    
    Keyword arguments:
    df - Pandas dataframe which has the data.
    period - Period of time over which you want to aggregate the data
    col - Feature of the dataframe
    
    """
    line_chart_dataset = df.groupby(pd.Grouper(freq='M'))[[col]].mean()
    return (plt.plot(line_chart_dataset.index.month_name(),
            line_chart_dataset[col]),plt.ylim((-10, 25)),
            plt.xlabel('Months'),
            plt.ylabel('Temp (C)'),
            plt.title('Temperature Trend 2020'),
            plt.xticks(rotation = 90))  
    







# Function to perform univariate analysis of categorical columns
def plot_categorical_columns(df):
    """ Univariate analysis of categorical columns
    
    This function accepts the dataframe df which analyzes all the variable in the data and performs the univariate analysis using bar plot.
    
    Keyword arguments:
    df - Pandas dataframe which has the data.
    
    """
    return df.value_counts(normalize=True).plot(kind='bar')








# Function to plot continous plots
def plot_cont(df,plt_typ):
    """ Univariate analysis of Numerical columns
    
    This function accepts the dataframe df, plt_type(boxplot/distplot) which analyzes all the variable in the data and performs the univariate analysis using boxplot or distplot plot.
    
    Keyword arguments:
    df - Pandas dataframe which has the data.
    plt_type - type of plot through which you want to visualize the data
    
    """
    continous =df.columns.tolist()
    for column in continous:
        if plt_typ == "distplot":
            plt.figure()
            sns.distplot(numerical_dataset[column])
        if plt_typ == "boxplot":
            plt.figure()
            sns.boxplot(numerical_dataset[column])
        else:
                print("Pass either distplot/boxplot")
    







# Function to plot grouped values based on the feature
def group_values(df,col1,agg1,col2):
    """ Agrregate values by grouping
    
    This function accepts a dataframe, 2 column(feature) and aggregated function(agg1) which groupby the dataframe based on the column and plots the bar plot.
   
    Keyword arguments:
    df - Pandas dataframe which has the data.
    col1 - Feature of the dataframe on which values will be aggregated.
    agg1 - Dictionary of aggregate functions with feature as the key and func as the value
    col2 - Feature of the dataframe to be plot against grouped data.
    
    Returns:
    grouping - Dataframe with all columns on which it is grouped on.
    """
    agg1={'mean':np.mean, 'max':np.max, 'min':np.min}
    g=df.groupby([col1])[col2].mean()
    return g.plot(kind='bar', figsize=(12,4))
    




# Read the Data and pass the parameter as parse_dates=True, index_col='Date/Time'
weather_df=pd.read_csv(path,parse_dates=True, index_col='Date/Time' )
#print(weather_df)

categorical_dataset = weather_df.select_dtypes(include = 'object')
numerical_dataset = weather_df.select_dtypes(include = 'number')

# Lets try to generate a line chart that visualizes the temperature readings in the months.
# Call the function line_chart() with the appropriate parameters.

print(line_chart(numerical_dataset,numerical_dataset.index,'Temp (C)'))


# Now let's perform the univariate analysis of categorical features.
# Call the "function plot_categorical_columns()" with appropriate parameters.

print(plot_categorical_columns(categorical_dataset['Weather']))


# Let's plot the Univariate analysis of Numerical columns.
# Call the function "plot_cont()" with the appropriate parameters to plot distplot
print(plot_cont(numerical_dataset,"distplot" ))


# Call the function "plot_cont()" with the appropriate parameters to plot boxplot
print(plot_cont(numerical_dataset,"boxplot" ))

# Groupby the data by Weather and plot the graph of the mean visibility during different weathers. Call the function group_values to plot the graph.

print(group_values(weather_df,'Weather','mean','Visibility (km)'))

# Feel free to try on diffrent features and aggregated functions like max, min.

print(group_values(weather_df,'Weather','max','Visibility (km)'))
print(group_values(weather_df,'Weather','min','Visibility (km)'))







