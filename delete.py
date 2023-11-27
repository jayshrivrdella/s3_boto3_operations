import boto3
from botocore.exceptions import NoCredentialsError

# AWS credentials
aws_access_key = "AKIARRDRMAIAULU3EV64"
aws_secret_key = "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"
bucket_name = "trialsamplebucket"
file_key = "car.csv"

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)


def delete_file(bucket, key):
    try:
        # Delete the object from the specified key
        s3.delete_object(Bucket=bucket, Key=key)

        print(f"File '{key}' deleted successfully.")
    except NoCredentialsError:
        print("Credentials not available.")


# Example usage
delete_file(bucket_name, file_key)
