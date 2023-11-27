import boto3
from botocore.exceptions import NoCredentialsError

# AWS credentials
aws_access_key = "AKIARRDRMAIAULU3EV64"
aws_secret_key = "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"
bucket_name = "trialsamplebucket"
local_file_path = "C:\\Users\Vrdella\Downloads\hello.pdf"  # Path to the local file you want to upload
s3_file_key = "hello.pdf"  # Desired key for the file in S3

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)


def upload_file(local_path, bucket, s3_key):
    try:
        # Upload the file
        s3.upload_file(local_path, bucket, s3_key)
        print(f"File '{local_path}' uploaded to S3 bucket '{bucket}' with key '{s3_key}'.")
    except NoCredentialsError:
        print("Credentials not available.")


# Example usage
upload_file(local_file_path, bucket_name, s3_file_key)