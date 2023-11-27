import boto3
from botocore.exceptions import NoCredentialsError, ClientError

# AWS credentials
aws_access_key = "AKIARRDRMAIAULU3EV64"
aws_secret_key = "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"
bucket_name = "trialsamplebucket"
old_folder = "firstfolder/"
new_folder = "secondfolder/"
file_name = "who.csv"

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)


def move_object(bucket, old_key, new_key):
    try:
        # Copy the object to the new location
        s3.copy_object(Bucket=bucket, CopySource={'Bucket': bucket, 'Key': old_key}, Key=new_key)

        # Delete the object from the old location
        s3.delete_object(Bucket=bucket, Key=old_key)

        print(f"Object '{old_key}' moved to '{new_key}' successfully.")
    except NoCredentialsError:
        print("Credentials not available.")
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchKey':
            print(f"Error: Object '{old_key}' does not exist in the specified location.")
        else:
            print(f"Error: {e}")


# Example usage
move_object(bucket_name, old_folder + file_name, new_folder + file_name)
