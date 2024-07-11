from mediatr import Mediator

from src.application.currency.commands.add_currency.add_currency_command_handler import (
    AddCurrencyCommandHandler,
)
from src.application.currency.commands.edit_currency.edit_currency_command_handler import (
    EditCurrencyCommandHandler,
)
from src.application.currency.commands.remove_currency.remove_currency_command_handler import (
    RemoveCurrencyCommandHandler,
)
from src.application.currency.queries.get_currencies_list.get_currencies_list_query_handler import (
    GetCurrenciesListQueryHandler,
)
from src.application.currency.queries.get_currency_detail.get_currency_detail_query_handler import (
    GetCurrencyDetailQueryHandler,
)


def my_class_handler_manager(handler_class, is_behavior=False):
    from src.presentation.rest_api.config.containers import container

    return container.resolve(handler_class)


mediator_registers = Mediator(handler_class_manager=my_class_handler_manager)

mediator_registers.register_handler(GetCurrenciesListQueryHandler)
mediator_registers.register_handler(GetCurrencyDetailQueryHandler)
mediator_registers.register_handler(AddCurrencyCommandHandler)
mediator_registers.register_handler(EditCurrencyCommandHandler)
mediator_registers.register_handler(RemoveCurrencyCommandHandler)
