'''This module consists of functions related to reading from a json file and
functions realted to creating and accessing the database'''
import random
import sqlite3
from datetime import datetime
from sqlite3.dbapi2 import Error
from stock import Stock
import os
import pandas as pd

def read_json(filepath):
    ''' read a json file and returns a list of elements of the
        json file'''
    try:
        df = pd.read_json(filepath) 
        unique_symbols = set(df['Symbol'])
    except Exception as e:
        print(f'read_json encountered {e} exception')
    else:
        for symbol in unique_symbols:
            df["no_share"] = random.randint(79,426)         
        
        return df
def convert_to_dictonary(data):
    '''convert a list of stock objects in to a dictonary of stocks with a 
       key of id and value of  stock objects'''

    stock_list = []
    for index, stock_row in data.iterrows():
       
        purchase_date = stock_row['Date'].strftime("%d-%b-%y")
        
        new_Stock = Stock(index+1, stock_row['Symbol'], purchase_date, stock_row['Open'],
                          stock_row['High'], stock_row['Low'], stock_row['Close'], stock_row['Volume'], stock_row['no_share'])
        stock_list.append(new_Stock)
        
    return stock_list
    
def create_table():
    '''creates stock table'''
    try:
        with sqlite3.connect("data/database/stocks.db") as conn:
            cursor = conn.cursor()
            conn.execute("DROP TABLE IF EXISTS STOCK")
            sql_create_stock = '''
                        CREATE TABLE STOCK(STOCK_ID INTEGER PRIMARY KEY,
                        SYMBOL VARCHAR(10), PURCHASE_DATE TEXT, OPEN REAL,
                        HIGH REAL, LOW REAL,
                        CLOSE REAL, VOLUME REAL, NUMBER_OF_SHARE INTEGER
                        )
            '''
          
            cursor.execute(sql_create_stock)
            conn.commit()
            print("Table created Successfully")
    except Exception as e:
        print(f'create_table  encountered {e} exception')

def store_data_to_db(data_stored_in_dic_format):
    '''store data into STOCK table inside stocks database'''
    
    for stock in data_stored_in_dic_format:
        
        try:
            with sqlite3.connect("data/database/stocks.db") as conn:
                 cursor = conn.cursor()
                 query_insert_stock = '''
                                         INSERT INTO STOCK(STOCK_ID, SYMBOL,
                                         PURCHASE_DATE , OPEN,
                                         HIGH, LOW ,
                                         CLOSE , VOLUME,NUMBER_OF_SHARE )
                                         VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
        
                              '''
    
                 cursor.execute(query_insert_stock,
                                (stock._stock_id,stock._symbol,
                                stock._date,stock._open_stock,
                                 stock._high, stock._low,
                                 stock._close, stock._volume, stock._share_no))
                 conn.commit()
                 
                 print("Data stored successfully")
        except Error as e:
            print(f'store_data_to_db  encountered {e} exception') 

def read_a_json_file():
    '''automatically reads a json file stored inside data/pre_defined_Stocks_data directory'''
    path_to_json = 'data/pre_defined_stocks_data/'
    try:
       json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
    except Exception as e:
        print("read_a_json encountered {e} exception")
    else:
        filePath = path_to_json +json_files[0]
        return filePath



   
    
    