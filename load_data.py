#!/usr/bin/python3

import pandas
import csv

def process_pandas():
    df = pandas.read_csv('prices.csv')

    # DataFrame objects have lots of features.  For example, you can 
    # perform calculations on columns.
    # We can also perform calculcations on a single column
    Average = df['PRODUCT_PRICE'].mean()

    # We are returning the timedelta
    return Average

def process_csv():
    f = open('prices.csv', 'r')

    # We supply the file object into a reader to parse the csv file
    reader = csv.DictReader(f)

    # initialize some accumulator variables
    count = 0
    total = 0

    # The main loop
    for record in reader:
        # each item in reader is a row in the csv file converted to a python dictionary
        total += float(record['PRODUCT_PRICE'])
        count += 1

    # remember to close the file object
    f.close()
    if count == 0:
        print("division by zero")
    else:
        return total/count

def process_py():
    f = open('prices.csv', 'r')
    # read the header line (we do this to skip the header line)
    header = f.readline().rstrip().split(',')

    # to calculate average, we also need to keep 
    # track of the number of total lines
    num_rows = 0
    sum = 0

    # Applying the "accumulator pattern"
    for line in f:        
        # split is a simple way to read csv files
        fields = line.rstrip().split(',')

        sum += float(fields[-2])

        num_rows += 1
    # remember to close the file object
    f.close()
    # return the average
    return sum/num_rows

def process_csv_dict():
    f = open('prices.csv', 'r')
    reader = csv.DictReader(f)
    Product_Prices = {}
    Product_rows = {}
    for record in reader:
        if record["ITEM_CATEGORY_NAME"] in Product_Prices:
            Product_Prices[record["ITEM_CATEGORY_NAME"]] += float(record['PRODUCT_PRICE'])
            Product_rows[record["ITEM_CATEGORY_NAME"]] += 1
        else:
            Product_Prices[record["ITEM_CATEGORY_NAME"]] = float(record['PRODUCT_PRICE'])  # Initialize with the first price
            Product_rows[record["ITEM_CATEGORY_NAME"]] = 1

    Averages = {key: (Product_Prices[key] / Product_rows[key]) if Product_rows[key] != 0 else "Error: Division by zero" for key in Product_Prices}        

    return Averages

def process_pandas_groupby():
    df = pandas.read_csv('prices.csv')
    productprices_df = df[["ITEM_CATEGORY_NAME","PRODUCT_PRICE"]]
    df_average = productprices_df.groupby('ITEM_CATEGORY_NAME').mean()
    return df_average.head()

if __name__ == "__main__":
    print("Average price using pure python: ", end='')    
    print(process_py())
    print("Average price using csv module: ", end='')    
    print(process_csv())
    print("Average price using pandas module: ", end='')    
    print(process_pandas())
    print(process_csv_dict())
    print(process_pandas_groupby())