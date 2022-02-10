from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession


def create_spark_session() -> SparkSession:
    spark = ( SparkSession.builder 
        .config('spark.jars.packages', 'org.apache.hadoop:hadoop-aws:3.1.2,net.snowflake:spark-snowflake_2.12:2.9.0-spark_3.1,net.snowflake:snowflake-jdbc:3.13.3')
        .config('fs.s3a.aws.credentials.provider', 'com.amazonaws.auth.DefaultAWSCredentialsProviderChain') 
        .config('fs.s3a.impl', 'org.apache.hadoop.fs.s3a.S3AFileSystem') 
        .getOrCreate()
        )

    return spark
# the credentials will be rendered from AWS using those functions above in config


df = create_spark_session().read.json('s3a://dataminded-academy-capstone-resources/raw/open_aq/data_part_1.json')

# df.write.json("../resources/weather.json")



#df.show()
df.printSchema()
#check out which are the columnames
flattened_df = df.select(["city","coordinates.latitude","coordinates.longitude","country","date.local","date.utc","entity","isAnalysis","isMobile","location","locationId","parameter","sensorType","unit","value"])
# df.show()
flattened_df.printSchema()
