import os

from fitzroy import handle_event


# os.environ["PRODUCT_URL"] = "https://www.example.com/product/sweater/size/md"
# os.environ["LINK_URL"] = "https://bit.ly/123456"
# os.environ["DESIRED_COLOR"] = "GREEN"
# os.environ["EXPECTED_PRICE"] = "79.99"
# os.environ["SNS_TOPIC_ARN"] = "arn:aws:sns:us-west-2:123456789:fitzroy-notifications-topic"


def main():
    handle_event(None, None)


if __name__ == "__main__":
    main()
