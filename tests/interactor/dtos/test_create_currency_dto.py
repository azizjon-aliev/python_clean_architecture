from src.interactor.dtos.currency_dtos import CreateCurrencyInputDto


def test_create_currency_input_dto():
    data = {"code": "USD", "name": "US Dollar", "symbol": "$"}

    input_dto = CreateCurrencyInputDto(**data)

    assert input_dto.code == data.get("code")
    assert input_dto.name == data.get("name")
    assert input_dto.symbol == data.get("symbol")
