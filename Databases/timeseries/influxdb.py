import influxdb_client
from influxdb_client import InfluxDBClient, Point, WriteOptions
from datetime import datetime

# Initialize InfluxDB Client
client = InfluxDBClient(url="http://localhost:8086", token="T_-PcgG49sy5ybS_qHLboeSBWU8mRAWKrEaShRbLxj4QknlGQ9ckuZjg4uaViWWIlbNvVs8OiAbuqQegKPAjPw==", org="leornard")

# Function to write data to InfluxDB
def write_data(measurement, tags, fields, time, bucket):
    point = Point(measurement).tag(tags).field(fields).time(time)
    write_api = client.write_api(write_options=WriteOptions(batch_size=1000, flush_interval=10_000))
    write_api.write(bucket=bucket, org="your-org", record=point)

# Example: Writing historical stock data
historical_stock_tags = {"symbol": "AAPL"}
historical_stock_fields = {"open": 150.0, "close": 155.0, "volume": 1000000}
write_data("stocks", historical_stock_tags, historical_stock_fields, datetime.utcnow(), "historical_data")

# Example: Writing live FX data
live_fx_tags = {"pair": "EURUSD"}
live_fx_fields = {"bid": 1.18, "ask": 1.181}
write_data("fx", live_fx_tags, live_fx_fields, datetime.utcnow(), "live_data")

# Close client
client.close()

#example from influxdb_client documentation
""" 
bucket="<BUCKET>"

write_api = client.write_api(write_options=SYNCHRONOUS)
   
for value in range(5):
  point = (
    Point("measurement1")
    .tag("tagname1", "tagvalue1")
    .field("field1", value)
  )
  write_api.write(bucket=bucket, org="leornard", record=point)
  time.sleep(1) # separate points by 1 second
"""