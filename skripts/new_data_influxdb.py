import pandas as pd
from influxdb import InfluxDBClient
from influxdb import DateFrameClient



host = 'localhost'
port = 8086
username = 'root'
password = 'root'
database = 'demo'

# This part will be used when planning to work with pandas dataframes

# Pandas: Instantinate connection to Database 
client = DateFrameClient(host = host,
                         port = port,
                         username = username,
                         password = password 
                         database = database)

json_body

# Create new database
client.create_database('demo')

#JSON: Instantinate connection to Database
client = InfluxDBClient (host = host,
                         port = port,
                         username = username,
                         password = password 
                         database = database)


#create a new database
client.create('database')


