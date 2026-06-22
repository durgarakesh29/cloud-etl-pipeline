import boto3

s3 = boto3.client("s3")

s3.upload_file(
    "data/sales.csv",
    "rakesh-sales-raw",
    "sales/sales.csv"
)

print("Upload Successful")