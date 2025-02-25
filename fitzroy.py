import os

import boto3
import requests

sns = boto3.resource("sns")

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"

def _check_price(
    product_url: str,
    link_url: str,
    desired_color: str,
    expected_price: float,
):
    response = requests.get(product_url, headers={"User-Agent": USER_AGENT})
    result = response.json()
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

    # check desired color still available
    if desired_color not in color_price:
        return f"[FITZROY] Desired color {desired_color} not available. Check online at {link_url}"

    print(f"Price found matches expected: price = ${price}")


def _send_message(message: str, sns_topic_arn: str):
    print(f"Sending message: {message}")
    topic = sns.Topic(sns_topic_arn)
    response = topic.publish(Message=message)
    print(f"SNS message published to topic: response = {response}")


# entry point for lambda
def handle_event(event, context):
    product_url = os.environ["PRODUCT_URL"]
    link_url = os.environ["LINK_URL"]
    desired_color = os.environ["DESIRED_COLOR"]
    expected_price = float(os.environ["EXPECTED_PRICE"])
    sns_topic_arn = os.environ["SNS_TOPIC_ARN"]

    try:
        if message := _check_price(
            product_url=product_url,
            link_url=link_url,
            desired_color=desired_color,
            expected_price=expected_price,
        ):
            _send_message(message, sns_topic_arn)
    except Exception as e:
        _send_message(f"Failed! {e}", sns_topic_arn)
        raise
