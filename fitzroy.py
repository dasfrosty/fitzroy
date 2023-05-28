import boto3
import os
import requests


sns = boto3.resource("sns")


def _check_price(product_url: str, link_url: str, expected_price: float):
    result = requests.get(product_url).json()
    color_price = result["product"]["colorPrice"]
    price = None

    # check if any colors do not match the expected price
    for color, item in color_price.items():
        price = float(item.get("price", {}).get("sales", {}).get("value"))
        if price != expected_price:
            return f"[FITZROY] Unexpected price for {color}! Expected ${expected_price} got ${price}. See online at {link_url}"

    if price is None:
        return (
            f"[FITZROY] Could not determine price for item! Check online at {link_url}"
        )

    # run extra check just in case
    for color, item in color_price.items():
        if item.get("price", {}).get("list") != None:
            return f"[FITZROY] Color {color} may be on sale. Check online at {link_url}"


def _send_message(message: str, sns_topic_arn: str):
    print(message)

    topic = sns.Topic(sns_topic_arn)
    response = topic.publish(Message=message)
    print(response)


# entry point for lambda
def handle_event(event, context):
    product_url = os.environ["PRODUCT_URL"]
    link_url = os.environ["LINK_URL"]
    expected_price = float(os.environ["EXPECTED_PRICE"])
    sns_topic_arn = os.environ["SNS_TOPIC_ARN"]

    try:
        if message := _check_price(product_url, link_url, expected_price):
            _send_message(message, sns_topic_arn)
    except Exception as e:
        _send_message(f"Failed! {e}", sns_topic_arn)
        raise
