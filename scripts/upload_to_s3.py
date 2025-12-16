import boto3
import os
import yaml
from pathlib import Path

def load_config():
    with open('../config/config.yaml', 'r') as f:
        return yaml.safe_load(f)

def upload_data_to_s3():
    config = load_config()
    s3 = boto3.client('s3', region_name=config['aws']['region'])
    bucket = config['aws']['s3_bucket']
    prefix = config['aws']['s3_prefix']
    
    data_dir = Path('../data')
    
    for file in data_dir.glob('*.csv'):
        key = f"{prefix}{file.name}"
        print(f"Uploading {file.name} to s3://{bucket}/{key}")
        s3.upload_file(str(file), bucket, key)
        print(f"✓ Uploaded {file.name}")

if __name__ == '__main__':
    upload_data_to_s3()
