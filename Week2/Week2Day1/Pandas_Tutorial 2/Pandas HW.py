#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'Week2/Week2Day1/Pandas_Tutorial 2'))
	print(os.getcwd())
except:
	pass

#%%
# 1-21 and # 57-60
import pandas as pd


#%%
# 2. Print the version of pandas that has been imported.

pd.__version__


#%%
# 3. Print out all the version information of the libraries that are required by the pandas library.

pd.show_versions()


#%%
import numpy as np

data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


#%%
#4. Create a DataFrame df from this dictionary data which has the index labels.
#5. Display a summary of the basic information about this DataFrame and its data.
df = pd.DataFrame(data, index=labels)
df


#%%
#6. Return the first 3 rows of the DataFrame df.

df.head(3)


#%%
#7. Select just the 'animal' and 'age' columns from the DataFrame df.

df[["animal", "age"]]


#%%
#8. Select the data in rows [3, 4, 8] and in columns ['animal', 'age'].
# an example:  data.iloc[[0,3,6,24], [0,5,6]] # 1st, 4th, 7th, 25th row + 1st 6th 7th columns.

df.iloc[[2,3,7],[0,1]]


#%%
#9 9. Select only the rows where the number of visits is greater than 3.

df[df['visits'] > 3]


#%%
#10. Select the rows where the age is missing, i.e. is NaN.

df[df['age'].isnull()]


#%%
#11 11. Select the rows where the animal is a cat and the age is less than 3.
# under_15_males = df.loc[ (df['gender'] == 'M') & (df['age'] < 15) ]

cats_under_3 = df.loc[( df['animal'] == 'cat') & (df['age'] < 3)]
cats_under_3


#%%
#12. Select the rows the age is between 2 and 4 (inclusive).

df.loc[(df['age'] >= 2) & (df['age'] <= 4)]

# better answer is df[df['age'].between(2, 4)]


#%%
#13. Change the age in row 'f' to 1.5.
df.loc['f', 'age'] = 1.5  # changed in place
df.iloc[[5]]


#%%
#14. Calculate the sum of all visits.

df['visits'].sum()


#%%
#15. Calculate the mean age for each different animal in df.
df.groupby('animal')['age'].mean()


#%%
#16. Append a new row 'k' to df with your choice of values for each column. Then delete that row to return the original DataFrame.

df.loc['k'] = [5.5, 'dog', 'no', 2]

# and then...

df = df.drop('k')


#%%
#17. Count the number of each type of animal in df.

# reset the db here since it was getting messy - you can always make copies
# example: df_bitcoin_expanded = df_bitcoin.copy()

df = pd.DataFrame(data, index=labels)
df.groupby('animal').sum()


#%%
# 18. Sort df first by the values in the 'age' in decending order, then by the value in the 'visit' column in ascending order.

df.sort_values(by=['age', 'visits'], ascending=[False,True])




#%%
#19. The 'priority' column contains the values 'yes' and 'no'. 
# Replace this column with a column of boolean values: 'yes' should be True and 'no' should be False.

df['priority'] = df['priority'].map({'yes': True, 'no': False})
df
#output comes back NaN for some reason


#%%
#20. In the 'animal' column, change the 'snake' entries to 'python'.


df['animal'] = df['animal'].replace('snake', 'python')
df


#%%
#2121. For each animal type and each number of visits, find the mean age (hint: use a pivot table).

df.pivot_table(index='animal', columns='visits', values='age', aggfunc='mean')


#%%
#57. Columns in your DataFrame can also be used to modify colors and sizes. Bill has been keeping track of his performance at work over time, as well as how good he was feeling that day, and whether he had a cup of coffee in the morning. Make a plot which incorporates all four features of this DataFrame.

(Hint: If you're having trouble seeing the plot, try multiplying the Series which you choose to represent size by 10 or more)

The chart doesn't have to be pretty: this isn't a course in data viz!

df = pd.DataFrame({"productivity":[5,2,3,1,4,5,6,7,8,3,4,8,9],
                   "hours_in"    :[1,9,6,5,3,9,2,9,1,7,4,2,2],
                   "happiness"   :[2,1,3,2,3,1,2,3,1,2,2,1,3],
                   "caffienated" :[0,0,1,1,0,0,0,0,1,1,0,1,0]})


#%%

#58. What if we want to plot multiple things? Pandas allows you to pass in a matplotlib Axis object for plots, and plots will also return an Axis object.

Make a bar plot of monthly revenue with a line plot of monthly advertising spending (numbers in millions)

df = pd.DataFrame({"revenue":[57,68,63,71,72,90,80,62,59,51,47,52],
                   "advertising":[2.1,1.9,2.7,3.0,3.6,3.2,2.7,2.4,1.8,1.6,1.3,1.9],
                   "month":range(12)
                  })


#%%
import numpy as np
def float_to_time(x):
    return str(int(x)) + ":" + str(int(x%1 * 60)).zfill(2) + ":" + str(int(x*60 % 1 * 60)).zfill(2)

def day_stock_data():
    #NYSE is open from 9:30 to 4:00
    time = 9.5
    price = 100
    results = [(float_to_time(time), price)]
    while time < 16:
        elapsed = np.random.exponential(.001)
        time += elapsed
        if time > 16:
            break
        price_diff = np.random.uniform(.999, 1.001)
        price *= price_diff
        results.append((float_to_time(time), price))
    
    
    df = pd.DataFrame(results, columns = ['time','price'])
    df.time = pd.to_datetime(df.time)
    return df

#Don't read me unless you get stuck!
def plot_candlestick(agg):
    """
    agg is a DataFrame which has a DatetimeIndex and five columns: ["open","high","low","close","color"]
    """
    fig, ax = plt.subplots()
    for time in agg.index:
        ax.plot([time.hour] * 2, agg.loc[time, ["high","low"]].values, color = "black")
        ax.plot([time.hour] * 2, agg.loc[time, ["open","close"]].values, color = agg.loc[time, "color"], linewidth = 10)

    ax.set_xlim((8,16))
    ax.set_ylabel("Price")
    ax.set_xlabel("Hour")
    ax.set_title("OHLC of Stock Value During Trading Day")
    plt.show()


#%%
#59. Generate a day's worth of random stock data, and aggregate / reformat it so that it 
#has hourly summaries of the opening, highest, lowest, and closing prices




#%%
#60. Now that you have your properly-formatted data, try to plot it yourself as a candlestick chart. Use the plot_candlestick(df) function above, or matplotlib's plot documentation i
#If you get stuc



