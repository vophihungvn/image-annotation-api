from django.urls import path
from api import views

urlpatterns = [
    path('', views.default),
    path('labels', views.handle_label),
    path('labels/<str:id>', views.handle_label_item),

    path('images', views.handle_image),
    path('images/<str:id>', views.handle_label_item),
    # path('tags', views.handle_tag),
]
