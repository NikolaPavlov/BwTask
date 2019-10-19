import re


PRICE_REGEX = '(\d+\.\d{1,2})'


def format_price(price_str):
    try:
        extracted_price = re.findall(PRICE_REGEX, price_str)[0]
        return float(extracted_price)
    except:
        return None
