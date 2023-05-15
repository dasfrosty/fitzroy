# import boto3
import os
import requests

# TODO: make this an env var
LINK_URL = "https://www.patagonia.com/product/mens-nano-puff-fitz-roy-trout-hoody/195699027954.html"


def check_price(product_url: str, expected_price: float):
    result = requests.get(product_url).json()
    color_price = result["product"]["colorPrice"]
    price = None

    # check if any colors do not match the expected price
    for color, item in color_price.items():
        price = float(item.get("price", {}).get("sales", {}).get("value"))
        if price != expected_price:
            return f"[FITZROY] Unexpected price for {color}! Expected ${expected_price} got ${price}. See online at {LINK_URL}"

    if price is None:
        return (
            f"[FITZROY] Could not determine price for item! Check online at {LINK_URL}"
        )

    # run extra check just in case
    for color, item in color_price.items():
        if item.get("price", {}).get("list") != None:
            return f"[FITZROY] Color {color} may be on sale. Check online at {LINK_URL}"


def send_message(message: str):
    # TODO
    print(message)


# entry point for lambda
def handle_event(event, context):
    product_url = os.environ["PRODUCT_URL"]
    expected_price = float(os.environ["EXPECTED_PRICE"])

    try:
        if message := check_price(product_url, expected_price):
            send_message(message)
    except Exception as e:
        send_message(f"Failed! {e}")
        raise


# entry point for testing locally
def main():
    product_url = "https://www.patagonia.com/on/demandware.store/Sites-patagonia-us-Site/en_US/Product-VariationAttributes?version=2&pid=195699137363&storeID=null"
    expected_price = float("369")

    if message := check_price(product_url, expected_price):
        send_message(message)
    else:
        print("Nothing to report")


if __name__ == "__main__":
    main()
