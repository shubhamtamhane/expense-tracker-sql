"""
The purpose of this file is to hold various sql queries to be used in utilities functions
"""

import sqlite3 as sql3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class DBQueries:

    def __init__(self):
        self.conn = sql3.connect('expense_tracker.db')
        self.cursor = self.conn.cursor()

    def get_data(self, file):
        data = pd.read_csv(file)
        attributes = ['hrk','vendor', 'date', 'description','meansofpayment','city', 'category', 'currency','country']
        new_data = data[attributes]
        new_data.rename(columns={'hrk': 'cost'}, inplace=True)
        return new_data
    
    def run(self):
        file = 'expences1.csv'
        data = self.get_data(file)
        data.to_sql('expense', self.conn, index=False, if_exists='replace')

    def create_table(self):
        with sql3.connect('expense_tracker.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS users 
                           (email varchar(40),
                           password varchar(40), 
                           firstname varchar(40), 
                           lastname varchar(40));""")
            
    def add_items(self):
        with sql3.connect('expense_tracker.db') as conn:
            cursor = conn.cursor()
            
            cursor.execute("""CREATE TABLE items_list(
                               Id INTEGER PRIMARY KEY NOT NULL,
                               date DATE NOT NULL,
                               amount DECIMAL(10, 2),
                               details VARCHAR(255),
                               email varchar(40));
                           """)
            
            conn.commit()

    def drop_table(self):
        with sql3.connect('expense_tracker.db') as conn:
            cursor = conn.cursor()
            cursor.execute("drop table items_list")
            conn.commit()

if __name__ == '__main__':
    data_obj = DBQueries()
    data_obj.add_items()

