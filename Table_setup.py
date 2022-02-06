import pandas as pd

#reading the csv files into the program

vending_machine = pd.read_csv('vending_machine.csv')
stock = pd.read_csv('stock.csv')

#creating a set of all the snacks
snack_set = set()
for i in vending_machine.index:
    snack_set.add(vending_machine['snack'][i])

#converting set to list to make it iterable
snack_list = list(snack_set)

#replacing the snack on the stock dataframe to match that of the vending_machine dataframe
for i in stock.index:
    j = stock['snack'][i].split()
    first_test = j[-1].capitalize()
    second_test = j[-2].capitalize()+' '+ j[-1].capitalize()
    if second_test in snack_set:
        stock.loc[i, "snack"]= second_test
    elif first_test in snack_set:
        stock.loc[i,'snack']= first_test

#merging the vending maching and stock dataframes
df = pd.merge(vending_machine,stock,on="snack", how='outer')

#making the machine code column the new index
df.set_index('machine_code', inplace=True)

#adding the missing data into the dataframe
df.loc[['B4']] = ('Iru-bru', 3.0, 'drinks', 3.00)

#print(df)
