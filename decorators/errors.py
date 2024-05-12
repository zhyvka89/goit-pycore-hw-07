def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return e
        except IndexError:
            return "Enter user name."
        except KeyError as e:
            return e
        except AttributeError as e:
            return e
        except TypeError as e:
            return e

    return inner