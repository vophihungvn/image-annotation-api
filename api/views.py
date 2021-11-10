"""
    Api handlers
"""
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import (
    api_view,
    parser_classes,
    permission_classes
)
from api.utils import APIResponse, update_attrs
from api.models import Image, Label, Tag
from api.serializers import ImageSerializer, LabelSerializer, TagSerializer
from rest_framework.parsers import MultiPartParser, FileUploadParser


@api_view(['GET'])
def default(_):
    """
        Default route
    """
    return APIResponse.success({
        'message': 'success'
    })


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def handle_label(request):
    """
        Label handler
        GET: Get all labels
        POST: Create new label
    """
    user = request.user

    if request.method == 'POST':
        # create new label

        label = Label(
            name=request.data["name"],
            category=request.data["category"],
            created_by=user.id
        )
        label.save()
        return APIResponse.success(LabelSerializer(label).data)

    labels = Label.objects.filter(created_by=user.id).all()

    return APIResponse.success(LabelSerializer(labels, many=True).data)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def handle_label_item(request, *args, **kwargs):
    """
        Handle label items
        GET: Get 1 label
        PUT: Update label item
        DELETE: Delete label item
    """

    user = request.user

    label_id = kwargs['id']

    try:
        label = Label.objects.get(pk=label_id, created_by=user.id)
    except:
        return APIResponse.error(
            {"message": "Label not found"},
            status=status.HTTP_404_NOT_FOUND
        )
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
@parser_classes([MultiPartParser, FileUploadParser])
@permission_classes([IsAuthenticated])
def handle_image(request, *args, **kwargs):
    """
        Image handler
        GET: Get all images
        POST: Create new image
    """
    user = request.user
    if request.method == 'POST':
        # create new image
        image = Image(
            src=request.FILES['image'],
            created_by=user.id
        )

        image.save()
        return APIResponse.success(ImageSerializer(image).data)

    # List all images
    images = Image.objects.filter(created_by=user.id).all()

    return APIResponse.success(ImageSerializer(images, many=True).data)


@api_view(['GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def handle_image_item(request, *args, **kwargs):
    """
        Handle image items
        GET: Get 1 image
        DELETE: Delete image item
    """

    user = request.user

    image_id = kwargs['id']
    try:
        image = Image.objects.get(pk=image_id, created_by=user.id)
    except:
        return APIResponse.error(
            {"message": "Image not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        # Get image by id
        return APIResponse.success(ImageSerializer(image).data)

    # Delete image
    image.delete()
    return APIResponse.success(None)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def handle_image_tag(request, *args, **kwargs):
    """
        Handle image label
        GET: Get image labels
        POST: Add new image label
    """

    user = request.user

    image_id = kwargs['id']
    try:
        image = Image.objects.get(pk=image_id, created_by=user.id)
    except:
        return APIResponse.error(
            {"message": "Image not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'POST':
        label_id = request.data['label_id']

        try:
            label = Label.objects.get(pk=label_id, created_by=user.id)
        except:
            return APIResponse.error(
                {"message": "Label not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        tag = Tag(
            image=image,
            label=label,
            position=request.data.get('position'),
            created_by=user.id
        )

        tag.save()

        return APIResponse.success(TagSerializer(tag).data)

    tags = Tag.objects.filter(image_id=image_id, created_by=user.id)

    return APIResponse.success(TagSerializer(tags, many=True).data)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def handle_tag_item(request, *args, **kwargs):
    """
        Handle tag items
        GET: Get 1 tag
        PUT: Update tag item
        DELETE: Delete tag item
    """

    user = request.user
    tag_id = kwargs['id']

    tag = Tag.objects.get(pk=tag_id, created_by=user.id)
    if not tag:
        return APIResponse.error(
            {"message": "Tag not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        # Get tag id
        return APIResponse.success(TagSerializer(tag).data)

    if request.method == 'DELETE':
        # Delete tag
        tag.delete()
        return APIResponse.success(None)

    # Update tag
    tag = update_attrs(tag, **request.data)
    return APIResponse.success(TagSerializer(tag).data)
