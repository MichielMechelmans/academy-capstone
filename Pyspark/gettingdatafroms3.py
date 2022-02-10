from pyspark import SparkContext
from pyspark.sql import SparkSession


spark = SparkSession.builder.getOrCreate()

spark = (
            Sparksession
            .builder
            .appName("WETL")
            .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.1.2,net.snowflake:spark-snowflake_2.12:2.9.0-spark_3.1,net.snowflake:snowflake-jdbc:3.13.3")
)
df = spark.read.json("s3://dataminded-academy-capstone-resources/raw/open_aq/*.json")

df.show()