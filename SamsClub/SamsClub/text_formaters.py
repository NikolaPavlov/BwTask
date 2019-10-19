import re


NOT_AVAILABLE_MSG = 'not available'
PRICE_REGEX = '(\d+\.\d{1,2})'


def format_price(price_str):
    if price_str:
        extracted_price = re.findall(PRICE_REGEX, price_str)[0]
        return float(extracted_price)
    else:
        return NOT_AVAILABLE_MSG

def format_id(id_str):
    if id_str:
        return int(id_str)
    else:
        return NOT_AVAILABLE_MSG
