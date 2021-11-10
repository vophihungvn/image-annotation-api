"""
    API serializer classes
"""
from rest_framework import serializers
from api.models import Label, Image, Tag


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    label = serializers.SerializerMethodField("_get_label")

    def _get_label(self, obj):
        """Get Label of tag"""
        label = Label.objects.filter(pk=obj.id).first()
        return LabelSerializer(label).data

    class Meta:
        model = Tag
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField("_get_tags")

    def _get_tags(self, obj):
        """Get all tags of image"""
        tags = Tag.objects.filter(image=obj)
        return TagSerializer(tags, many=True).data

    class Meta:
        model = Image
        fields = "__all__"
