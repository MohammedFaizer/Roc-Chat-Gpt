from django.urls import path

from .views import Roc_Properties_Views

urlpatterns = [
    path("roc/properties", Roc_Properties_Views.as_view(), name="roc_properties"),
]
