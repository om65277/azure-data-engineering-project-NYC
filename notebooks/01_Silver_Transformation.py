from pyspark.sql.functions import *

# Silver Layer
silver = "abfss://silver@taxidatalakeom.dfs.core.windows.net"

# Read source data from Silver
df_trip = spark.read.parquet(
    f"{silver}/trips2023data/*.parquet"
)

# Display data
display(df_trip)

# Check record count
print("Total Records:", df_trip.count())
