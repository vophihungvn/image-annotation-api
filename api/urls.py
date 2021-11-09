from django.urls import path
from api import views

urlpatterns = [
    path('', views.default, name="default"),
    path('labels', views.handle_label, name='label'),
    path('labels/<str:id>', views.handle_label_item, name='label-item'),

    path('images', views.handle_image, name="image"),
    path('images/<str:id>', views.handle_image_item, name="image-item"),
    path('images/<str:id>/tags', views.handle_image_tag, name="image-tag"),

    path('tags/<str:id>', views.handle_tag_item, name="tag"),
]
