from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("DemoSpark").getOrCreate()
print(spark)