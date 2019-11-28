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


#Write data to database
#First make sure the data is correctly transformed
#1st make sure the timestamp column is in datetime format
#2nd make sure the timestamp column is set as index
#Examples:

#Transform timestamp column into datetime format
data['timestamp'] = pd.to_datetime(data['timestamp'])

#Set timestamp as index
data = data.set_index('timestamp')

#Once the data is clean and properly aligned it can be sent to Influx DB
client.write_points(data, 'value X')
