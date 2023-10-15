from django.conf import settings

from rest_framework.exceptions import APIException, ValidationError, AuthenticationFailed, NotAuthenticated, MethodNotAllowed, PermissionDenied
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

from django.utils.translation import gettext_lazy as _

class ClientError(APIException):
    '''
    Custom exception for client-side related errors.
    '''
    
    status_code = 400
    default_detail = _('Invalid request.')

    def __init__(self, detail=default_detail, code=status_code):
        self.detail = {
            'status': 'failed',
            'code': code,
            'message': detail
        }
        self.status_code = code 

class SerializerValidationError(ValidationError):
    '''
    Custom exception for serializer field validation. Normally raised during field valdiation in serializers.    
    Note: Do not use in raising validation error. Always use serializers.ValidationError when overriding validate method.
    '''
   
    status_code = 400
    default_detail = _('Invalid input.')

    def __init__(self, detail=default_detail, code=status_code):       
        self.detail = detail 
        self.status_code = code
    

def custom_exception_handler(exc, context):
    '''
    Custom exception handler for certain exceptions    
    Note: This handler only checks for generic error,  404 and 403 are handled in views.
    '''
    # Call the default DRF exception handler to get the standard error response.
    response = exception_handler(exc, context)
    
    if response: # check if response is returned and then check for other exceptions that may arise    
        if isinstance(exc, NotAuthenticated):        
            error_data = {
                'status': 'fail',
                'code': 401,
                "message": _('Authentication credentials were not provided.'),
            }
            return Response(error_data, status = 401) 

        elif isinstance(exc, AuthenticationFailed):        
            error_data = {
                'status': 'fail',
                'code': 401,
                "message": _('Incorrect authentication credentials.'),
            }
            return Response(error_data, status = 401) 
        
        elif isinstance(exc, MethodNotAllowed):       
            request = context['request']
            method = request.method
             
            error_data = {
                'status': 'fail',
                'code': 405,
                "message": _(f'Method {method} not allowed.'),
            }
            return Response(error_data, status = 405)   
        
        elif isinstance(exc, PermissionDenied):       
                        
            error_data = {
                'status': 'fail',
                'code': 403,
                "message": _('You do not have permission to perform this action.'),
            }
            return Response(error_data, status = 403)      
        
        return response
    
    # check for any generic error if no response is returned 
    # comment out this part to see error stack trace during development (Django yellow screen)
    if isinstance(exc, Exception) and not settings.SHOW_ERROR_STACK_TRACE: 
        error_data = {
            "status": "error", 
            "message": "An error occurred while processing your request.",
            "code": 500,
            "data":{
                "detail": str(exc)
            }
        }
        return Response(error_data, status = 500) 
    
    
