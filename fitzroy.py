# import boto3
import os
from botocore.vendored import requests

TEST_URL = os.environ["TEST_URL"]


def lambda_handler(event, context):
    requests.get(TEST_URL)
