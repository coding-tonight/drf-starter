import logging
import re

from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound, APIException

from .exceptions import FieldValidationError
from .constants import SUCCESS_RESPONSE, SUCCESS_DATA, ERROR_RESPONSES

logger = logging.getLogger('django')


class ResponseHandleMixins:
    """ ResponseHandleMixins
    """
    @staticmethod
    def handle_success_response(data = None, message = None) -> Response:
        
        RESPONSE = {
            **SUCCESS_RESPONSE,
            SUCCESS_DATA: data,
        }
        logger.info(f'response....{RESPONSE}')
        return Response(RESPONSE, status=status.HTTP_200_OK)
    
    @staticmethod
    def handle_error_response(exe, error = None, message = None) -> Response:
        
        logger.error(str(exe), exc_info=True)
        
        if isinstance(exe, FieldValidationError):
            RESPONSE = {
                **ERROR_RESPONSES['generic'],
                'error': exe.detail
            }
            return Response(RESPONSE, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        if isinstance(exe, NotFound):
            RESPONSE = {
                **ERROR_RESPONSES['generic'],
                'error': exe.detail
            }
            return Response(RESPONSE, status=status.HTTP_404_NOT_FOUND)
        
        if isinstance(exe, APIException):
           return Response(exe.detail, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
       

class FieldValidationMixins:    
    @staticmethod
    def is_email_valid(email: str) -> bool:
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        
        if status := re.match(regex, email):
            return status
        return status
        
        