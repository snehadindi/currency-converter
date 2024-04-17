CURRENCIES = {
    'USD': 1,
    'EUR': 1.06,
    'YEN': 0.0067,
    'GBP': 1.23,
    'AUD': 0.64,
    'CAD': 0.74
}

class CurrencyNotSupportedError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

def to_usd(currency, amount):
    if currency not in CURRENCIES:
         raise CurrencyNotSupportedError(f"{currency} is not supported")
    elif amount < 0:
        raise InvalidAmountError("Invalid amount")
    else:
        return amount * CURRENCIES[currency]

def from_usd(currency, amount_usd):
    if currency not in CURRENCIES:
        raise CurrencyNotSupportedError(f"{currency} is not supported")
    elif amount_usd < 0:
        raise InvalidAmountError("Invalid amount")
    else:
        converted_amount = amount_usd / CURRENCIES[currency]
        return round(converted_amount, 4)
