"""
    Api handlers
"""
from rest_framework.decorators import api_view
from api.utils import APIResponse


@api_view(['GET'])
def default(_):
    """
        Default route
    """
    return APIResponse.success({
        'message': 'success'
    })
