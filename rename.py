import boto3

# AWS credentials
aws_access_key = "AKIARRDRMAIAULU3EV64"
aws_secret_key = "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"
bucket_name = "trialsamplebucket"
old_key = "bar.csv"
new_key = "car.csv"

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)


def rename_object(bucket, old_key, new_key):
    try:
        # Copy the object to the new key
        s3.copy_object(Bucket=bucket, CopySource={'Bucket': bucket, 'Key': old_key}, Key=new_key)

        # Delete the object from the old key
        s3.delete_object(Bucket=bucket, Key=old_key)

        print(f"Object '{old_key}' renamed to '{new_key}' successfully.")
    except Exception as e:
        print(f"Error: {e}")


# Example usage
rename_object(bucket_name, old_key, new_key)
