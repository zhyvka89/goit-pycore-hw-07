from datetime import datetime
from classes.Field import Field


class Birthday(Field):
    def __init__(self, value):
        try:
            bday_date = datetime.strptime(value, "%d.%m.%Y")
            super().__init__(bday_date)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")