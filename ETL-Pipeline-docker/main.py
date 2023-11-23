import os
from datetime import datetime
from scr.extract import extract_transaction_data
from scr.transform import identify_remove_duplicates
from scr.load_data_to_s3 import df_to_s3
from dotenv import load_dotenv
load_dotenv() # only for local testing

dbname = os.getenv("dbname")
host = os.getenv("host")
port = os.getenv("port")
user = os.getenv("user")
password = os.getenv("password")
aws_access_key_id = os.getenv("aws_access_key_id")
aws_secret_access_key = os.getenv("aws_secret_access_key")

start_time = datetime.now()

# connect to redshift and extract online transactions data with transformation tasks
print('\nExtract and Transform the data...')
online_trans_cleaned = extract_transaction_data(dbname, host, port, user, password)
print('\nExtraction and transformation in sql completed')

# remove duplicated data
print('\nDeduplicate the data...')
online_trans_duplicated = identify_remove_duplicates(online_trans_cleaned)
print('\nDuplicated data removed')

# load the cleaned data to s3
print('\nLoad the data to s3...')
s3_bucket = "waia-data-dump"
key = "bootcamp2/etl/na_online_trans_cleaned.csv"
df_to_s3(online_trans_duplicated, key, s3_bucket, aws_access_key_id, aws_secret_access_key)

execution_time = datetime.now()-start_time
print(f"\nTotal execution time (hh:mm:ss.ms) {execution_time}")
