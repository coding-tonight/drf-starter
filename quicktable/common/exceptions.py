from rest_framework.exceptions import ValidationError, NotFound , NotAuthenticated


class FieldValidationError(ValidationError):
    pass

class ShopNotFound(NotFound):
    pass

