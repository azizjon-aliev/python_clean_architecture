from src.domain.entities.currency import Currency

data = {"currency_id": 1, "code": "USD", "name": "US Dollar", "symbol": "$"}


def test_currency_creation():
    currency: Currency = Currency(**data)

    assert currency.currency_id == data.get("currency_id")
    assert currency.code == data.get("code")
    assert currency.name == data.get("name")
    assert currency.symbol == data.get("symbol")


def test_currency_from_dict():
    currency: Currency = Currency.from_dict(data=data)

    assert currency.currency_id == data.get("currency_id")
    assert currency.code == data.get("code")
    assert currency.name == data.get("name")
    assert currency.symbol == data.get("symbol")


def test_currency_to_dict():
    currency: Currency = Currency.from_dict(data=data)
    assert currency.to_dict() == data


def test_currency_equality():
    currency1: Currency = Currency.from_dict(data=data)
    currency2: Currency = Currency.from_dict(data=data)
    assert currency1 == currency2
