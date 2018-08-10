from django.urls import path
from .views import ConvertView

urlpatterns = [
    path('', ConvertView.as_view(), name='usd_rub_converter'),
]
