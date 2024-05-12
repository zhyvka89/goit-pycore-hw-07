from classes.Field import Field


class Phone(Field):
    def __init__(self, phone_number):
        super().__init__(self.validate(phone_number))

    def validate(self, phone_number):
        if len(phone_number) != 10:
            raise ValueError('Phone number should be 10 digits long.')
        return phone_number