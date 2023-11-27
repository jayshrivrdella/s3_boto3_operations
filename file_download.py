import boto3
from botocore.exceptions import NoCredentialsError

# AWS credentials
aws_access_key = "AKIARRDRMAIAULU3EV64"
aws_secret_key = "YBpE9whSi8Yx09/P9fcr53GEa5+v4EwAFeOW2kWO"
bucket_name = "trialsamplebucket"
s3_file_key = "your_s3_folder/file.txt"  # Key of the file in S3
local_download_path = "C:\\Users\Vrdella\Downloads\hello.pdf"  # Desired path for the downloaded file

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)


def download_file(bucket, s3_key, local_path):
    try:
        # Download the file
        s3.download_file(bucket, s3_key, local_path)
        print(f"File '{s3_key}' downloaded from S3 bucket '{bucket}' to '{local_path}'.")
    except NoCredentialsError:
        print("Credentials not available.")


# Example usage
download_file(bucket_name, s3_file_key, local_download_path)
