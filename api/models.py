"""
    API app models
"""
from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_on = models.DateTimeField(editable=False, auto_now_add=True)
    created_by = models.IntegerField(editable=False, blank=True, null=True)
    updated_on = models.DateTimeField(editable=False, auto_now=True)
    updated_by = models.IntegerField(editable=False, blank=True, null=True)

    class Meta:
        abstract = True


class Label(BaseModel):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)


class Image(BaseModel):
    src = models.ImageField(upload_to="images")


class Tag(BaseModel):
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    position = models.JSONField()
