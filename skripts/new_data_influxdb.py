from influxdb import InfluxDBClient

database = db

# using Http
client = InfluxDBClient(database=database)
