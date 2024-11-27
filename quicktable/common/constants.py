# Success Constants
SUCCESS_MESSAGE = 'Operation completed successfully.'
SUCCESS_STATUS = 'success'
SUCCESS_DATA = 'data'

# Error Constants
ERROR_MESSAGE = 'An error occurred while processing the request.'
ERROR_STATUS = 'error'
ERROR_DATA = 'error'


INTERNAL_SERVER_ERROR_MESSAGE = 'Internal server error. Please try again later.'
INTERNAL_SERVER_ERROR_STATUS = 'error'

DUPLICATE_VALUE_ERROR_MESSAGE = 'Duplicate value found. Please use a unique value.'
DUPLICATE_VALUE_ERROR_STATUS = 'error'

NOT_FOUND_ERROR_MESSAGE = 'The requested resource was not found.'
NOT_FOUND_ERROR_STATUS = 'error'


# Success Case
SUCCESS_RESPONSE = {
    'message': SUCCESS_MESSAGE,
    'status': SUCCESS_STATUS,
}

# Generic Error Case
GENERIC_ERROR_RESPONSE = {
    'message': ERROR_MESSAGE,
    'status': ERROR_STATUS,
}

# Internal Server Error Case
INTERNAL_SERVER_ERROR_RESPONSE = {
    'message': INTERNAL_SERVER_ERROR_MESSAGE,
    'status': 'error'
}

# Duplicate Value Error Case
DUPLICATE_VALUE_ERROR_RESPONSE = {
    'message': DUPLICATE_VALUE_ERROR_MESSAGE,
    'status':  ERROR_STATUS
}

# Not Found Error Case
NOT_FOUND_ERROR_RESPONSE = {
    'message': NOT_FOUND_ERROR_MESSAGE,
    'status': NOT_FOUND_ERROR_STATUS
}

# Combined Error Responses for Organization
ERROR_RESPONSES = {
    'generic': GENERIC_ERROR_RESPONSE,
    'internal_server_error': INTERNAL_SERVER_ERROR_RESPONSE,
    'duplicate_value': DUPLICATE_VALUE_ERROR_RESPONSE,
    'not_found': NOT_FOUND_ERROR_RESPONSE
}