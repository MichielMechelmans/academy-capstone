gifrom pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from secretsmanager import get_secrets
import json

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


def write_to_snowflake(df):
    credentials = get_secrets()
    secret_string = credentials['SecretString']

    secrets = json.loads(secret_string)

    SNOWFLAKE_SOURCE_NAME = "net.snowflake.spark.snowflake"

    sfOptions   = {
        "sfURL" : secrets["URL"] + ".snowflakecomputing.com",
        "sfUser" : secrets["USER_NAME"],
        "sfDatabase" : secrets["DATABASE"],
        "sfPassword": secrets["PASSWORD"],
        "sfRole": secrets["ROLE"],
        "sfSchema" : "MICHIEL",
        "sfWarehouse" : secrets["WAREHOUSE"]
    }
    (df.write
        .format(SNOWFLAKE_SOURCE_NAME)
        .options(**sfOptions)
        .option("dbtable","MICHIEL")
        .mode("overwrite")
        .save()
    )


#df.show()
df.printSchema()
#check out which are the columnames
flattened_df = df.select(["city","coordinates.latitude","coordinates.longitude","country","date.local","date.utc","entity","isAnalysis","isMobile","location","locationId","parameter","sensorType","unit","value"])
# df.show()
flattened_df.printSchema()
write_to_snowflake(flattened_df)


def write_to_snowflake(df):
    credentials = get_secrets()
    secret_string = credentials['SecretString']

    secrets = json.loads(secret_string)

    SNOWFLAKE_SOURCE_NAME = "net.snowflake.spark.snowflake"

    sfOptions   = {
        "sfURL" : secrets["URL"] + ".snowflakecomputing.com",
        "sfUser" : secrets["USER_NAME"],
        "sfAuthenticator" : secrets["oauth"],
        "sfDatabase" : secrets["DATABASE"],
        "sfSchema" : "MICHIEL",
        "sfWarehouse" : secrets["WAREHOUSE"]
    }
    (df.write
        .format(SNOWFLAKE_SOURCE_NAME)
        .options(**sfOptions)
        .option("dbtable","MICHIEL")
        .mode("overwrite")
        .save()
    )
