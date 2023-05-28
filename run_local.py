import os

from fitzroy import handle_event


PRODUCT_URL = "https://www.patagonia.com/on/demandware.store/Sites-patagonia-us-Site/en_US/Product-VariationAttributes?version=2&pid=195699137363&storeID=null"
LINK_URL = "https://www.patagonia.com/product/mens-nano-puff-fitz-roy-trout-hoody/195699027954.html"
EXPECTED_PRICE = "369"
SNS_TOPIC_ARN = "arn:aws:sns:us-west-2:352038380407:fitzroy-notifications-topic"


def main():
    os.environ["PRODUCT_URL"] = PRODUCT_URL
    os.environ["LINK_URL"] = LINK_URL
    os.environ["EXPECTED_PRICE"] = EXPECTED_PRICE
    os.environ["SNS_TOPIC_ARN"] = SNS_TOPIC_ARN

    handle_event(None, None)


if __name__ == "__main__":
    main()
