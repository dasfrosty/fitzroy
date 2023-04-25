# import boto3
import os
import requests

TEST_URL = os.environ["TEST_URL"]


def lambda_handler(event, context):
    requests.get(TEST_URL)


if __name__ == "__main__":
    lambda_handler(None, None)
