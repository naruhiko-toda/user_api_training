class Tel:
    def __init__(self, value):
        self.__validate(value)
        self.value = value

    def __validate(self, value):
        if not value:
            return
        if value.count("-") != 2:
            raise ValueError("電話番号のフォーマットはxxx-xxxx-xxxxにしてください")
        if len(value.split('-')[1]) != 4 or len(value.split('-')[0]) != 3 or len(value.split('-')[2]) != 4:
            raise ValueError("電話番号のフォーマットはxxx-xxxx-xxxxにしてください")
