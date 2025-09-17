# random decorators and helper functions
def decorate_all_methods(decorator):
    def decorate(cls):
        for attr_name, attr_value in cls.__dict__.items():
            if callable(attr_value):
                setattr(cls, attr_name, decorator(attr_value))
        return cls
    return decorate

