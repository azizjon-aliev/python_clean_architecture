from src.interactor.interfaces.presenters.base_presenter import AbstractPresenterInterface
from src.interactor.dtos.authentication_dtos import TokenDto


class LoginPresenterInterface(AbstractPresenterInterface[TokenDto]):
    pass
