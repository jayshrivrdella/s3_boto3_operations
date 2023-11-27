import boto3
from botocore.exceptions import NoCredentialsError

# AWS credentials
aws_access_key = "AKIARRDRMAIAULU3EV64"
aws_secret_key = "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"
bucket_name = "trialsamplebucket"
folder_name = "firstfolder"

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)


def create_folder(bucket, folder):
    try:
        # Upload an empty object with the folder name as the key
        s3.put_object(Bucket=bucket, Key=folder)
        print(f"Folder '{folder}' created successfully.")
    except NoCredentialsError:
        print("Credentials not available.")


# Example usage
create_folder(bucket_name, folder_name)