from __future__ import print_function
import os
import sys
from time import strftime, sleep
import boto3
from botocore.exceptions import ClientError

VERSION_LABEL = strftime("%Y-%m-%d,%H-%M-%S")
BUCKET_KEY = os.getenv('APPLICATION_NAME') + '/' + VERSION_LABEL +'-yesteacherpython.zip'

def upload_to_s3(yesteacher):
    """
    
    """
    try:
        client = boto3.client('s3')
    except ClientError as err:
        print("Failed to create boto3 client.\n" + str(err))
        return False

    try:
        print('Uploading to S3.........\n')
        client.put_object(
            Body=open(yesteacher, 'rb'),
            Bucket=os.getenv('S3_BUCKET'),
            Key=BUCKET_KEY
        )
        print('Successfully uploaded to S3.........\n')
    except ClientError as err:
        print("Failed to upload yesteacher to S3.\n" + str(err))
        return False
    except IOError as err:
        print("Failed to access yesteacher.zip in this directory.\n" + str(err))
        return False

    return True

def create_new_version():
    """
    Creates a new application version in AWS Elastic Beanstalk
    """
    try:
        client = boto3.client('elasticbeanstalk')
    except ClientError as err:
        print("Failed to create boto3 client.\n" + str(err))
        return False

    try:
        print('Creating new version.........\n')
        print("Enter New Version Description..............\n")
        description=input()
        response = client.create_application_version(
            ApplicationName=os.getenv('APPLICATION_NAME'),
            VersionLabel=VERSION_LABEL,
            Description=description,
            SourceBundle={
                'S3Bucket': os.getenv('S3_BUCKET'),
                'S3Key': BUCKET_KEY
            },
            Process=True
        )
        print('version created.............\n')
    except ClientError as err:
        print("Failed to create application version.\n" + str(err))
        return False

    try:
        if response['ResponseMetadata']['HTTPStatusCode'] is 200:
            return True
        else:
            print(response)
            return False
    except (KeyError, TypeError) as err:
        print(str(err))
        return False

def deploy_new_version():
    """
    Deploy a new version to AWS Elastic Beanstalk
    """
    try:
        client = boto3.client('elasticbeanstalk')
    except ClientError as err:
        print("Failed to create boto3 client.\n" + str(err))
        return False

    try:
        print('Updating new environment with new version......................\n')
        response = client.update_environment(
            ApplicationName=os.getenv('APPLICATION_NAME'),
            EnvironmentName=os.getenv('APPLICATION_ENVIRONMENT'),
            VersionLabel=VERSION_LABEL,
        )
    except ClientError as err:
        print("Failed to update environment.\n" + str(err))
        return False

    print(response)
    return True

def main():
    " For Deployment"
    if not upload_to_s3('./yesteacher.zip'):
        sys.exit(1)
    if not create_new_version():
        sys.exit(1)
    # Wait for the new version to be consistent before deploying
    sleep(5)
    if not deploy_new_version():
        sys.exit(1)

if __name__ == "__main__":

    main()





"""
PATH='/home/shivamguys/Desktop/yesteacher/dist'
import os
from glob import glob
result = [y for x in os.walk(PATH) for y in glob(os.path.join(x[0], '*'))]

"""


