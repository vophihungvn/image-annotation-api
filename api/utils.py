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
    def error(errors, status=status.HTTP_400_BAD_REQUEST):
        """Failure response function"""
        result = {"status": status, "data": errors}
        return Response(result, status=status)


def update_attrs(instance, **kwargs):
    """ Updates model instance attributes and saves the instance """
    instance_pk = instance.pk
    for key, value in kwargs.items():
        if hasattr(instance, key):
            setattr(instance, key, value)
        else:
            raise KeyError("Failed to update non existing attribute {}.{}".format(
                instance.__class__.__name__, key
            ))
    instance.save(force_update=True)
    return instance.__class__.objects.get(pk=instance_pk)
