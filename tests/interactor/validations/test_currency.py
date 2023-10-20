import pytest
from src.interactor.validations.currency_validation import (
    CreateCurrencyInputDtoValidator,
    ListCurrencyInputDtoValidator,
    UpdateCurrencyInputDtoValidator,
)


def test_list_currency_input_dto_validate() -> None:
    data = {"skip": 0, "limit": 100}
    input_dto = ListCurrencyInputDtoValidator(**data)

    assert input_dto.skip == data.get("skip")
    assert input_dto.limit == data.get("limit")


def test_create_currency_input_dto_validate() -> None:
    data = {
        "code": "USD",
        "name": "US Dollar",
        "symbol": "$",
    }
    input_dto = CreateCurrencyInputDtoValidator(**data)

    assert input_dto.code == data.get("code")
    assert input_dto.name == data.get("name")
    assert input_dto.symbol == data.get("symbol")


def test_update_currency_input_dto_validate() -> None:
    data = {
        "code": "USD",
        "name": "US Dollar",
    }
    input_dto = UpdateCurrencyInputDtoValidator(**data)

    assert input_dto.code == data.get("code")
    assert input_dto.name == data.get("name")
    assert input_dto.symbol is None


def test_invalid_list_currency_input_dto_validate() -> None:
    with pytest.raises(ValueError):
        ListCurrencyInputDtoValidator(skip="test", limit="test")


def test_invalid_create_currency_input_dto_validate():
    with pytest.raises(ValueError):
        CreateCurrencyInputDtoValidator(code="test", name=111)


def test_invalid_update_currency_input_dto_validate() -> None:
    with pytest.raises(ValueError):
        UpdateCurrencyInputDtoValidator(code="test", name=111)
