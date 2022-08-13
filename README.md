# Data Con LA 2022

## Building a serverless data processing pipeline with PySpark on AWS

Data is all over the place, and what matters is how we manage that data and make sense out of it and take some meaningful data driven decision. In this session we will discuss about whole data engineering pipeline, starting from data collection, processing, analysis and visualization in a complete serverless fashion. We will pick some opensource dataset and shall store and process it on cloud(AWS). While the focus would be more on the general understanding of data pipeline aspects of data engineering, but during the process we will learn few of the AWS services which can help us to achieve our goal in an effective and efficient way.

## Implementation Steps for Data Processing 

1. Create an S3 Bucket `dataconla2022` 

2. Create few folders :
    a) `input`
    b) `code`
    c) `output`

2. Place the dataset in the S3 bucket under the `input` folder` 
    - `aws s3 cp dataset/wikiticker.json s3://dataconla2022-1/input/` 

3. Create an EMR cluster using the [steps mentioned here](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-setting-up.html)    

4. SSH to the EMR Cluster created in the previous step 

5. Copy the pySpark [code](code/agg_filter.py) inside the EMR cluster 

6. Submit the pySpark job 

    `sudo spark-submit agg_filter.py`


## Steps for Data Cataloging and Analysis

1. Create a Glue Crawler from the [Glue console](https://us-east-1.console.aws.amazon.com/glue/home?region=us-east-1#addCrawler:)

    - Create a database or use any of the existing database 
    - When asked for the data source, use the following path :
      `s3://dataconla2022/output`
    - Run the crawler 

2. Once the crawler run gets completed, open [Amazon Athena](https://us-east-1.console.aws.amazon.com/athena/home?region=us-east-1#/query-editor/) and query the database 

    - `SELECT * FROM "AwsDataCatalog"."<your DB Name>"."aggregate" 
        LIMIT 10;`


## Implementation Steps for Data Processing (using Amazon EMR Serverless) 

1. Create an IAM role using the [steps](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/getting-started.html) mentioned here

2.  Open `Amazon EMR Serverless` [console](https://us-east-1.console.aws.amazon.com/emr/home?region=us-east-1#/serverless)

2. Create an Application and use the IAM role created in `Step 1` 

3. Copy the code to the S3 bucket
`aws s3 cp agg_filter.py s3://dataconla2022-1/code/` 

3. Submit a job and mentioned the script location as `s3://dataconla2022-1/code/agg_filter.py`

