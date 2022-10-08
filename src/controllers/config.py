class Config:
    """Configuration variables"""
    _currency_api_key = "29bf0c8397f4da77d274dd28c4e98868657dfdda"
    _currencies_list = ["USD", "EUR", "INR"]

    @property
    def currency_api_key(self) -> str:
        return self._currency_api_key

    @property
    def currency_list(self) -> list:
        return self._currencies_list


config = Config()  # Config class sigleton
