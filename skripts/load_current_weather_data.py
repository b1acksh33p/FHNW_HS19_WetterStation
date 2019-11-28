#!/usr/bin/env python3

# import the library
from fhnw_ds_hs2019_weatherstation_api import data_import as weather
import os
import time


# DB and CSV config
config = weather.Config()
# define DB host
config.db_host='localhost'
# connect to DB
weather.connect_db(config)
while True:
    try:
        weather.import_latest_data(config)
        time.sleep(300)
    except:
        time.sleep(60)
      
