import pandas as pd
from influxdb import InfluxDBClient
from influxdb import DataFrameClient


host = 'localhost'
port = 8086
username = 'root'
password = 'root'
database = 'demo'

#Instantinate client and establish connection to Database 
client = DataFrameClient(host = host,
                         port = port,
                         username = username,
                         password = password, 
                         database = database)

#Load Data you want into pandas dataframe
data = pd.read_csv("name_of_file.csv")

#Create new database. Replace 'demo' with any name you want for the database
client.create_database('demo')

#Delete database. Replace 'demo' with any name you want for the database
client.drop_database('demo')




