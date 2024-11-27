from rest_framework.exceptions import APIException, ValidationError, NotFound


class FieldValidationError(ValidationError):
    pass

class ShopNotFound(NotFound):
    pass