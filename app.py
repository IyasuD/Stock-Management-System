'''
Author:          Iyasu Geleta
Date Created:    08/21/2020
Functionality:
	         This program depending up on the user input either plots a pie chart that indicate the
           amount in percentahe an investor spent using pygal or the plots a line graph for a list
           of stocks stored in json file using matplotlib package.
             
             PartI: Plots a pie chart and generate a recipt in PDF format.
             PartII: Reads the json data and stores the data into stocks database.
             PartIII: Fetches the data from the data base and cast the date list in to
             a format matlibplot understands.
             PartIV:Plots the totalcost vs Time line graph
             
             For PartII
             Assumption: on each day a random  number of stock is purchased.[Reason to scale the graph 
             and difficulty to input stock number for a large set of data]
             Program Structure: data_managemnt module consists of functions to manipulate data
                              : plot_util consist functions that assist in ploting the graph

'''

#import statements sorted alphabetically
from data_management import *
from matplotlib.dates import DateFormatter, MonthLocator
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

from utils import *


def main():
    """Program execution starts from here"""

    # diplay name of the Program
    app_title()

    while True:
        #part I
        response = display_menu()
        if response == 1:
            #accept and greet investor
            investor_name = accept_name()

            #call the purchase stock function
            purchase_Stock(investor_name)
            
        elif response == 2:
            #part II[readjson file]
            print("Did you store your json file inside the data/pre_defined_stocks_data directory")
            response = input("Press y or n:\n")
            
            if response == 'y' or 'Y':
                #from data management module read ajsonfile 
                filepath = read_a_json_file()
                stocks_data = read_json(filepath=filepath)
               
               # Create table
                create_table()
               
               # For convienience convert stocks_data list in to stock_dict
                stock_dict = convert_to_dictonary(data=stocks_data)
               
               # Store the dictonary data into the stocks database
                store_data_to_db(stock_dict)                
   
                  
                #Part III[Fetch data from database]
                try:       
                    conn = sqlite3.connect("data/database/stocks.db")
                    df = pd.read_sql("SELECT SYMBOL,OPEN, HIGH, LOW, CLOSE, NUMBER_OF_SHARE, PURCHASE_DATE FROM STOCK", conn)
                    df["TOTAL_COST"] = df["CLOSE"] * df["NUMBER_OF_SHARE"]
                except Error as e:
                   print(f'main function  encountered {e} exception')
                else:
                    # part IV [Plot graph]
                    fig,ax = plt.subplots()
                    unique_symbols = set(df['SYMBOL'])
                    df['PURCHASE_DATE'] = pd.to_datetime(df['PURCHASE_DATE'])
                    for symbol in unique_symbols:
                        ax.plot(df[df.SYMBOL==symbol].PURCHASE_DATE,
                        df[df.SYMBOL==symbol].TOTAL_COST,
                        label=symbol)
                      
                    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m'))
                    ax.xaxis.set_major_locator(MonthLocator(interval=3))
                    ax.set_xlabel("Date")
                    #Assumption 
                    ax.set_ylabel("Total Cost")
                    ax.legend(loc='best')
                    plt.title("Stocks Data Visualization")
                    plt.savefig('outputs/simplePlot.png')
            else:
              exit()
            
        elif response == 0:
            print("Quiting...")
            exit()


if __name__ == "__main__":
    main()
    
    

   