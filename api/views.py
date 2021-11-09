"""
    Api handlers
"""
from rest_framework import status
from rest_framework.decorators import api_view
from api.utils import APIResponse, update_attrs
from api.models import Image, Label, Tag
from api.serializers import ImageSerializer, LabelSerializer, TagSerializer


@api_view(['GET'])
def default(_):
    """
        Default route
    """
    return APIResponse.success({
        'message': 'success'
    })


@api_view(['GET', 'POST'])
def handle_label(request):
    """
        Label handler
        GET: Get all labels
        POST: Create new label
    """
    if request.method == 'POST':
        # create new label

        label = Label(
            name=request.data["name"],
            category=request.data["category"],
        )
        label.save()
        return APIResponse.success(LabelSerializer(label).data)

    labels = Label.objects.all()

    return APIResponse.success(LabelSerializer(labels, many=True).data)


@api_view(['GET', 'PUT', 'DELETE'])
def handle_label_item(request, *args, **kwargs):
    """
        Handle label items
        GET: Get 1 label
        PUT: Update label item
        DELETE: Delete label item
    """

    label_id = kwargs['id']

    label = Label.objects.get(pk=label_id)
    if not label:
        return APIResponse.error(
            {"message": "Label not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        # Get label id
        return APIResponse.success(LabelSerializer(label).data)

    if request.method == 'DELETE':
        # Delete label
        label.delete()
        return APIResponse.success(None)

    # Update label
    label = update_attrs(label, **request.data)
    return APIResponse.success(LabelSerializer(label).data)


@api_view(['GET', 'POST'])
def handle_image(request):
    """
        Image handler
        GET: Get all images
        POST: Create new image
    """

    if request.method == 'POST':
        # create new image

        label = Label(
            name=request.data["name"],
            category=request.data["category"],
        )
        label.save()
        return APIResponse.success(LabelSerializer(label).data)

    labels = Label.objects.all()

    return APIResponse.success(LabelSerializer(labels, many=True).data)


@api_view(['GET', 'PUT', 'DELETE'])
def handle_image_item(request, *args, **kwargs):
    """
        Handle image items
        GET: Get 1 image
        PUT: Update image item
        DELETE: Delete image item
    """

    image_id = kwargs['id']
    image = Image.objects.get(pk=image_id)
    if not image:
        return APIResponse.error(
            {"message": "Image not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        # Get label id
        return APIResponse.success(ImageSerializer(image).data)


# @api_view(['GET', 'POST'])
# def handle_tag(request):
#     """
#         Tag handler
#         GET: Get all tags
#         POST: Create new tag
#     """
#     if request.method == 'POST':
#         # create new tag

#         label = Label(
#             name=request.data["name"],
#             category=request.data["category"],
#         )
#         label.save()
#         return APIResponse.success(LabelSerializer(label).data)

#     labels = Label.objects.all()

#     return APIResponse.success(LabelSerializer(labels, many=True).data)


# @api_view(['GET', 'PUT', 'DELETE'])
# def handle_tag_item(request, *args, **kwargs):
#     """
#         Handle tag items
#         GET: Get 1 tag
#         PUT: Update tag item
#         DELETE: Delete tag item
#     """

#     image_id = kwargs['id']
#     image = Image.objects.get(pk=image_id)
#     if not image:
#         return APIResponse.error(
#             {"message": "Image not found"},
#             status=status.HTTP_404_NOT_FOUND
#         )
