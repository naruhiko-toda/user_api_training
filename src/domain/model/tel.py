import re

class Tel:
    def __init__(self, value):
        self.__validate(value)
        self.value = value

    def __validate(self, value):
        if not value:
            return
        if not re.match(r"\d{3}-\d{4}-\d{4}$", value):
            raise ValueError("電話番号のフォーマットはxxx-xxxx-xxxxにしてください")
