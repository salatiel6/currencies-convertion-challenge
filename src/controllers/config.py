class Config:
    """Configuration variables"""
    _currency_api_key = "29bf0c8397f4da77d274dd28c4e98868657dfdda"
    _currencies = ("USD", "EUR", "INR")

    @property
    def currency_api_key(self) -> str:
        return self._currency_api_key

    @property
    def currencies(self) -> tuple:
        return self._currencies


config = Config()  # Config class sigleton
