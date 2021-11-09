"""
    Utility for Api app
"""
from rest_framework import status
from rest_framework.response import Response


class APIResponse:
    """API response helper class"""
    @staticmethod
    def success(data):
        """Success response function"""
        result = {"status": status.HTTP_200_OK, "data": data}
        return Response(result, status=status.HTTP_200_OK)

    @staticmethod
    def error(errors):
        """Failure response function"""
        result = {"status": status.HTTP_400_BAD_REQUEST, "data": errors}
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
