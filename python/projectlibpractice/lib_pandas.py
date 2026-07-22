"series"
# import pandas as pd
# stock = pd.Series([50, 12, 85, 0, 23], index=['a', 'b', 'c', 'd', 'e'])
# # print(stock)

# "accessing by lablel"
# print(stock['c'])

# "accessing by index using iloc"
# print(stock.iloc[-1])

# "filtering in series"
# print(stock[stock<15])



"dataframe"
# import pandas as pd
# data = {
#     'Item' : ['a', 'b', 'c', 'd', 'e'],
#     'Stock' : [50, 12, 85, 0 ,23],
#     'Price' : [1.5, 0.75, 2.0, 1.1, 3.5]
# }

# store_df = pd.DataFrame(data)
# print(store_df)

"math operation on dataframe"
# store_df['Total_Value'] = store_df['Stock']*store_df['Price']
# print(store_df)

"multi condition filtering on dataframe"
# print(store_df[(store_df['Stock']>0) & (store_df['Price']<2.0)])

"aggregation (summary metrics)"
# total_sum_value = store_df['Total_Value'].sum()
# print(total_sum_value)
# average_price = store_df['Price'].mean()
# print(average_price)

"grouping and categorizing data (groupby)"
# store_df['Category'] = ['Fruit', 'Fruit', 'Fruit', 'Fruit', 'Berry']
# sum_total_value = store_df.groupby('Category')['Total_Value'].sum()
# print(sum_total_value)





""" Create two Pandas Series objects manually.Series A should have
values [10, 20, 30] with indices ['x', 'y', 'z'].Series B should have
values [100, 200, 300] with indices ['y', 'z', 'w'].Add them together
(Series A + Series B). Write down the exact resulting index labels and
their values. Then, provide a secondary code solution that adds the
together but forces any missing overlapping labels to treat their
missing partner as 0 instead of turning into a null value."""

# import pandas as pd
# seriesA = pd.Series([10,20,30], index=('x','y','z'))
# seriesB = pd.Series([100,200,300], index=('y','z','w'))
# seriesC = seriesA.add(seriesB, fill_value=0)

# print(seriesC)





"""Given a raw Pandas Series containing erratic data points,
write a line of code to find the index label (not the position number)
of the highest value in the Series. Then, extract the top 3 highest
values sorted from largest to smallest."""

# import pandas as pd
# s = pd.Series([14, 85, 23, 85, 92, 11], index=['row1', 'row2', 'row3', 'row4', 'row5', 'row6'])
# highest = s.idxmax()
# print(highest)
# sorted_s = s.sort_values()
# print(sorted_s)
# print(sorted_s.tail(3))





"""You are handed a Series containing a large list of string
classifications. Write a concise expression to calculate the
percentage composition of each unique value rather than its raw
frequency count. The output values must be expressed as decimals
between 0.0 and 1.0."""

# import pandas as pd

# s = pd.Series(['A', 'B', 'A', 'A', 'C', 'B', 'A', 'C'])
# result_series = s.value_counts(normalize=True)
# print(result_series)





"""Take a Series of numerical values and alter its values completely
using a conditional logic threshold. If a value is strictly below 50,
it should be mapped to the string "Fail". If it is 50 or above, it
should be mapped to the string "Pass"."""
# import pandas as pd
# scores = pd.Series([42, 89, 50, 12, 73])
# def status(score):
#     if score>50:
#         return "pass"
#     else:
#         return "fail"
# result = scores.map(status)
# print(result)





"""You have a Series containing floating-point numbers mixed with null
values (np.nan). Perform a sequential cleanup operation: First, find
out exactly how many missing values exist. Next, fill any missing
values using Forward Fill logic (inheriting the value directly
preceding it). Finally, convert the final array cleanly into standard
64-bit integers"""
# import pandas as pd
# import numpy as np
# data = pd.Series([10.0, np.nan, 20.0, 30.0, np.nan, 40.0])
# result = data.ffill().astype("Int64")
# print(result)
