from concatfile import final_data


# print(final_data.head())
# print(final_data.describe())#to see mean std min max
# print(final_data.shape)
f_data=final_data.drop(['Domain'],axis=1)#removing domain column
# print(f_data.shape)
# print(f_data.isnull().sum())#check empty values or missing values,,,,.sum() totals the  number of null for each column
f_data=f_data.sample(frac=1).reset_index(drop=True)#to shuffle data ...frac means fraction
# print(f_data.head())
