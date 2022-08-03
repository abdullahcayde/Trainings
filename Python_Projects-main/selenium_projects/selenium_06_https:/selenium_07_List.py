import pandas as pd
import os

headers_list = ['Honda Jazz Automatik Tüv 03/24', 'Honda jazz.1.4 Automatik neun TÜV', 'Auto Honda', 'Honda Jazz 1,2 Trend Advantage mit Klimaautomatik, Start/Stopp', 'Honda jazz 1.4', 'Honda Jazz 1.4 LS', 'Honda Jazz 1.4 LS', 'Honda Jazz 1,4 ES Sport, aus Rentnerhand, TÜV 08/24', 'Honda jazz hybrid Automatik', 'Honda Jazz 1.4 Automatik Scheckheftgepflegt bei Honda']
price_list = ['3.800 €', '3.800 €', '4.600 €', '6.900 €', '4.500 € VB', '4.500 €', '2.300 €', '4.990 €', '6.500 €', '3.699 €']
print(len(headers_list),len(price_list))

# ------------------------ 1 - Two list to Dataframe -------------------
# 1.1 Two list to Dataframe with Dictionary
d = {'Title':headers_list, 'Price':price_list}
df = pd.DataFrame(d)
print(df)
print(80*'*')



# 1.2 Two list to Dataframe with Zip Method
data_tuples = list(zip(headers_list, price_list))
df = pd.DataFrame(data_tuples, columns = ["Title2", "Price2"])
print(df)


# ------------------------ 2 - Save DataFrame to csv to folder -------------------
df.to_csv('NAME.csv')