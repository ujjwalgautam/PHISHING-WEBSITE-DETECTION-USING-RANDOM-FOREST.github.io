import pandas as pd


# data1 = pd.read_csv("LegimateURL.csv")
data1 = pd.read_csv("leg.csv")
# print(data1.head())
# data2 = pd.read_csv("PhishingURL.csv")
data2 = pd.read_csv("phis.csv")
# print(data2.head())
# print(data1.shape)
# print(data2.shape)
final_data=pd.concat([data1,data2])
# print(final_data.head())
# print(final_data.shape)
# print(data1.info())
# print(final_data.info())
# print(data2.info())

