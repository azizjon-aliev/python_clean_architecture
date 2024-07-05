from mediatr import Mediator

from src.application.currency.queries.get_currencies_list_query_handler import (
    GetCurrenciesListQueryHandler,
)


def my_class_handler_manager(handler_class, is_behavior=False):
    from src.presentation.rest_api.config.containers import container

    return container.resolve(handler_class)


mediator_registers = Mediator(handler_class_manager=my_class_handler_manager)

mediator_registers.register_handler(GetCurrenciesListQueryHandler)
