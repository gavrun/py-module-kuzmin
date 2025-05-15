import pandas as pd

my_series = pd.Series([5, 6, 7, 8, 9, 10])
print(my_series)
print(my_series[4])

fixed_df = pd.read_csv('bikes.csv',
                       sep=';', encoding='latin1',
                       parse_dates=['Date'], dayfirst=True,
                       index_col='Date')
fixed_df[:3]

#print(fixed_df)
print(fixed_df['Berri 1'][:10])
