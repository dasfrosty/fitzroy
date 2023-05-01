# import boto3
import os
import requests

FITZROY_URL = "https://www.patagonia.com/on/demandware.store/Sites-patagonia-us-Site/en_US/Product-VariationAttributes?version=2&pid=195699027954&storeID=null"
EXAMPLE_URL = "https://www.patagonia.com/on/demandware.store/Sites-patagonia-us-Site/en_US/Product-VariationAttributes?version=2&pid=195699137363&storeID=null"

LINK_URL = "https://www.patagonia.com/product/mens-nano-puff-fitz-roy-trout-hoody/195699027954.html"

EXPECTED_PRICE = 369


def check_price(url, expected_price):
    result = requests.get(url).json()
    color_price = result["product"]["colorPrice"]

    for color, item in color_price.items():
        price = item.get("price", {}).get("sales", {}).get("value")
        if price != expected_price:
            return f"[FITZROY] Unexpected price for {color}! Expected ${expected_price} got ${price}. See online at {LINK_URL}"

    # run extra check just in case
    for color, item in color_price.items():
        if item.get("price", {}).get("list") != None:
            return f"[FITZROY] Color {color} may be on sale. Check online at {LINK_URL}"


def send_message(message):
    # TODO
    print(message)


# entry point for lambda
def handle_event(event, context):
    # TODO: remove
    requests.get(os.environ["TEST_URL"])

    try:
        if message := check_price(FITZROY_URL, EXPECTED_PRICE):
            send_message(message)
    except:
        # TODO
        print("Failed!")
        raise


# entry point for testing locally
def main():
    if message := check_price(EXAMPLE_URL, EXPECTED_PRICE):
        print(message)
    else:
        print("Nothing to report")


if __name__ == "__main__":
    main()
