import boto3

s3 = boto3.client("s3")

s3.upload_file(
    "output/final_sales.csv",
    "rakesh-sales-processed",
    "transformed/final_sales.csv"
)

print("Processed file uploaded")