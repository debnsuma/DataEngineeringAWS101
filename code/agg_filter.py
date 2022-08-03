from pyspark.sql import SparkSession
from pyspark.sql import functions as F

S3_INPUT_DATA = 's3://codementor-mydemo-bucket-2/input/wikiticker.json'
S3_OUTPUT_DATA_AGG = 's3://codementor-mydemo-bucket-2/output/aggregate'
S3_OUTPUT_DATA_FILTER = 's3://codementor-mydemo-bucket-2/output/filtered'


def main():

    spark = SparkSession.builder.appName("My Demo ETL App").getOrCreate()
    spark.sparkContext.setLogLevel('ERROR')

    # Spark Dataframe (Raw)- Transformation 
    df = spark.read.json(S3_INPUT_DATA)
    print(f"Total no. of records in the source data set is : {df.count()}")

    aggregated_df = df.groupBy(df.channel).count()
    filtered_df = df.filter((df.isRobot == False) & (df.countryName == 'United States'))
    print(f"The total no. of records in this aggregated data set is {aggregated_df.count()}")
    print(f"The total no. of records in this filtered data set is {filtered_df.count()}")

    
    print("######### Aggregated Dataframe Summary ##########")
    aggregated_df.show(5)
    aggregated_df.printSchema()
    print("######### Filtered Dataframe Summary ##########")
    filtered_df.show(5)
    filtered_df.printSchema()

    try:
        aggregated_df.write.mode('overwrite').parquet(S3_OUTPUT_DATA_AGG)
        print('The aggregated data is uploaded')
        filtered_df.write.mode('overwrite').parquet(S3_OUTPUT_DATA_FILTER)
        print('The filtered data is uploaded')        
    except:
        print('Something went wrong, please check the logs :P')
    
if __name__ == '__main__':
    main()