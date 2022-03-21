import pandas as pd
import os
import shutil

# Copy file from Connected Volume to Local Folder for editing
shutil.copy("/path/to/remote/file", "/path/to/local/folder")

# Open data as dataframe (df)
df = pd.read_csv("/path/to/local/folder")

# Drop unnecessary spacer row ------- at index 0 and the last row by index -1. Your unique formatting needs should go here.
df = df.drop(labels=0, axis=0)
df.drop(index=df.index[-1],axis=0,inplace=True)
# Convert dollar columns to float. Your unique formatting needs should go here.
df = df.astype({'SundaySales':'float','MondaySales':'float', 'TuesdaySales':'float', 'WednesdaySales':'float', 'ThursdaySales':'float', 'FridaySales':'float', 'SaturDaySales':'float'})

# Comment out code below if sneaky NaNs make their way into the data
# df['ReportDate'].replace('', np.nan, inplace=True)

# Convert ReportDate column from object type to date type in mmddyy format
df['ReportDate'] = pd.to_datetime(df['ReportDate'])
df['ReportDate'] = df['ReportDate'].dt.strftime('%m/%d/%y')

# Type and print statements for debugging
# df = df.dtypes
# print(df)

# Export formatted file to a new file with no index or header to be imported into database.
df.to_csv("/path/to/smart/folder", index=False, header=False)
